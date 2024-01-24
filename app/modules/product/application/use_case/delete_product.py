from uuid import UUID
from typing import TypeVar

from domain.use_case import UseCase
from modules.product.application.dao.product_dao import ProductDAO
from modules.product.application.repository.product_repository import ProductRepository


Input = TypeVar("Input")


class DeleteProduct(UseCase):
    def __init__(self, product_repository: ProductRepository):
        UseCase.__init__(self)
        self.__product_repository = product_repository

    def execute(self, input: Input):
        id = input.get('id', None)
        uuid = UUID(id)

        product = self.__product_repository.find_by_id(uuid)

        if not product:
            raise Exception(f'product with id {id} not found')

        self.__product_repository.delete(product)
