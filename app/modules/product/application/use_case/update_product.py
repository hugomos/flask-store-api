from uuid import UUID
from typing import TypeVar

from domain.use_case import UseCase
from modules.product.domain.value_object.product_name import ProductName
from modules.product.domain.value_object.product_price import ProductPrice
from modules.product.application.repository.product_repository import ProductRepository
from modules.product.application.dao.product_dao import ProductDAO


Input = TypeVar("Input")


class UpdateProduct(UseCase):
    def __init__(self, product_repository: ProductRepository):
        UseCase.__init__(self)
        self.__product_repository = product_repository

    def execute(self, input: Input):
        id = input.get('id', None)
        uuid = UUID(id)

        product = self.__product_repository.find_by_id(uuid)

        if not product:
            raise Exception(f'product with id {id} not found')

        name = input.get('name', None)
        price = input.get('price', None)
        description = input.get('description', None)

        if not (name or price or description):
            raise Exception(
                'at least one of the fields is required to update a product')

        if name:
            product.name = ProductName.create(name).value

        if price:
            product.price = ProductPrice.create(price).value

        if description:
            product.description = description

        self.__product_repository.save(product)
