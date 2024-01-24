from infra.http.http_controller import HttpController

from modules.product.infra.factory.use_case_factory import ProductUseCaseFactory
from modules.product.application.http_mapper.list_all_products import ListAllProductsHttpMapper


class ProductControllerFactory:
    def __init__(self, use_case_factory: ProductUseCaseFactory):
        self.__use_case_factory = use_case_factory

    def create_create_product(self) -> HttpController:
        return HttpController(
            use_case=self.__use_case_factory.create_create_product(),
            mapper=None
        )

    def create_delete_product(self) -> HttpController:
        return HttpController(
            use_case=self.__use_case_factory.create_delete_product(),
            mapper=None
        )

    def create_update_product(self) -> HttpController:
        return HttpController(
            use_case=self.__use_case_factory.create_update_product(),
            mapper=None
        )

    def create_list_all_products(self) -> HttpController:
        return HttpController(
            use_case=self.__use_case_factory.create_list_all_products(),
            mapper=ListAllProductsHttpMapper()
        )

    def create_find_product_by_id(self) -> HttpController:
        return HttpController(
            use_case=self.__use_case_factory.create_find_product_by_id(),
            mapper=None
        )
