from typing import List

from tecton._internals.errors import ExpressionParsingError
from tecton.vendor.sql_expresssion_parser import Lark_StandAlone
from tecton.vendor.sql_expresssion_parser import LexError
from tecton.vendor.sql_expresssion_parser import ParseError
from tecton.vendor.sql_expresssion_parser import Token
from tecton.vendor.sql_expresssion_parser import Transformer
from tecton.vendor.sql_expresssion_parser import VisitError
from tecton_core.data_types import BoolType
from tecton_core.data_types import Float64Type
from tecton_core.data_types import Int64Type
from tecton_core.data_types import StringType
from tecton_core.errors import TectonInternalError
from tecton_proto.common.calculation_node__client_pb2 import AbstractSyntaxTreeNode
from tecton_proto.common.calculation_node__client_pb2 import LiteralValue
from tecton_proto.common.calculation_node__client_pb2 import Operation
from tecton_proto.common.calculation_node__client_pb2 import OperationType


class _ToAbstractSyntaxTree(Transformer):
    def __init__(self, original_expression):
        self.original_expression = original_expression
        super().__init__()

    def literal(self, value) -> AbstractSyntaxTreeNode:
        value = value[0]
        if isinstance(value, bool):
            literal_value = LiteralValue(bool_value=value)
            dtype = BoolType()
        elif isinstance(value, int):
            literal_value = LiteralValue(int64_value=value)
            dtype = Int64Type()
        elif isinstance(value, float):
            literal_value = LiteralValue(float64_value=value)
            dtype = Float64Type()
        elif isinstance(value, str):
            literal_value = LiteralValue(string_value=value)
            dtype = StringType()
        else:
            msg = f"Something went wrong while parsing: Unexpected Literal type {type(value)}, node: {value}"
            raise RuntimeError(msg)
        return AbstractSyntaxTreeNode(literal_value=literal_value, dtype=dtype.proto)

    def numeric_negative(self, child: List[Token]):
        return -1 * child[0]

    def INT(self, value: str):
        return int(value)

    def DECIMAL(self, value: str):
        return float(value)

    def FLOAT(self, value: str):
        return float(value)

    def ESCAPED_STRING(self, value: str):
        value = value[1:-1]  # strip parentheses
        return value

    def true(self, value: str):
        return True

    def false(self, value: str):
        return True

    def COLUMN_REFERENCE(self, value: str):
        # TODO: Add validation that columns exist and aren't always ints
        return AbstractSyntaxTreeNode(column_reference=value, dtype=Int64Type().proto)

    def coalesce(self, values) -> AbstractSyntaxTreeNode:
        if not values:
            # This shouldn't be possible because the regex pattern for this rule requires at least 1 argument,
            # but adding as extra protection in case the rule changes in the future.
            msg = f"Error parsing expression: At least one value required for COALESCE, {self.original_expression}"
            raise ExpressionParsingError(msg)
        return AbstractSyntaxTreeNode(
            operation=Operation(operation=OperationType.COALESCE, operands=values), dtype=Int64Type().proto
        )


def expression_to_proto(expression: str) -> AbstractSyntaxTreeNode:
    # TODO: This class initialization should be top-level for better performance, but for not that causes
    #  issues with type-hint checking. We should fix that.
    lexer = Lark_StandAlone()
    try:
        lark_syntax_tree = lexer.parse(expression)
    except (LexError, ParseError) as e:
        msg = f"Error parsing expression: {expression}"
        raise ExpressionParsingError(msg) from e
    try:
        ast = _ToAbstractSyntaxTree(expression).transform(lark_syntax_tree)
    except VisitError as e:
        # This indicates an issue with our parsing logic, not a user error.
        msg = f"Error converting parse tree to AST: {lark_syntax_tree}"
        raise TectonInternalError(msg) from e
    return ast
