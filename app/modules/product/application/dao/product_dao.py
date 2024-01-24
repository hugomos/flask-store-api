from uuid import UUID
from abc import ABC, abstractmethod


class ProductRaw:
    def __init__(self, id: str, name: str, description: str, price: float):
        self.id = id
        self.name = name
        self.description = description
        self.price = price


class ProductDAO(ABC):

    @abstractmethod
    def exists_by_id(self, id: UUID) -> bool:
        pass

    @abstractmethod
    def find_many(self) -> list[ProductRaw]:
        pass
