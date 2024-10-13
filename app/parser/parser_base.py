# Interfaz base para los parsers de los distintos tipos de archivos

from abc import ABC, abstractmethod


class IParser(ABC):
    @abstractmethod
    def parse(self, file_path):
        pass
