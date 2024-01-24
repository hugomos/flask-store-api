from flask import request
from typing import TypeVar

from domain.use_case import UseCase
from modules.product.domain.entity.product import Product
from modules.product.domain.value_object.product_name import ProductName
from modules.product.domain.value_object.product_price import ProductPrice
from modules.product.application.repository.product_repository import ProductRepository


Input = TypeVar("Input")


class CreateProduct(UseCase):
    def __init__(self, product_repository: ProductRepository):
        UseCase.__init__(self)
        self.__product_repository = product_repository

    def execute(self, input: Input) -> None:
        name = input.get('name', None)
        price = input.get('price', None)
        description = input.get('description', None)

        if not (name and price):
            raise Exception('name and price are required')

        product_name = ProductName.create(name).value
        product_price = ProductPrice.create(price).value

        product = Product(
            name=product_name, description=description, price=product_price)

        self.__product_repository.save(product)
