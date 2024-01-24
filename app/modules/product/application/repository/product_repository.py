from uuid import UUID
from abc import ABC, abstractmethod

from modules.product.domain.entity.product import Product


class ProductRepository(ABC):

    @abstractmethod
    def save(self, product: Product):
        pass

    @abstractmethod
    def delete(self, product: Product) -> None:
        pass

    def find_by_id(self, id: UUID) -> Product:
        pass
