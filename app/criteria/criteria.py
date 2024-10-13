from builder.base import IBuilder
from dialect.sqlDialect import SQLDialect


class Criteria:
    def __init__(self, table, dialect: SQLDialect, builder_class: IBuilder):
        self.table = table
        self.fields = []
        self.conditions = []
        self.joins = []
        self.limit = None
        self.dialect = dialect
        self.builder_class = builder_class

    def set_query_type(self, query_type):
        self.type_of_query = query_type
        return self

    def add_field(self, field):
        self.fields.append(field)
        return self

    def add_condition(self, condition):
        self.conditions.append(condition)
        return self

    def add_join(self, join):
        self.joins.append(join)
        return self

    def set_limit(self, limit):
        self.limit = limit
        return self

    def build(self):
        builder = self.builder_class(self.dialect, self)
        return builder.build_query()
