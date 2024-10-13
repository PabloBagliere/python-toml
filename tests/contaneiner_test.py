from app.conteiner.container import Container
from app.parser.parser_base import IParser


class mock_parser(IParser):
    def parse(self, file_path):
        return file_path


def test_container_mysql_select():
    file_data = {
        "system": {
            "version": "0.1.0",
            "type": "consulta",
            "description": "Consulta los países del mundo",
            "table": "country",
            "limit": 10,
            "dialect": "mysql",
        },
        "field": [
            {
                "name": "Code",
                "type": "char",
                "primary": True,
                "length": 3,
                "as": "Código",
            },
            {"name": "Name", "type": "char", "length": 52, "as": "Nombre"},
            {"name": "Region", "type": "char", "length": 26},
            {"name": "Population", "type": "int"},
        ],
    }
    container = Container(mock_parser())
    query = container.build_query(file_data)
    assert (
        query
        == "SELECT `Code` AS `Código`, `Name` AS `Nombre`, `Region`, `Population` FROM country LIMIT 10"
    )


def test_container_posgres_select():
    file_data = {
        "system": {
            "version": "0.1.0",
            "type": "consulta",
            "description": "Consulta los países del mundo",
            "table": "country",
            "limit": 10,
            "dialect": "postgresql",
        },
        "field": [
            {
                "name": "Code",
                "type": "char",
                "primary": True,
                "length": 3,
                "as": "Código",
            },
            {"name": "Name", "type": "char", "length": 52, "as": "Nombre"},
            {"name": "Region", "type": "char", "length": 26},
            {"name": "Population", "type": "int"},
        ],
    }
    container = Container(mock_parser())
    query = container.build_query(file_data)
    assert (
        query
        == 'SELECT "Code" AS "Código", "Name" AS "Nombre", "Region", "Population" FROM country LIMIT 10'
    )


def test_container_sqlite_select():
    file_data = {
        "system": {
            "version": "0.1.0",
            "type": "consulta",
            "description": "Consulta los países del mundo",
            "table": "country",
            "limit": 10,
            "dialect": "sqlite",
        },
        "field": [
            {
                "name": "Code",
                "type": "char",
                "primary": True,
                "length": 3,
                "as": "Código",
            },
            {"name": "Name", "type": "char", "length": 52, "as": "Nombre"},
            {"name": "Region", "type": "char", "length": 26},
            {"name": "Population", "type": "int"},
        ],
    }
    container = Container(mock_parser())
    query = container.build_query(file_data)
    assert (
        query
        == 'SELECT "Code" AS "Código", "Name" AS "Nombre", "Region", "Population" FROM country LIMIT 10'
    )
