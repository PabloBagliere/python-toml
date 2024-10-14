from parser.parser_base import IParser
import tomli
from dataclasses import dataclass


@dataclass
class TOMLParser(IParser):
    def load_file(self, file_path):
        # Cargar el archivo TOML
        with open(file_path, "rb") as file:
            data = tomli.load(file)
        return data

    def parse(self, file_path):
        # Cargar los datos del archivo .toml
        data = self.load_file(file_path)
        return data
