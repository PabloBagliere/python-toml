from builder.base import IBuilder
from criteria.criteria import Criteria
from dialect.sqlDialect import SQLDialect


class SQLBuilder(IBuilder):
    def __init__(self, dialect: SQLDialect, criteria: Criteria):
        self.dialect = dialect
        self.criteria = criteria

    def build_query(self):
        if self.criteria.type_of_query == "consulta":
            return self.dialect.build_select_query(self.criteria)
        elif self.criteria.type_of_query == "INSERT":
            return self.dialect.build_insert_query(self.criteria)
        raise NotImplementedError(
            f"Query type {self.criteria.type_of_query} not implemented."
        )
