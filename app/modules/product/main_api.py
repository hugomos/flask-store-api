from flask import Blueprint, Flask
from flask_sqlalchemy import SQLAlchemy

from modules.product.infra.factory.controller_factory import ProductControllerFactory
from modules.product.infra.factory.database_factory import ProductDatabaseFactory
from modules.product.infra.factory.use_case_factory import ProductUseCaseFactory

from modules.product.infra.http.product_http_router import ProductHttpRouter


class ProductMain:
    def __init__(self, orm: SQLAlchemy):
        self.orm = orm

    def register(self):
        bp = Blueprint('product', __name__)

        self.database_factory = ProductDatabaseFactory(self.orm)
        self.use_case_factory = ProductUseCaseFactory(self.database_factory)
        self.controller_factory = ProductControllerFactory(
            self.use_case_factory
        )
        self.router = ProductHttpRouter(self.controller_factory)
        self.router.create(bp)

        return bp
