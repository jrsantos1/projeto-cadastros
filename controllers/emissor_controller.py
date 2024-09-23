from config import app, db
from models.cadastro import Emissor
from flask import request, redirect, url_for, render_template
import datetime

@app.route('/editar_emissor/<cnpj>', methods=['GET', 'POST'])
def editar_emissor(cnpj):
    emissor = Emissor.query.get_or_404(cnpj)

    if request.method == 'POST':
        emissor.instituicao_garantia_cnpj = request.form['instituicao_garantia_cnpj']
        emissor.rating = request.form['rating']
        emissor.emissor = request.form['emissor']
        emissor.analista = request.form['analista']
        emissor.setor = request.form['setor']
        emissor.grupo = request.form['grupo']
        emissor.mesaGestao = request.form['mesaGestao']
        emissor.dtAtualizacao = datetime.now()

        db.session.commit()
        return redirect(url_for('listar_emissores'))
    
    return render_template('editar_emissor.html', emissor=emissor)

@app.route('/excluir_emissor/<cnpj>', methods=['POST'])
def excluir_emissor(cnpj):
    emissor = Emissor.query.get_or_404(cnpj)
    db.session.delete(emissor)
    db.session.commit()
    return redirect(url_for('listar_emissores'))

@app.route('/limites_credito/emissores')
def listar_emissores():
    emissores = Emissor.query.all()
    return render_template('emissor/listar_emissores.html', emissores=emissores)