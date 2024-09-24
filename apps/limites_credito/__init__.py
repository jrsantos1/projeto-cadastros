from flask import Blueprint
from server import app, db

limites_credito_routes = Blueprint('limite_credito', __name__, url_prefix='/limites_credito')

@limites_credito_routes.route('/', methods=['GET'])
def home_limites_credito():
    return {
        'message': 'Olá, mundo!'
    }
