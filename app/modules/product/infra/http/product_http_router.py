from flask import Blueprint
from modules.product.infra.factory.controller_factory import ProductControllerFactory


class ProductHttpRouter:
    ENDPOINT_PREFIX = '/api/products'

    def __init__(self, controller_factory: ProductControllerFactory):
        self.__controller_factory = controller_factory

    def create(self, bp: Blueprint):
        self.__create_product(bp)
        self.__delete_product(bp)
        self.__update_product(bp)
        self.__list_all_products(bp)
        self.__find_product_by_id(bp)

    def __create_product(self, bp: Blueprint):
        bp.add_url_rule(
            f'{self.ENDPOINT_PREFIX}/create',
            view_func=self.__controller_factory.create_create_product().handle,
            methods=['POST'],
            endpoint='create_product'
        )

    def __delete_product(self, bp: Blueprint):
        bp.add_url_rule(
            f'{self.ENDPOINT_PREFIX}/delete/<string:id>',
            view_func=self.__controller_factory.create_delete_product().handle,
            methods=['DELETE'],
            endpoint='delete_product'
        )

    def __update_product(self, bp: Blueprint):
        bp.add_url_rule(
            f'{self.ENDPOINT_PREFIX}/update/<string:id>',
            view_func=self.__controller_factory.create_update_product().handle,
            methods=['PUT'],
            endpoint='update_product'
        )

    def __list_all_products(self, bp: Blueprint):
        bp.add_url_rule(
            f'{self.ENDPOINT_PREFIX}/list',
            view_func=self.__controller_factory.create_list_all_products().handle,
            methods=['GET'],
            endpoint='list_all_products'
        )

    def __find_product_by_id(self, bp: Blueprint):
        bp.add_url_rule(
            f'{self.ENDPOINT_PREFIX}/<string:id>',
            view_func=self.__controller_factory.create_find_product_by_id().handle,
            methods=['GET'],
            endpoint='find_product_by_id'
        )
