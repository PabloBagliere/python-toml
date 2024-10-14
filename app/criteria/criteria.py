from field.field import Field
from builder.base import IBuilder
from dialect.sqlDialect import SQLDialect

from dataclasses import dataclass


@dataclass
class Criteria:
    table: str
    fields: list[Field]
    joins: list
    limit: int
    dialect: SQLDialect
    builder_class: IBuilder
    type_of_query: str = None

    def __init__(self, table: str, dialect: SQLDialect, builder_class: IBuilder):
        self.table: str = table
        self.fields: list[Field] = []
        self.joins = []
        self.limit: int = None
        self.dialect = dialect
        self.builder_class = builder_class

    def set_query_type(self, query_type: str):
        self.type_of_query = query_type
        return self

    def add_field(self, field: Field):
        self.fields.append(field)
        return self

    def add_join(self, join):
        self.joins.append(join)
        return self

    def set_limit(self, limit: int):
        self.limit = limit
        return self

    def build(self):
        builder = self.builder_class(self.dialect, self)
        return builder.build_query()
