from dialect.sqlDialect import SQLDialect


# Clase que representa un dialecto para SQLite
class SQLiteDialect(SQLDialect):
    # Implementación de SELECT para SQLite
    def build_select_query(self, criteria):
        fields = ", ".join([self.format_field(f) for f in criteria.fields]) or "*"
        sql = f"SELECT {fields} FROM {criteria.table}"

        # Añadimos los JOINS
        if criteria.joins:
            sql += " " + " ".join([str(j) for j in criteria.joins])

        # Añadimos las condiciones
        if criteria.conditions:
            conditions = " AND ".join([str(c) for c in criteria.conditions])
            sql += f" WHERE {conditions}"

        # Añadir LIMIT si está presente
        if hasattr(criteria, "limit") and criteria.limit is not None:
            sql += f" LIMIT {criteria.limit}"

        return sql

    # Implementación de INSERT para SQLite
    def build_insert_query(self, criteria):
        fields = ", ".join([f.name for f in criteria.fields])
        values = ", ".join([f"'{f.value}'" for f in criteria.fields])
        sql = f"INSERT INTO {criteria.table} ({fields}) VALUES ({values})"
        return sql

    # Formatear un campo para SQLite
    def format_field(self, field):
        # Los nombres de columnas y alias pueden estar entre comillas dobles
        if field.alias:
            return f'"{field.name}" AS "{field.alias}"'
        return f'"{field.name}"'
