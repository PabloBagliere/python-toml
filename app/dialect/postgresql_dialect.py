from dialect.sqlDialect import SQLDialect


class PostgreSQLDialect(SQLDialect):
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

    def build_insert_query(self, criteria):
        # Implementación para un INSERT en PostgreSQL
        pass

    def format_field(self, field):
        # Los nombres de columnas y alias pueden estar entre comillas dobles
        if field.alias:
            return f'"{field.name}" AS "{field.alias}"'
        return f'"{field.name}"'
