from uuid import UUID

from infra.database.sql_alchemy import db
from flask import Blueprint, jsonify, request

from modules.product.application.use_case.create_product import CreateProduct
from app.modules.product.infra.database.product_repository_database import ProductRepositoryDatabase

product_bp = Blueprint('product', __name__, url_prefix='/api/products')

product_repository = ProductRepositoryDatabase(db=db)

product_bp.add_url_rule(
    '/api/products/create', view_func=CreateProduct, methods=['POST'])


@product_bp.route('/create', methods=['POST'])
def create_product():
    try:
        create_product_use_case = CreateProduct(product_repository)

        data = request.get_json()

        name = data.get('name', None)
        price = data.get('price', None)
        description = data.get('description', None)

        if not (name and price):
            return jsonify({'error': 'name and price are required'}), 400

        response = create_product_use_case.perform(
            {"name": name, "price": price, "description": description})

        if response.is_left():
            return jsonify({'error': str(response.value)}), 500

        return jsonify(None), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@product_bp.route('/<string:id>', methods=['GET'])
def get_product_by_id(id):
    id = UUID(id)
    product = product_repository.find_by_id(id)

    if not product:
        return jsonify({'error': 'product not found'}), 404

    return jsonify({
        'name': product.name,
        'price': product.price,
        'description': product.description
    })


@product_bp.route('/', methods=['GET'])
def list_all_products():
    products = product_repository.find_many()
    return jsonify([{'id': product.id, 'name': product.name, 'price': product.price} for product in products])


@product_bp.route('/update/<string:id>', methods=['PUT'])
def update_product_by_id(id):
    id = UUID(id)
    product = product_repository.find_by_id(id)

    if not product:
        return jsonify({'error': 'product not found'}), 404

    data = request.get_json()

    name = data.get('name', None)
    price = data.get('price', None)
    description = data.get('description', None)

    product.name = name if name else product.name
    product.price = price if price else product.price
    product.description = description if description else product.description

    product_repository.save(product)
    return jsonify(None), 200


@product_bp.route('/delete/<string:id>', methods=['DELETE'])
def delete_product_by_id(id):
    id = UUID(id)
    product = product_repository.find_by_id(id)

    if not product:
        return jsonify({'error': 'product not found'}), 404

    product_repository.delete(product)

    return jsonify(None), 204
