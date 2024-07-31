from abc import ABC, abstractmethod
from typing import Set, Self
from pandas import DataFrame
from pathlib import Path


class ExternalDataSource(ABC):
    instances: Set[Self] = set()

    @classmethod
    def get_instances(cls) -> Set[Self]:
        return cls.instances

    @classmethod
    def save_prices_data(cls, data: DataFrame, path: Path) -> None:
        data.to_csv(path, sep='\t')
        # todo: error handling

    @property
    @abstractmethod
    def name(self):
        ...

    @property
    @abstractmethod
    def url(self):
        ...

    @property
    @abstractmethod
    def prices_data(self):
        pass

    @property
    @abstractmethod
    def logs_path(self):
        pass
