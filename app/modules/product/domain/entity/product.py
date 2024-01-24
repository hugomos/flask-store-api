import uuid
from infra.database.sql_alchemy import db
from sqlalchemy.dialects.postgresql import UUID


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(UUID(as_uuid=True), primary_key=True,
                   default=uuid.uuid4, unique=True, nullable=False)

    name = db.Column(db.String(80), nullable=False)

    description = db.Column(db.Text)

    __price = db.Column('price', db.Integer, nullable=False)

    @property
    def price(self):
        return self.__price / 100.0

    @price.setter
    def price(self, value):
        self.__price = int(value * 100)
