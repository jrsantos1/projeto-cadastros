from flask import Blueprint
from server import app, db
from models.cadastro import Emissor, Estruturados, EstruturadosEvento, EventoEmissor, Limite
from flask import request, redirect, url_for, render_template, flash
import datetime
from forms import EmissorForm, EstruturadosForm, EstruturadosEventoForm, EventoEmissorForm, LimiteForm

limites_credito_routes = Blueprint('limite_credito', __name__, url_prefix='/limites_credito')


## ROTAS EMISSOR

@limites_credito_routes.route('/editar_emissor/<cnpj>', methods=['GET', 'POST'])
def editar_emissor(cnpj):
    emissor = Emissor.query.get_or_404(cnpj)

    if request.method == 'POST':
        emissor.instituicao_garantia_cnpj = request.form['instituicao_garantia_cnpj']
        emissor.rating = request.form['rating']
        emissor.emissor = request.form['emissor']
        emissor.analista = request.form['analista']
        emissor.setor = request.form['setor']
        emissor.grupo = request.form['grupo']
        emissor.mesa_gestao = request.form['mesaGestao']
        emissor.data_atualizacao = datetime.now()

        db.session.commit()
        return redirect(url_for('listar_emissores'))
    
    return render_template('limites_credito/editar_emissor.html', emissor=emissor)

@limites_credito_routes.route('/excluir_emissor/<cnpj>', methods=['POST'])
def excluir_emissor(cnpj):
    
    try:
        emissor = Emissor.query.get_or_404(cnpj)
        db.session.delete(emissor)
        db.session.commit()
    except Exception as e:
        # Enviar mensagem flash de erro
        flash(f'Erro ao excluir emissor {emissor.emissor} com CNPJ {cnpj}.', 'danger')
        return redirect(url_for('listar_emissores'))

    # Enviar mensagem flash de sucesso
    flash(f'Emissor {emissor.emissor} com CNPJ {cnpj} foi excluído com sucesso.', 'success')
    return redirect(url_for('listar_emissores'))

@limites_credito_routes.route('/emissores')
def listar_emissores():
    emissores = Emissor.query.all()
    return render_template('limites_credito/listar_emissores.html', emissores=emissores)

@limites_credito_routes.route('/formulario_cadastrar_emissor', methods=['GET'])
def formulario_cadastrar_emissor():
    form = EmissorForm()  # Cria uma instância do formulário vazio
    return render_template('limites_credito/cadastrar_emissor.html', form=form)

@limites_credito_routes.route('/test')
def test():
    return render_template('limites_credito/base_test.html')


@limites_credito_routes.route('/cadastrar_emissor', methods=['GET', 'POST'])
def cadastrar_emissor():
    form = EmissorForm()

    # Verifica se o formulário foi enviado e se os dados são válidos
    if form.validate_on_submit():
        # Cria uma instância do modelo Emissor com os dados do formulário
        novo_emissor = Emissor(
            cnpj=form.cnpj.data,
            instituicao_garantia_cnpj=form.instituicao_garantia_cnpj.data,
            rating=form.rating.data,
            emissor=form.emissor.data,
            analista=form.analista.data,
            setor=form.setor.data,
            grupo=form.grupo.data,
            mesa_gestao=form.mesa_gestao.data,
            data_atualizacao=datetime.datetime.now()
        )
        
        # Adiciona o novo emissor ao banco de dados
        db.session.add(novo_emissor)
        db.session.commit()
        
        # Envia uma mensagem de sucesso
        flash('Emissor cadastrado com sucesso!', 'success')
        
        # Redireciona para outra página (ajuste conforme necessário)
        return redirect(url_for('limite_credito.listar_emissores'))  # 'listar_emissores' seria outra rota onde você lista os emissores cadastrados

    # Renderiza o template HTML com o formulário
    return render_template('limites_credito/cadastrar_emissor.html', form=form)

## ------------------------------------------- estruturados ----------------------------------------- 

@app.route('/cadastrar_estruturados', methods=['GET', 'POST'])
def cadastrar_estruturados():
    form = EstruturadosForm()
    if form.validate_on_submit():
        novo_estruturado = Estruturados(
            ticker=form.ticker.data,
            classe=form.classe.data,
            cnpj=form.cnpj.data,
            indexador=form.indexador.data,
            vencimento=form.vencimento.data,
            duration=form.duration.data
        )
        db.session.add(novo_estruturado)
        db.session.commit()
        flash('Estruturado cadastrado com sucesso!', 'success')
        return redirect(url_for('listar_estruturados'))
    return render_template('cadastrar_estruturados.html', form=form)

@app.route('/atualizar_estruturados/<ticker>', methods=['GET', 'POST'])
def atualizar_estruturados(ticker):
    estruturado = Estruturados.query.get_or_404(ticker)
    form = EstruturadosForm(obj=estruturado)
    if form.validate_on_submit():
        estruturado.classe = form.classe.data
        estruturado.cnpj = form.cnpj.data
        estruturado.indexador = form.indexador.data
        estruturado.vencimento = form.vencimento.data
        estruturado.duration = form.duration.data
        db.session.commit()
        flash('Estruturado atualizado com sucesso!', 'success')
        return redirect(url_for('listar_estruturados'))
    return render_template('limites_credito/atualizar_estruturados.html', form=form)

@app.route('/excluir_estruturados/<ticker>', methods=['POST'])
def excluir_estruturados(ticker):
    estruturado = Estruturados.query.get_or_404(ticker)
    db.session.delete(estruturado)
    db.session.commit()
    flash('Estruturado excluído com sucesso!', 'success')
    return redirect(url_for('listar_estruturados'))

@app.route('/listar_estruturados')
def listar_estruturados():
    estruturados = Estruturados.query.all()
    return render_template('listar_estruturados.html', estruturados=estruturados)

@limites_credito_routes.route('/cadastrar_estruturados_evento', methods=['GET', 'POST'])
def cadastrar_estruturados_evento():
    form = EstruturadosEventoForm()
    if form.validate_on_submit():
        novo_evento = EstruturadosEvento(
            ticker=form.ticker.data,
            rating=form.rating.data,
            data_aprovacao=form.data_aprovacao.data,
            data_vencimento=form.data_vencimento.data,
            comite=form.comite.data,
            tipo_oferta=form.tipo_oferta.data,
            ic_coordenador_lider=form.ic_coordenador_lider.data,
            coordenador_unico=form.coordenador_unico.data,
            descricao_evento=form.descricao_evento.data,
            link_ata=form.link_ata.data,
            status_esg=form.status_esg.data,
            classificacao_esg=form.classificacao_esg.data,
            detalhamento=form.detalhamento.data
        )
        db.session.add(novo_evento)
        db.session.commit()
        flash('Evento estruturado cadastrado com sucesso!', 'success')
        return redirect(url_for('limite_credito.listar_estruturados_eventos'))  # Altere para sua rota de listagem
    return render_template('limites_credito/cadastrar_estruturados_evento.html', form=form)

@limites_credito_routes.route('/atualizar_estruturados_evento/<int:evento_id>', methods=['GET', 'POST'])
def atualizar_estruturados_evento(evento_id):
    evento = EstruturadosEvento.query.get_or_404(evento_id)
    form = EstruturadosEventoForm(obj=evento)
    
    if form.validate_on_submit():
        evento.ticker = form.ticker.data
        evento.rating = form.rating.data
        evento.data_aprovacao = form.data_aprovacao.data
        evento.data_vencimento = form.data_vencimento.data
        evento.comite = form.comite.data
        evento.tipo_oferta = form.tipo_oferta.data
        evento.ic_coordenador_lider = form.ic_coordenador_lider.data
        evento.coordenador_unico = form.coordenador_unico.data
        evento.descricao_evento = form.descricao_evento.data
        evento.link_ata = form.link_ata.data
        evento.status_esg = form.status_esg.data
        evento.classificacao_esg = form.classificacao_esg.data
        evento.detalhamento = form.detalhamento.data
        
        db.session.commit()
        flash('Evento estruturado atualizado com sucesso!', 'success')
        return redirect(url_for('limite_credito.listar_estruturados_eventos'))  # Altere para sua rota de listagem
    
    return render_template('limites_credito/cadastrar_estruturados_evento.html', form=form)

@limites_credito_routes.route('/excluir_estruturados_evento/<int:evento_id>', methods=['POST'])
def excluir_estruturados_evento(evento_id):
    evento = EstruturadosEvento.query.get_or_404(evento_id)
    db.session.delete(evento)
    db.session.commit()
    flash('Evento estruturado excluído com sucesso!', 'success')
    return redirect(url_for('limite_credito.listar_estruturados_eventos'))  # Altere para sua rota de listagem

@limites_credito_routes.route('/listar_estruturados_eventos')
def listar_estruturados_eventos():
    eventos = EstruturadosEvento.query.all()
    return render_template('limites_credito/listar_estruturados_eventos.html', eventos=eventos)


## ------------------------------------------- evento emissor -----------------------------------------


@limites_credito_routes.route('/limites_credito/')
def listar_eventos():
    eventos = EventoEmissor.query.all()
    return render_template('limites_credito/listar_eventos.html', eventos=eventos)

@limites_credito_routes.route('/limites_credito/novo', methods=['GET', 'POST'])
def novo_evento():
    form = EventoEmissorForm()
    if form.validate_on_submit():
        novo_evento = EventoEmissor(
            descricao_evento=form.descricao_evento.data,
            cnpj=form.cnpj.data,
            rating=form.rating.data,
            data_aprovacao=form.data_aprovacao.data,
            data_vencimento=form.data_vencimento.data,
            tipo_comite=form.tipo_comite.data,
            tipo_oferta=form.tipo_oferta.data,
            coordenador_unico=form.coordenador_unico.data,
            coordenador_lider=form.coordenador_lider.data,
            vl_percentual_divida=form.vl_percentual_divida.data,
            status_esg=form.status_esg.data,
            classificacao_esg=form.classificacao_esg.data,
            detalhamento=form.detalhamento.data
        )
        db.session.add(novo_evento)
        db.session.commit()
        flash('Evento criado com sucesso!')
        return redirect(url_for('limites_credito.listar_eventos'))
    return render_template('limites_credito/novo_evento.html', form=form)

@limites_credito_routes.route('/limites_credito/<int:evento_id>/editar', methods=['GET', 'POST'])
def editar_evento(evento_id):
    evento = EventoEmissor.query.get_or_404(evento_id)
    form = EventoEmissorForm(obj=evento)
    if form.validate_on_submit():
        form.populate_obj(evento)
        db.session.commit()
        flash('Evento atualizado com sucesso!')
        return redirect(url_for('limites_credito.listar_eventos'))
    return render_template('limites_credito/editar_evento.html', form=form)

@limites_credito_routes.route('/limites_credito/<int:evento_id>/deletar', methods=['POST'])
def deletar_evento(evento_id):
    evento = EventoEmissor.query.get_or_404(evento_id)
    db.session.delete(evento)
    db.session.commit()
    flash('Evento deletado com sucesso!')
    return redirect(url_for('limites_credito.listar_eventos'))


@limites_credito_routes.route('/limites_credito/limites/')
def listar_limites():
    limites = Limite.query.all()
    return render_template('limites_credito/listar_limites.html', limites=limites)

@limites_credito_routes.route('/limites_credito/limites/novo', methods=['GET', 'POST'])
def novo_limite():
    form = LimiteForm()
    if form.validate_on_submit():
        novo_limite = Limite(
            cd_issuer=form.cd_issuer.data,
            cnpj=form.cnpj.data,
            nivel_controle=form.nivel_controle.data,
            vl_prazo=form.vl_prazo.data,
            cd_mesa=form.cd_mesa.data,
            vl_terceiros=form.vl_terceiros.data,
            vl_reserva_tecnica=form.vl_reserva_tecnica.data,
            data_aprovacao=form.data_aprovacao.data,
            data_vencimento=form.data_vencimento.data,
            ic_caracteristica_holding=form.ic_caracteristica_holding.data,
            ic_run_off=form.ic_run_off.data
        )
        db.session.add(novo_limite)
        db.session.commit()
        flash('Limite criado com sucesso!')
        return redirect(url_for('limites_credito.listar_limites'))
    return render_template('limites_credito/novo_limite.html', form=form)

@limites_credito_routes.route('/limites_credito/limites/<int:id_limite>/editar', methods=['GET', 'POST'])
def editar_limite(id_limite):
    limite = Limite.query.get_or_404(id_limite)
    form = LimiteForm(obj=limite)
    if form.validate_on_submit():
        form.populate_obj(limite)
        db.session.commit()
        flash('Limite atualizado com sucesso!')
        return redirect(url_for('limites_credito.listar_limites'))
    return render_template('limites_credito/editar_limite.html', form=form)

@limites_credito_routes.route('/limites_credito/limites/<int:id_limite>/deletar', methods=['POST'])
def deletar_limite(id_limite):
    limite = Limite.query.get_or_404(id_limite)
    db.session.delete(limite)
    db.session.commit()
    flash('Limite deletado com sucesso!')
    return redirect(url_for('limites_credito.listar_limites'))