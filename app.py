from flask import render_template
from config import app, db

@app.route('/')
def listar_emissores():
    return render_template('emissor/listar_emissores.html')

@app.route('/cadastrar_emissor')
def cadastrar_emissor():
    return render_template('cadastro.html')

if __name__ == '__main__':
    # Cria as tabelas antes de rodar o servidor
    with app.app_context():
        db.create_all()
    app.run(debug=True)
