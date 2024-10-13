from abc import ABC, abstractmethod


class SQLDialect(ABC):
    @abstractmethod
    def build_select_query(self, criteria):
        pass

    @abstractmethod
    def build_insert_query(self, criteria):
        pass

    @abstractmethod
    def format_field(self, field):
        pass
