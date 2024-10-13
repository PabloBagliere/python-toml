from field.field import Field
from criteria.criteria import Criteria
from dialect.mysql_dialect import MySQLDialect
from dialect.postgresql_dialect import PostgreSQLDialect
from dialect.sqlite_dialect import SQLiteDialect
from builder.sql_builder import SQLBuilder
from parser.parser_base import IParser


class Container:
    def __init__(self, parser: IParser):
        self.dialects = {
            "mysql": MySQLDialect(),
            "postgresql": PostgreSQLDialect(),
            "sqlite": SQLiteDialect(),
        }
        self.parser = parser

    def create_criteria(self, data):
        system_info = data["system"]
        table = system_info["table"]
        query_type = system_info["type"]
        limit = system_info.get("limit", None)
        dialect_name = system_info["dialect"]

        # Elegir el dialecto adecuado según el valor en el archivo TOML
        if dialect_name not in self.dialects:
            raise ValueError(f"Dialect {dialect_name} not supported")
        dialect = self.dialects[dialect_name]

        # Crear el Criteria
        criteria = Criteria(table, dialect, SQLBuilder)
        criteria.set_query_type(query_type)

        # Extraer los campos
        fields = data.get("field", [])
        for field_data in fields:
            field = Field(
                name=field_data["name"],
                field_type=field_data["type"],
                primary=field_data.get("primary", False),
                length=field_data.get("length", None),
                alias=field_data.get("as", None),
            )
            criteria.add_field(field)

        # Si hay un límite, lo aplicamos
        if limit:
            criteria.set_limit(limit)

        return criteria

    def build_query(self, file_path):
        data = self.parser.parse(file_path)
        criteria = self.create_criteria(data)
        query = criteria.build()
        return query
