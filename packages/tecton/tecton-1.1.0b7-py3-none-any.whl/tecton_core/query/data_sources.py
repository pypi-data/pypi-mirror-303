import datetime
import itertools
import time
from functools import reduce
from operator import and_
from typing import Callable
from typing import Optional
from typing import Tuple
from typing import Union

import attrs
import pandas
import pyarrow

from tecton_core import conf
from tecton_core import duckdb_factory
from tecton_core import id_helper
from tecton_core import specs
from tecton_core.offline_store import BotoOfflineStoreOptionsProvider
from tecton_core.query.errors import UserCodeError
from tecton_core.query.executor_params import ExecutionContext
from tecton_core.query.nodes import DataSourceScanNode
from tecton_core.query.pandas.node import ArrowExecNode
from tecton_core.schema import Schema
from tecton_core.schema_validation import tecton_schema_to_arrow_schema
from tecton_core.specs import DatetimePartitionColumnSpec
from tecton_core.time_utils import get_timezone_aware_datetime
from tecton_proto.args.pipeline__client_pb2 import DataSourceNode
from tecton_proto.data import batch_data_source__client_pb2 as batch_data_source_pb2


@attrs.define
class FileDataSourceScanNode(ArrowExecNode):
    ds: specs.DataSourceSpec
    ds_node: Optional[DataSourceNode]
    is_stream: bool = attrs.field()
    start_time: Optional[datetime.datetime] = None
    end_time: Optional[datetime.datetime] = None

    @classmethod
    def from_node_input(cls, query_node: DataSourceScanNode) -> "FileDataSourceScanNode":
        assert isinstance(query_node.ds.batch_source, specs.FileSourceSpec)
        return cls.from_node_inputs(query_node, input_node=None)

    @property
    def spec(self) -> specs.FileSourceSpec:
        return self.ds.batch_source

    def to_arrow_reader(self, context: ExecutionContext) -> pyarrow.RecordBatchReader:
        import duckdb

        file_uri = self.spec.uri
        timestamp_field = self.spec.timestamp_field

        schema = Schema(self.ds.schema.tecton_schema) if self.ds.schema else None
        arrow_schema = tecton_schema_to_arrow_schema(schema) if schema else None
        if self.spec.timestamp_format and arrow_schema:
            # replace timestamp column type with string,
            # we will convert timestamp with DuckDB (see below)
            timestamp_pos = arrow_schema.names.index(timestamp_field)
            arrow_schema = arrow_schema.set(timestamp_pos, pyarrow.field(timestamp_field, pyarrow.string()))

        proto_format = self.spec.file_format
        if proto_format == batch_data_source_pb2.FILE_DATA_SOURCE_FORMAT_CSV:
            arrow_format = "csv"
        elif proto_format == batch_data_source_pb2.FILE_DATA_SOURCE_FORMAT_JSON:
            arrow_format = "json"
        elif proto_format == batch_data_source_pb2.FILE_DATA_SOURCE_FORMAT_PARQUET:
            arrow_format = "parquet"
        else:
            raise ValueError(batch_data_source_pb2.FileDataSourceFormat.Name(self.spec.file_format))

        fs, path = pyarrow.fs.FileSystem.from_uri(file_uri)
        if isinstance(fs, pyarrow.fs.S3FileSystem):
            options = BotoOfflineStoreOptionsProvider.static_options()
            if options is not None:
                fs = pyarrow.fs.S3FileSystem(
                    access_key=options.access_key_id,
                    secret_key=options.secret_access_key,
                    session_token=options.session_token,
                    # When created via Filesystem.from_uri, the bucket region will be autodetected. This constructor
                    # does not have a bucket from which it can detect the region, so we need to copy it over from the
                    # previous instance.
                    region=fs.region,
                )

        # There seems to be a bug in Arrow related to the explicit schema:
        # when we pass an explicit schema to `dataset` and both resolution and timezone in the timestamp column
        # don't match the schema in parquet files - filters that are pushed down by DuckDB will not work.
        # It is very likely that we will not guess both resolution and timezone correctly.
        # So we won't pass schema for now.
        arrow_schema = arrow_schema if arrow_format != "parquet" else None

        partitioning = None
        partition_filter = None
        # If source supports partitions then only read the relevant partitions
        if (self.start_time or self.end_time) and self.spec.datetime_partition_columns:
            partition_fields = []
            filter_conditions = []
            for i, partition in enumerate(self.spec.datetime_partition_columns):
                partition_col = partition.column_name if partition.column_name else f"_dir_partition_{i}"
                partition_type = None
                partition_value_at_start = None
                partition_value_at_end = None

                if self.start_time:
                    partition_value_at_start, partition_type = _partition_value_and_type_for_time(
                        partition, self.start_time
                    )
                if self.end_time:
                    partition_value_at_end, partition_type = _partition_value_and_type_for_time(
                        partition, self.end_time
                    )

                if partition_value_at_start == partition_value_at_end:
                    # Use the partition path to reduce scanning for metadata when initializing the dataset
                    hive_key = f"{partition.column_name}=" if partition.column_name else ""
                    partition_value = self.start_time.strftime(partition.format_string)
                    path = path.rstrip("/") + f"/{hive_key}{self.start_time.strftime(partition_value)}"
                else:
                    # Otherwise we use a range filter and break so we don't combine hierarchical partition filters
                    partition_fields.append(pyarrow.field(partition_col, partition_type))
                    filter_conditions.append((pyarrow.dataset.field(partition_col) >= partition_value_at_start))
                    filter_conditions.append((pyarrow.dataset.field(partition_col) <= partition_value_at_end))
                    # TODO: combine range filters on hierarchical partitions using nested 'Or' filters
                    break

            # Setup dataset partitioning if we used partition range filters
            if partition_fields:
                partitioning = pyarrow.dataset.partitioning(
                    pyarrow.schema(partition_fields),
                    # default is a directory partition
                    flavor="hive" if self.spec.datetime_partition_columns[0].column_name else None,
                )
                partition_filter = reduce(and_, filter_conditions)

        file_dataset = pyarrow.dataset.dataset(
            source=path, schema=arrow_schema, filesystem=fs, format=arrow_format, partitioning=partitioning
        )
        reader = pyarrow.RecordBatchReader.from_batches(
            file_dataset.schema, file_dataset.to_batches(filter=partition_filter)
        )
        if self.spec.post_processor:

            def _map(input_df: pandas.DataFrame) -> pandas.DataFrame:
                try:
                    return self.spec.post_processor(input_df)
                except Exception as exc:
                    msg = "Post processor function of data source " f"('{self.spec.name}') " f"failed with exception"
                    raise UserCodeError(msg) from exc

            reader = map_batches(reader, _map)

        # ToDo: consider using pyarrow compute instead
        duckdb_session = duckdb_factory.create_connection()
        relation = duckdb_session.from_arrow(reader)
        column_types = dict(zip(relation.columns, relation.dtypes))

        if column_types[timestamp_field] == duckdb.typing.VARCHAR:
            if self.spec.timestamp_format:
                conversion_exp = f"strptime(\"{timestamp_field}\", '{self.spec.timestamp_format}')"
            else:
                conversion_exp = f'CAST("{timestamp_field}" AS TIMESTAMP)'
            relation = relation.select(f'* REPLACE({conversion_exp} AS "{timestamp_field}")')

        if self.start_time:
            if column_types[timestamp_field] == duckdb.typing.TIMESTAMP_TZ:
                start_time = get_timezone_aware_datetime(self.start_time)
            else:
                start_time = self.start_time.replace(tzinfo=None)
            relation = relation.filter(f"\"{timestamp_field}\" >= '{start_time}'")
        if self.end_time:
            if column_types[timestamp_field] == duckdb.typing.TIMESTAMP_TZ:
                end_time = get_timezone_aware_datetime(self.end_time)
            else:
                end_time = self.end_time.replace(tzinfo=None)
            relation = relation.filter(f"\"{timestamp_field}\" < '{end_time}'")

        return relation.fetch_arrow_reader()

    def as_str(self):
        return f"FileDataSourceScanNode for {self.ds.name}"


@attrs.define
class PushTableSourceScanNode(ArrowExecNode):
    ds: specs.DataSourceSpec
    ds_node: Optional[DataSourceNode]
    is_stream: bool = attrs.field()
    start_time: Optional[datetime.datetime] = None
    end_time: Optional[datetime.datetime] = None

    @classmethod
    def from_node_input(cls, query_node: DataSourceScanNode) -> "PushTableSourceScanNode":
        assert isinstance(query_node.ds.batch_source, specs.PushTableSourceSpec)
        return cls.from_node_inputs(query_node, input_node=None)

    @property
    def spec(self) -> specs.PushTableSourceSpec:
        return self.ds.batch_source

    def to_arrow_reader(self, context: ExecutionContext) -> pyarrow.RecordBatchReader:
        from deltalake import DeltaTable

        ds_id = id_helper.IdHelper.from_string(self.ds.id)
        creds = next(
            filter(
                lambda o: o is not None,
                (p.get_s3_options_for_data_source(ds_id) for p in context.offline_store_options_providers),
            ),
            None,
        )
        if not creds:
            msg = f"Unable to retrieve S3 store credentials for data source {self.ds.name}"
            raise Exception(msg)
        storage_options = {
            "AWS_ACCESS_KEY_ID": creds.access_key_id,
            "AWS_SECRET_ACCESS_KEY": creds.secret_access_key,
            "AWS_SESSION_TOKEN": creds.session_token,
            "AWS_S3_LOCKING_PROVIDER": "dynamodb",
            "AWS_REGION": conf.get_or_raise("CLUSTER_REGION"),
        }
        saved_error = None
        for _ in range(20):
            try:
                table = DeltaTable(table_uri=self.spec.ingested_data_location, storage_options=storage_options)
                break
            except OSError as e:
                saved_error = e
                time.sleep(0.1)
        else:
            msg = "Failed to read from S3"
            raise TimeoutError(msg) from saved_error
        ds = table.to_pyarrow_dataset()
        return pyarrow.RecordBatchReader.from_batches(ds.schema, ds.to_batches())

    def as_str(self):
        return f"PushTableSourceScanNode for {self.ds.name}"


def _partition_value_and_type_for_time(
    partition: DatetimePartitionColumnSpec, dt: datetime
) -> Tuple[Union[int, datetime.date], pyarrow.DataType]:
    fmt = partition.format_string
    if fmt == "%-Y" or fmt == "%Y":
        return dt.year, pyarrow.int32()
    elif fmt == "%-m" or fmt == "%m":
        return dt.month, pyarrow.int32()
    elif fmt == "%-d" or fmt == "%d":
        return dt.day, pyarrow.int32()
    elif fmt == "%-H" or fmt == "%H":
        return dt.hour, pyarrow.int32()
    elif fmt == "%Y-%m-%d":
        return dt.date(), pyarrow.date32()
    else:
        msg = f"Datetime format `{fmt}` not supported for partition column {partition.column_name}"
        raise ValueError(msg)


def map_batches(
    input_: pyarrow.RecordBatchReader, map_: Callable[[pandas.DataFrame], pandas.DataFrame]
) -> pyarrow.RecordBatchReader:
    def gen():
        while True:
            try:
                batch = input_.read_next_batch()
            except StopIteration:
                return
            processed = map_(batch.to_pandas())
            yield pyarrow.RecordBatch.from_pandas(processed)

    batches = gen()
    first_batch = next(batches)
    return pyarrow.RecordBatchReader.from_batches(first_batch.schema, itertools.chain([first_batch], batches))
