from flask_sqlalchemy import SQLAlchemy

from modules.product.application.factory.database_factory import DatabaseFactory

from modules.product.application.repository.product_repository import ProductRepository
from modules.product.infra.database.product_dao_database import ProductDAODatabase
from modules.product.infra.database.product_repository_database import ProductRepositoryDatabase


class ProductDatabaseFactory(DatabaseFactory):

    def __init__(self, orm: SQLAlchemy) -> None:
        self.orm = orm

    def create_dao(self) -> ProductDAODatabase:
        return ProductDAODatabase(orm=self.orm)

    def create_repository(self) -> ProductRepository:
        return ProductRepositoryDatabase(orm=self.orm)
