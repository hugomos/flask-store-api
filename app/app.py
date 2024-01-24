import os

from flask import Flask, Blueprint
from flask_cors import CORS
from flask_migrate import Migrate

from infra.database.sql_alchemy import db
from infra.utils.navigate_up import navigate_up

from main.config.development import DevelopmentConfig
from modules.product.main_api import ProductMain

basedir = navigate_up(__file__, 2)

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

CORS(app, resources={r"/api/*": {"origins": "*"}})

db.init_app(app)
migrate = Migrate(app, db, directory=os.path.join(basedir, 'migrations'))


bp = ProductMain(orm=db).register()
app.register_blueprint(bp)

# Lista as rotas da API
print('\nRotas da API:')
for rule in app.url_map.iter_rules():
    if rule.rule.startswith('/api'):
        methods = ', '.join([str(x) for x in rule.methods if x in [
                            'GET', 'POST', 'PUT', 'DELETE']])
        print(f'{methods} -> {rule.rule}')
print('\n')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
