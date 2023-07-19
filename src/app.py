from flask import Flask, jsonify, request
from flask_cors import CORS
from apis import routes
from config import config
from database.db import get_connection


app = Flask(__name__, static_folder='./client/dist/static', template_folder='./client/dist')
cors = CORS(app, resources={r"/*":{"origins": "*"}})

def pageNotFound(error):
    return '<h1>Page not found. 404.</h1>', 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_blueprint(routes.main, url_prefix='/')
    app.register_error_handler(404, pageNotFound)
    app.run()