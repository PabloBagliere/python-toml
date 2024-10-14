from field.field import Field
from criteria.criteria import Criteria
from dialect.sqlDialect import SQLDialect
from dataclasses import dataclass


@dataclass
class MySQLDialect(SQLDialect):
    def build_select_query(self, criteria: Criteria):
        fields = ", ".join([self.format_field(f) for f in criteria.fields]) or "*"
        where = self.format_whare(criteria.fields)
        sql = f"SELECT {fields} FROM {criteria.table}"

        # Añadimos los JOINS
        if criteria.joins:
            sql += " " + " ".join([str(j) for j in criteria.joins])

        # Añadir WHERE si está presente
        if where:
            sql += f" WHERE {where}"

        # Añadir LIMIT si está presente
        if hasattr(criteria, "limit") and criteria.limit is not None:
            sql += f" LIMIT {criteria.limit}"

        return sql

    def build_insert_query(self, criteria):
        # Implementación para un INSERT en MySQL
        pass

    def format_field(self, field: Field):
        # Los alias se formatean con `AS`, sin comillas adicionales
        if field.alias:
            return f"`{field.name}` AS `{field.alias}`"
        return f"`{field.name}`"

    def format_whare(self, fields: list[Field]):
        # Implementación para MySQL
        data = ""
        if not fields:
            return ""
        for c in fields:
            for condition in c.condition:
                data += f" `{c.name}` {condition.operator} '{condition.value}' {condition.condition}"
        data = data[:-3]
        return data.strip()
