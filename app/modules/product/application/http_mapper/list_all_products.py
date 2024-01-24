from typing import List

from infra.http.ports.http_mapper import HttpMapper
from modules.product.infra.database.product_dao_database import ProductRaw


class ListAllProductsHttpMapper(HttpMapper):
    def map(self, input: List[ProductRaw]) -> List[dict]:
        return [
            {
                'id': product.id,
                'name': product.name,
                'price': product.price
            } for product in input
        ]
