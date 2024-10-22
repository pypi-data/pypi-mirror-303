from abc import ABC, abstractmethod


class _Config(ABC):
    _template: dict = None

    def _init_template(self) -> dict:
        if self._template is None:
            self._template = self._init_data()
        return self._template

    @staticmethod
    def _init_data(data: dict = None) -> dict:
        if data is None:
            data = {}
        return data


    @abstractmethod
    def compile(self): ...
