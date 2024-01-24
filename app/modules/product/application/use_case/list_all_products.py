from typing import TypeVar, Optional

from domain.use_case import UseCase
from modules.product.application.dao.product_dao import ProductDAO


Input = TypeVar("Input")


class ListAllProducts(UseCase):
    def __init__(self, product_dao: ProductDAO):
        self.__product_dao = product_dao

    def execute(self, input: Optional[Input] = None):
        return self.__product_dao.find_many()
