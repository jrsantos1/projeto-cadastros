from flask import render_template
from server import app, db

from apps.limites_credito import  limites_credito_routes
app.register_blueprint(limites_credito_routes)

if __name__ == '__main__':
    # Cria as tabelas antes de rodar o servidor
    with app.app_context():
        db.create_all()
    app.run(debug=True)
