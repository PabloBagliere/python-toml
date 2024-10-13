from conteiner.container import Container
from parser.toml_parser import TOMLParser

if __name__ == "__main__":
    file_path = "consulta.toml"
    container = Container(TOMLParser())
    query = container.build_query(file_path)
    print(query)
