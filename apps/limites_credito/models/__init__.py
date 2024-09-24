from flask import Blueprint

limites_credito_routes = Blueprint('limites_credito', __name__)

@limites_credito_routes.route('/')
def editar_emissor(cnpj):
    ...

@limites_credito_routes.route('/limites_credito')
def home_limites_credito():
    ...

