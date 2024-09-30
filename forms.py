from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateTimeField, FloatField, BooleanField, TextAreaField, DateField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Regexp, Optional, NumberRange
from models.cadastro import Emissor
from server import app, db
def get_choices():
    try:
        with app.app_context():
            emissores = Emissor.query.all()
        return [(emissor.cnpj, emissor.emissor) for emissor in emissores]
    except: return []

class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')

class EmissorForm(FlaskForm):

    cnpj = IntegerField('CNPJ', validators=[
        DataRequired(message="O CNPJ é obrigatório."),
        NumberRange(min=0, max=99999999999999, message="O CNPJ deve conter até 14 dígitos.")
    ])

    instituicao_garantia_cnpj = SelectField('Instituição Garantia',
                                            validators=[
                                                Optional()
                                            ],
                                            choices=get_choices(),
                                            coerce=int)

    # instituicao_garantia_cnpj = StringField('Instituição Garantia CNPJ', validators=[
    #     Optional(),
    #     Length(min=0, max=14, message="O CNPJ deve ter ate 14 caracteres."),
    #     Regexp(r'^\d+$', message="O CNPJ deve conter apenas números.")
    # ])

    ic_garantia_aval = BooleanField('Contém Garantia')
    cd_issuer = StringField('Código do Issuer', validators=[DataRequired(message="O código do issuer é obrigatório.")])
    rating = StringField('Rating', validators=[DataRequired(message="O rating é obrigatório.")])
    emissor = StringField('Emissor', validators=[DataRequired(message="O emissor é obrigatório.")])
    analista = StringField('Analista', validators=[DataRequired(message="O analista é obrigatório.")])
    setor = StringField('Setor', validators=[DataRequired(message="O setor é obrigatório.")])
    grupo = StringField('Grupo', validators=[DataRequired(message="O grupo é obrigatório.")])
    mesa_gestao = StringField('Mesa de Gestão', validators=[DataRequired(message="A mesa de gestão é obrigatória.")])
    submit = SubmitField('Cadastrar Emissor')

class AtivoForm(FlaskForm):
    ticker = StringField('Ticker', validators=[DataRequired(), Length(max=10)])
    rating = StringField('Rating', validators=[Length(max=10)])
    classe = StringField('Classe', validators=[DataRequired(), Length(max=10)])
    cnpj = SelectField('Emissor',validators=[Optional()],
                                            choices=get_choices(),
                                            coerce=int)
    indexador = StringField('Indexador', validators=[DataRequired(), Length(max=50)])
    data_vencimento = DateTimeField('Vencimento', format='%Y-%m-%d', validators=[DataRequired()])
    duration = FloatField('Duration', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

class AtivoEventoForm(FlaskForm):
    evento_id = IntegerField(label='Evento ID')
    ticker = StringField('Ticker', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    data_aprovacao = DateTimeField('Data de Aprovação', format='%Y-%m-%d', validators=[DataRequired()])
    data_vencimento = DateTimeField('Data de Vencimento', format='%Y-%m-%d', validators=[DataRequired()])
    comite = StringField('Comitê', validators=[DataRequired()])
    tipo_oferta = StringField('Tipo de Oferta', validators=[DataRequired()])
    ic_coordenador_unico = BooleanField('Coordenador Único')
    coordenador_lider = StringField('Coordenador Líder')
    descricao_evento = StringField('Descrição do Evento', validators=[DataRequired()])
    link_ata = StringField('Link da Ata', validators=[DataRequired()])
    cd_status_esg = StringField('Status ESG', validators=[DataRequired()])
    cd_classificacao_esg = StringField('Classificação ESG', validators=[DataRequired()])
    detalhamento_evento = TextAreaField('Detalhamento')
    submit = SubmitField('Salvar')

class EventoEmissorForm(FlaskForm):
    evento_id = IntegerField(label='Evento ID')
    descricao_evento = StringField('Descrição do Evento', validators=[DataRequired()])
    cnpj = SelectField('Emissor', validators=[Optional()],
                       choices=get_choices(),
                       coerce=int)
    rating = StringField('Rating', validators=[DataRequired()])
    data_aprovacao = DateTimeField('Data de Aprovação', format='%Y-%m-%d', validators=[DataRequired()])
    data_vencimento = DateTimeField('Data de Vencimento', format='%Y-%m-%d', validators=[DataRequired()])
    tipo_comite = StringField('Tipo de Comitê', validators=[DataRequired()])
    tipo_oferta = StringField('Tipo de Oferta', validators=[DataRequired()])
    ic_coordenador_unico = BooleanField('Coordenador Único')
    coordenador_lider = StringField('Coordenador Líder')
    vl_percentual_divida = FloatField('Valor Percentual Dívida')
    vl_percentual_divida_pl = FloatField('Valor Percentual Dívida PL')
    cd_status_esg = StringField('Status ESG', validators=[DataRequired()])
    cd_classificacao_esg = StringField('Classificação ESG', validators=[DataRequired()])
    detalhamento_evento = TextAreaField('Detalhamento', validators=[DataRequired()])
    link_ata = TextAreaField('Link Ata')
    submit = SubmitField('Salvar')

class LimiteForm(FlaskForm):
    limite_id = IntegerField(label='Evento ID')
    cd_issuer = StringField('Código do Issuer', validators=[DataRequired()])
    cnpj = SelectField('Emissor', validators=[DataRequired()],
                       choices=get_choices(),
                       coerce=int)
    nivel_controle = StringField('Nível de Controle', validators=[DataRequired()])
    vl_prazo = FloatField('Valor Prazo', validators=[DataRequired()])
    cd_mesa = StringField('Código da Mesa', validators=[DataRequired()])
    vl_terceiros = FloatField('Valor Terceiros', validators=[DataRequired()])
    vl_reserva_tecnica = FloatField('Valor Reserva Técnica', validators=[DataRequired()])
    data_aprovacao = DateTimeField('Data de Aprovação', validators=[DataRequired()], format='%Y-%m-%d')
    data_vencimento = DateTimeField('Data de Vencimento', validators=[DataRequired()], format='%Y-%m-%d')
    ic_caracteristica_holding = BooleanField('Característica Holding')
    ic_run_off = BooleanField('Run-off')
    submit = SubmitField('Salvar')