from abc import ABC, abstractmethod

from modules.product.application.dao.product_dao import ProductDAO
from modules.product.application.repository.product_repository import ProductRepository


class DatabaseFactory(ABC):

    @abstractmethod
    def create_dao(self) -> ProductDAO:
        pass

    @abstractmethod
    def create_repository(self) -> ProductRepository:
        pass
