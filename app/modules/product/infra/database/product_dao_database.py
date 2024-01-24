from uuid import UUID
from flask_sqlalchemy import SQLAlchemy

from modules.product.domain.entity.product import Product
from modules.product.application.dao.product_dao import ProductDAO, ProductRaw


class ProductDAODatabase(ProductDAO):
    def __init__(self, orm: SQLAlchemy):
        self.orm = orm

    def exists_by_id(self, id: UUID) -> bool:
        product = self.orm.session.query(Product).get(id)
        return product is not None

    def find_many(self) -> list[ProductRaw]:
        products = self.orm.session.query(Product).all()
        return [
            ProductRaw(product.id, product.name, product.description, product.price) for product in products
        ]
