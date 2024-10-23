from datetime import datetime
from typing import Any
from typing import Dict
from typing import Sequence
from typing import Tuple
from typing import Union
from urllib.parse import urljoin

from requests.models import Response

from tecton._internals import errors
from tecton_core import conf
from tecton_core import http


class IngestionClient:
    def __init__(self):
        # This configuration variable is ultimately coming from MDS.
        # Broadly speaking, the `get_or_raise` method below will call a `_get` method in conf.py,
        # which will look through the hierarchy of sources for a configuration variable.
        # If INGESTION_SERVICE is found via one of the acceptable ones, then it's used.
        # These sources include MDS, which is populated via the `GetConfigs` RPC. These RPC only provides
        # configurations specified in the server-side code, and this includes INGESTION_SERVICE.
        # See tecton/_internals/conf.py and tecton/_internals/metadata_service.py for more details
        domain = conf.get_or_raise("INGESTION_SERVICE")
        self.ingestion_url: str = urljoin(domain, "ingest")

    def ingest(
        self,
        workspace_name: str,
        push_source_name: str,
        ingestion_records: Sequence[Dict[str, Any]],
        dry_run: bool = False,
    ) -> Tuple[int, str, Union[Dict[str, Any], None]]:
        http_request = {
            "workspace_name": workspace_name,
            "dry_run": dry_run,
            "records": {
                push_source_name: [
                    {
                        "record": self._serialize_record(ingestion_record),
                    }
                    for ingestion_record in ingestion_records
                ]
            },
        }
        response = http.session().post(self.ingestion_url, json=http_request, headers=self._prepare_headers())
        return self._extract_from_response(response)

    @staticmethod
    def _extract_from_response(response: Response) -> Tuple[int, str, Union[Dict[str, Any], None]]:
        # NOTE: Responses not coming from our system will not necessarily be in JSON format

        if response.status_code != 200:
            error_message = f"Failed to ingest records: {response.reason}"
            try:
                response_data = response.json()
            except ValueError:
                response_data = None
                error_message += f"\nAdditionally, response content is not valid JSON: {response.text}"
            return response.status_code, error_message, response_data

        try:
            response_data = response.json()
        except ValueError:
            error_message = f"Response content is not valid JSON: {response.text}"
            return response.status_code, error_message, None
        return response.status_code, response.reason, response_data

    @staticmethod
    def _prepare_headers() -> Dict[str, str]:
        token = conf.get_or_none("TECTON_API_KEY")
        if not token:
            raise errors.FS_API_KEY_MISSING

        return {
            "authorization": f"Tecton-key {token}",
            "Content-Type": "application/json",
        }

    @staticmethod
    def _serialize_record(record: Dict[str, Any]) -> Dict[str, Any]:
        serialized_record = {}
        for k, v in record.items():
            if isinstance(v, datetime):
                serialized_record[k] = v.isoformat()
            else:
                serialized_record[k] = v
        return serialized_record
