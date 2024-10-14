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


def test_container_mysql_select_no_limit_no_as():
    file_data = {
        "system": {
            "version": "0.1.0",
            "type": "consulta",
            "description": "Consulta los países del mundo",
            "table": "country",
            "dialect": "mysql",
        },
        "field": [
            {"name": "Code", "type": "char", "primary": True, "length": 3},
            {"name": "Name", "type": "char", "length": 52},
            {"name": "Region", "type": "char", "length": 26},
            {"name": "Population", "type": "int"},
        ],
    }
    container = Container(mock_parser())
    query = container.build_query(file_data)
    assert query == "SELECT `Code`, `Name`, `Region`, `Population` FROM country"


def test_container_posgres_select_no_limit_no_as():
    file_data = {
        "system": {
            "version": "0.1.0",
            "type": "consulta",
            "description": "Consulta los países del mundo",
            "table": "country",
            "dialect": "postgresql",
        },
        "field": [
            {"name": "Code", "type": "char", "primary": True, "length": 3},
            {"name": "Name", "type": "char", "length": 52},
            {"name": "Region", "type": "char", "length": 26},
            {"name": "Population", "type": "int"},
        ],
    }
    container = Container(mock_parser())
    query = container.build_query(file_data)
    assert query == 'SELECT "Code", "Name", "Region", "Population" FROM country'


def test_container_sqlite_select_no_limit_no_as():
    file_data = {
        "system": {
            "version": "0.1.0",
            "type": "consulta",
            "description": "Consulta los países del mundo",
            "table": "country",
            "dialect": "sqlite",
        },
        "field": [
            {"name": "Code", "type": "char", "primary": True, "length": 3},
            {"name": "Name", "type": "char", "length": 52},
            {"name": "Region", "type": "char", "length": 26},
            {"name": "Population", "type": "int"},
        ],
    }
    container = Container(mock_parser())
    query = container.build_query(file_data)
    assert query == 'SELECT "Code", "Name", "Region", "Population" FROM country'


def test_container_mysql_select_no_as():
    file_data = {
        "system": {
            "version": "0.1.0",
            "type": "consulta",
            "description": "Consulta los países del mundo",
            "table": "country",
            "dialect": "mysql",
            "limit": 10,
        },
        "field": [
            {"name": "Code", "type": "char", "primary": True, "length": 3},
            {"name": "Name", "type": "char", "length": 52},
            {"name": "Region", "type": "char", "length": 26},
            {"name": "Population", "type": "int"},
        ],
    }
    container = Container(mock_parser())
    query = container.build_query(file_data)
    assert (
        query == "SELECT `Code`, `Name`, `Region`, `Population` FROM country LIMIT 10"
    )


def test_container_posgres_select_no_as():
    file_data = {
        "system": {
            "version": "0.1.0",
            "type": "consulta",
            "description": "Consulta los países del mundo",
            "table": "country",
            "dialect": "postgresql",
            "limit": 10,
        },
        "field": [
            {"name": "Code", "type": "char", "primary": True, "length": 3},
            {"name": "Name", "type": "char", "length": 52},
            {"name": "Region", "type": "char", "length": 26},
            {"name": "Population", "type": "int"},
        ],
    }
    container = Container(mock_parser())
    query = container.build_query(file_data)
    assert (
        query == 'SELECT "Code", "Name", "Region", "Population" FROM country LIMIT 10'
    )


def test_container_sqlite_select_no_as():
    file_data = {
        "system": {
            "version": "0.1.0",
            "type": "consulta",
            "description": "Consulta los países del mundo",
            "table": "country",
            "dialect": "sqlite",
            "limit": 10,
        },
        "field": [
            {"name": "Code", "type": "char", "primary": True, "length": 3},
            {"name": "Name", "type": "char", "length": 52},
            {"name": "Region", "type": "char", "length": 26},
            {"name": "Population", "type": "int"},
        ],
    }
    container = Container(mock_parser())
    query = container.build_query(file_data)
    assert (
        query == 'SELECT "Code", "Name", "Region", "Population" FROM country LIMIT 10'
    )


def test_container_sqlite_select_wheres():
    file_data = {
        "system": {
            "version": "0.1.0",
            "type": "consulta",
            "description": "Consulta los países del mundo",
            "table": "country",
            "dialect": "sqlite",
            "limit": 10,
        },
        "field": [
            {"name": "Code", "type": "char", "primary": True, "length": 3},
            {"name": "Name", "type": "char", "length": 52},
            {"name": "Region", "type": "char", "length": 26},
            {
                "name": "Population",
                "type": "int",
                "conditions": [
                    {"operator": "<", "value": 1000000, "condition": "AND"},
                    {"operator": ">", "value": 1000, "condition": "OR"},
                ],
            },
        ],
    }
    container = Container(mock_parser())
    query = container.build_query(file_data)
    assert (
        query
        == 'SELECT "Code", "Name", "Region", "Population" FROM country WHERE "Population" < \'1000000\' AND "Population" > \'1000\' LIMIT 10'
    )


def test_container_mysql_select_wheres():
    file_data = {
        "system": {
            "version": "0.1.0",
            "type": "consulta",
            "description": "Consulta los países del mundo",
            "table": "country",
            "dialect": "mysql",
            "limit": 10,
        },
        "field": [
            {"name": "Code", "type": "char", "primary": True, "length": 3},
            {"name": "Name", "type": "char", "length": 52},
            {"name": "Region", "type": "char", "length": 26},
            {
                "name": "Population",
                "type": "int",
                "conditions": [
                    {"operator": "<", "value": 1000000, "condition": "AND"},
                    {"operator": ">", "value": 1000, "condition": "OR"},
                ],
            },
        ],
    }
    container = Container(mock_parser())
    query = container.build_query(file_data)
    assert (
        query
        == "SELECT `Code`, `Name`, `Region`, `Population` FROM country WHERE `Population` < '1000000' AND `Population` > '1000' LIMIT 10"
    )


def test_container_postgres_select_wheres():
    file_data = {
        "system": {
            "version": "0.1.0",
            "type": "consulta",
            "description": "Consulta los países del mundo",
            "table": "country",
            "dialect": "postgresql",
            "limit": 10,
        },
        "field": [
            {"name": "Code", "type": "char", "primary": True, "length": 3},
            {"name": "Name", "type": "char", "length": 52},
            {"name": "Region", "type": "char", "length": 26},
            {
                "name": "Population",
                "type": "int",
                "conditions": [
                    {"operator": "<", "value": 1000000, "condition": "AND"},
                    {"operator": ">", "value": 1000, "condition": "OR"},
                ],
            },
        ],
    }
    container = Container(mock_parser())
    query = container.build_query(file_data)
    assert (
        query
        == 'SELECT "Code", "Name", "Region", "Population" FROM country WHERE "Population" < \'1000000\' AND "Population" > \'1000\' LIMIT 10'
    )


def test_container_sqlite_select_where():
    file_data = {
        "system": {
            "version": "0.1.0",
            "type": "consulta",
            "description": "Consulta los países del mundo",
            "table": "country",
            "dialect": "sqlite",
            "limit": 10,
        },
        "field": [
            {"name": "Code", "type": "char", "primary": True, "length": 3},
            {"name": "Name", "type": "char", "length": 52},
            {"name": "Region", "type": "char", "length": 26},
            {
                "name": "Population",
                "type": "int",
                "conditions": [{"operator": "<", "value": 1000000, "condition": "AND"}],
            },
        ],
    }
    container = Container(mock_parser())
    query = container.build_query(file_data)
    assert (
        query
        == 'SELECT "Code", "Name", "Region", "Population" FROM country WHERE "Population" < \'1000000\' LIMIT 10'
    )


def test_container_mysql_select_where():
    file_data = {
        "system": {
            "version": "0.1.0",
            "type": "consulta",
            "description": "Consulta los países del mundo",
            "table": "country",
            "dialect": "mysql",
            "limit": 10,
        },
        "field": [
            {"name": "Code", "type": "char", "primary": True, "length": 3},
            {"name": "Name", "type": "char", "length": 52},
            {"name": "Region", "type": "char", "length": 26},
            {
                "name": "Population",
                "type": "int",
                "conditions": [{"operator": "<", "value": 1000000, "condition": "AND"}],
            },
        ],
    }
    container = Container(mock_parser())
    query = container.build_query(file_data)
    assert (
        query
        == "SELECT `Code`, `Name`, `Region`, `Population` FROM country WHERE `Population` < '1000000' LIMIT 10"
    )


def test_container_postgres_select_where():
    file_data = {
        "system": {
            "version": "0.1.0",
            "type": "consulta",
            "description": "Consulta los países del mundo",
            "table": "country",
            "dialect": "postgresql",
            "limit": 10,
        },
        "field": [
            {"name": "Code", "type": "char", "primary": True, "length": 3},
            {"name": "Name", "type": "char", "length": 52},
            {"name": "Region", "type": "char", "length": 26},
            {
                "name": "Population",
                "type": "int",
                "conditions": [
                    {"operator": "<", "value": 1000000, "condition": "OR"},
                ],
            },
        ],
    }
    container = Container(mock_parser())
    query = container.build_query(file_data)
    assert (
        query
        == 'SELECT "Code", "Name", "Region", "Population" FROM country WHERE "Population" < \'1000000\' LIMIT 10'
    )
