from uuid import UUID
from flask_sqlalchemy import SQLAlchemy

from modules.product.domain.entity.product import Product
from modules.product.application.repository.product_repository import ProductRepository


class ProductRepositoryDatabase(ProductRepository):
    def __init__(self, orm: SQLAlchemy):
        self.orm = orm

    def save(self, product: Product) -> None:
        self.orm.session.add(product)
        self.orm.session.commit()

    def delete(self, product: Product) -> None:
        self.orm.session.delete(product)
        self.orm.session.commit()

    def find_by_id(self, id: UUID) -> Product:
        return self.orm.session.query(Product).get(id)
