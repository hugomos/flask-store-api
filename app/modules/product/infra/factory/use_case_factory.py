from modules.product.application.factory.database_factory import DatabaseFactory

from modules.product.application.use_case.create_product import CreateProduct
from modules.product.application.use_case.delete_product import DeleteProduct
from modules.product.application.use_case.update_product import UpdateProduct
from modules.product.application.use_case.find_product_by_id import FindProductById
from modules.product.application.use_case.list_all_products import ListAllProducts


class ProductUseCaseFactory:
    def __init__(self, database_factory: DatabaseFactory):
        self.__database_factory = database_factory

    def create_create_product(self) -> CreateProduct:
        return CreateProduct(self.__database_factory.create_repository())

    def create_delete_product(self) -> DeleteProduct:
        return DeleteProduct(self.__database_factory.create_repository())

    def create_update_product(self):
        return UpdateProduct(self.__database_factory.create_repository())

    def create_list_all_products(self):
        return ListAllProducts(self.__database_factory.create_dao())

    def create_find_product_by_id(self):
        return FindProductById(self.__database_factory.create_repository())
