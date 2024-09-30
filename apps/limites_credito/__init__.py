from flask import Blueprint
from server import app, db
from models.cadastro import Emissor, Ativo, AtivoEvento, EventoEmissor, Limite
from flask import request, redirect, url_for, render_template, flash
from datetime import datetime
from forms import EmissorForm, AtivoForm, AtivoEventoForm, EventoEmissorForm, LimiteForm

limites_credito_routes = Blueprint('limite_credito', __name__, url_prefix='/limites_credito')

@limites_credito_routes.route('/emissores')
def listar_emissores():
    emissores = Emissor.query.all()
    return render_template('limites_credito/listar_emissores.html', emissores=emissores)

@limites_credito_routes.route('/editar_emissor/<cnpj>', methods=['GET', 'POST'])
def editar_emissor(cnpj):
    emissor = Emissor.query.get_or_404(cnpj)
    form = EmissorForm(obj=emissor)
    return render_template('limites_credito/cadastrar_emissor.html', form=form)

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

@limites_credito_routes.route('/formulario_cadastrar_emissor', methods=['GET'])
def formulario_cadastrar_emissor():
    form = EmissorForm()
    return render_template('limites_credito/cadastrar_emissor.html', form=form)

@limites_credito_routes.route('/cadastrar_emissor', methods=['GET', 'POST'])
def cadastrar_emissor():
    form = EmissorForm()
    if form.validate_on_submit():
        emissor = Emissor.query.get(form.cnpj.data)
        if emissor:
            emissor.update_from_form(form=form)
            flash('Emissor atualizado com sucesso!', 'success')
        else:
            novo_emissor = Emissor(
                cnpj=form.cnpj.data,
                instituicao_garantia_cnpj=form.instituicao_garantia_cnpj.data,
                ic_garantia_aval=form.ic_garantia_aval.data,
                cd_issuer=form.cd_issuer.data,
                rating=form.rating.data,
                emissor=form.emissor.data,
                analista=form.analista.data,
                setor=form.setor.data,
                grupo=form.grupo.data,
                mesa_gestao=form.mesa_gestao.data,
                data_atualizacao=datetime.now()
            )
            db.session.add(novo_emissor)
            flash('Emissor cadastrado com sucesso!', 'success')
        db.session.commit()
        return redirect(url_for('limite_credito.listar_emissores'))  # 'listar_emissores' seria outra rota onde você lista os emissores cadastrados
    return render_template('limites_credito/cadastrar_emissor.html', form=form)

## ------------------------------------------- ativos -----------------------------------------

@limites_credito_routes.route('/cadastrar_ativo', methods=['GET', 'POST'])
def cadastrar_ativo():
    form = AtivoForm()
    if request.method == 'GET':
        return render_template('limites_credito/cadastrar_ativo.html', form=form)
    else:
        if form.validate_on_submit():
            novo_ativo = Ativo(
                ticker=form.ticker.data,
                classe=form.classe.data,
                rating=form.rating.data,
                cnpj=form.cnpj.data,
                indexador=form.indexador.data,
                data_vencimento=form.data_vencimento.data,
                duration=form.duration.data
            )
            db.session.add(novo_ativo)
            db.session.commit()
            flash('Ativo cadastrado com sucesso!', 'success')
            return redirect(url_for('limite_credito.listar_ativos'))
    return render_template('limites_credito/cadastrar_ativo.html', form=form)

@limites_credito_routes.route('/listar_ativos')
def listar_ativos():
    ativos = Ativo.query.all()
    return render_template('limites_credito/listar_ativos.html', ativos=ativos)

@limites_credito_routes.route('/formulario_atualizar_ativo/<ticker>', methods=['GET', 'POST'])
def formulario_atualizar_ativo(ticker):
    ativo = Ativo.query.get_or_404(ticker)
    form = AtivoForm(obj=ativo)
    return render_template('limites_credito/atualizar_ativo.html', form=form)

@limites_credito_routes.route('/atualizar_ativo/<ticker>', methods=['GET', 'POST'])
def atualizar_ativo(ticker):
    ativo = Ativo.query.get_or_404(ticker)
    form = AtivoForm(obj=ativo)
    ativo.update_from_form(form)
    if form.validate_on_submit():
        db.session.commit()
        flash('Ativo atualizado com sucesso!', 'success')
        return redirect(url_for('limite_credito.listar_ativos'))
    return render_template('limites_credito/atualizar_ativo.html', form=form)

@limites_credito_routes.route('/excluir_estruturados/<ticker>', methods=['POST'])
def excluir_ativo(ticker):
    ativo = Ativo.query.get_or_404(ticker)
    db.session.delete(ativo)
    db.session.commit()
    flash('Ativo excluído com sucesso!', 'success')
    return redirect(url_for('limite_credito.listar_ativos'))

#------------------ Estruturados evento -------------------------- #
@limites_credito_routes.route('/listar_ativos_eventos')
def listar_ativos_eventos():
    eventos = AtivoEvento.query.all()
    return render_template('limites_credito/listar_ativos_eventos.html', eventos=eventos)

@limites_credito_routes.route('/cadastrar_ativo_evento', methods=['GET', 'POST'])
def cadastrar_ativo_evento():
    form = AtivoEventoForm()
    if form.validate_on_submit():
        novo_evento = AtivoEvento(
            ticker=form.ticker.data,
            rating=form.rating.data,
            data_aprovacao=form.data_aprovacao.data,
            data_vencimento=form.data_vencimento.data,
            comite=form.comite.data,
            tipo_oferta=form.tipo_oferta.data,
            coordenador_lider=form.coordenador_lider.data,
            ic_coordenador_unico=form.ic_coordenador_unico.data,
            descricao_evento=form.descricao_evento.data,
            link_ata=form.link_ata.data,
            cd_status_esg=form.cd_status_esg.data,
            cd_classificacao_esg=form.cd_classificacao_esg.data,
            detalhamento_evento=form.detalhamento_evento.data
        )
        db.session.add(novo_evento)
        db.session.commit()
        flash('Evento ativo cadastrado com sucesso!', 'success')
        return redirect(url_for('limite_credito.listar_ativos_eventos'))  # Altere para sua rota de listagem
    return render_template('limites_credito/cadastrar_ativo_evento.html', form=form)

@limites_credito_routes.route('/formulario_atualizar_estruturados_evento/<int:evento_id>', methods=['GET', 'POST'])
def formulario_atualizar_ativo_evento(evento_id):
    ativo_evento = AtivoEvento.query.get_or_404(evento_id)
    form = AtivoEventoForm(obj=ativo_evento)
    return render_template('limites_credito/atualizar_ativo_evento.html', form=form)

@limites_credito_routes.route('/atualizar_estruturados_evento/<int:evento_id>', methods=['GET', 'POST'])
def atualizar_ativo_evento(evento_id):
    ativo_evento = AtivoEvento.query.get_or_404(evento_id)
    form = AtivoEventoForm(obj=ativo_evento)
    ativo_evento.update_from_form(form)
    if form.validate_on_submit():
        db.session.commit()
        flash('Evento ativo atualizado com sucesso!', 'success')
        return redirect(url_for('limite_credito.listar_ativos_eventos'))  # Altere para sua rota de listagem
    return render_template('limites_credito/atualizar_ativo_evento.html', form=form)

@limites_credito_routes.route('/excluir_ativo_evento/<int:evento_id>', methods=['POST'])
def excluir_ativo_evento(evento_id):
    evento = AtivoEvento.query.get_or_404(evento_id)
    db.session.delete(evento)
    db.session.commit()
    flash('Evento estruturado excluído com sucesso!', 'success')
    return redirect(url_for('limite_credito.listar_estruturados_eventos'))  # Altere para sua rota de listagem

## ------------------------------------------- evento emissor -----------------------------------------


@limites_credito_routes.route('/emissor/eventos')
def listar_emissor_eventos():
    eventos = EventoEmissor.query.all()
    return render_template('limites_credito/listar_emissor_eventos.html', eventos=eventos)

@limites_credito_routes.route('/emissor/novo', methods=['GET', 'POST'])
def cadastrar_emissor_evento():
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
            coordenador_lider=form.coordenador_lider.data,
            ic_coordenador_unico=form.ic_coordenador_unico.data,
            vl_percentual_divida=form.vl_percentual_divida.data,
            vl_percentual_divida_pl=form.vl_percentual_divida_pl.data,
            cd_status_esg=form.cd_status_esg.data,
            cd_classificacao_esg=form.cd_classificacao_esg.data,
            detalhamento_evento=form.detalhamento_evento.data,
            link_ata=form.link_ata.data
        )
        db.session.add(novo_evento)
        db.session.commit()
        flash('Evento criado com sucesso!')
        return redirect(url_for('limite_credito.listar_emissor_eventos'))
    return render_template('limites_credito/cadastrar_emissor_evento.html', form=form)

@limites_credito_routes.route('/emissor/evento/novo/<int:evento_id>/editar', methods=['GET', 'POST'])
def formulario_atualizar_emissor_evento(evento_id):
    evento = EventoEmissor.query.get_or_404(evento_id)
    form = EventoEmissorForm(obj=evento)
    return render_template('limites_credito/atualizar_emissor_evento.html', form=form)

@limites_credito_routes.route('/emissor/evento/atualizar/<int:evento_id>/editar', methods=['GET', 'POST'])
def atualizar_emissor_evento(evento_id):
    evento = EventoEmissor.query.get_or_404(evento_id)
    form = EventoEmissorForm(obj=evento)
    evento.update_from_form(form)
    if form.validate_on_submit():
        db.session.commit()
        flash('Evento atualizado com sucesso!')
        return redirect(url_for('limite_credito.listar_emissor_eventos'))
    return render_template('limites_credito/editar_evento.html', form=form)

@limites_credito_routes.route('/limites_credito/<int:evento_id>/deletar', methods=['POST'])
def deletar_evento(evento_id):
    evento = EventoEmissor.query.get_or_404(evento_id)
    db.session.delete(evento)
    db.session.commit()
    flash('Evento deletado com sucesso!')
    return redirect(url_for('limites_credito.listar_emissor_eventos'))

#------------------------------- limites ---------------------------------------

@limites_credito_routes.route('/limites', methods=['GET'])
def listar_limites():
    limites = Limite.query.all()
    return render_template('limites_credito/listar_limites.html', limites=limites)

@limites_credito_routes.route('/limites/novo', methods=['GET', 'POST'])
def cadastrar_limite():
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
        return redirect(url_for('limite_credito.listar_limites'))
    return render_template('limites_credito/cadastrar_limite.html', form=form)

@limites_credito_routes.route('limites/formulario_atualizar/<int:limite_id>')
def formulario_atualizar_limite(limite_id):
    limite = Limite.query.get_or_404(limite_id)
    form = LimiteForm(obj=limite)
    return render_template('limites_credito/atualizar_limite.html', form=form)
@limites_credito_routes.route('/limites/<int:limite_id>/editar', methods=['GET', 'POST'])
def atualizar_limite(limite_id):
    limite = Limite.query.get_or_404(limite_id)
    form = LimiteForm(obj=limite)
    if form.validate_on_submit():
        form.populate_obj(limite)
        db.session.commit()
        flash('Limite atualizado com sucesso!')
        return redirect(url_for('limite_credito.listar_limites'))
    return render_template('limites_credito/atualizar_limite.html', form=form)

@limites_credito_routes.route('/limites/<int:limite_id>/deletar', methods=['POST'])
def excluir_limite(limite_id):
    limite = Limite.query.get_or_404(limite_id)
    db.session.delete(limite)
    db.session.commit()
    flash('Limite deletado com sucesso!')
    return redirect(url_for('limites_credito.listar_limites'))