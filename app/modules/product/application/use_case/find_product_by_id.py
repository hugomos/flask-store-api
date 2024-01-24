from uuid import UUID
from typing import TypeVar

from domain.use_case import UseCase
from modules.product.application.repository.product_repository import ProductRepository

Input = TypeVar("Input")


class FindProductById(UseCase):
    def __init__(self, product_repository: ProductRepository):
        UseCase.__init__(self)
        self.__product_repository = product_repository

    def execute(self, input: Input):
        id = input.get('id', None)
        uuid = UUID(id)

        product = self.__product_repository.find_by_id(uuid)

        if not product:
            raise Exception(f'product with id {id} not found')

        return {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description
        }
