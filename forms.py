from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateTimeField, FloatField, BooleanField, TextAreaField, DateField
from wtforms.validators import DataRequired, Length, Regexp

class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')

class EmissorForm(FlaskForm):
    cnpj = StringField('CNPJ', validators=[
        DataRequired(message="O CNPJ é obrigatório."),
        Length(min=14, max=14, message="O CNPJ deve ter 14 caracteres."),
        Regexp(r'^\d{14}$', message="O CNPJ deve conter apenas números.")
    ])
    
    instituicao_garantia_cnpj = StringField('Instituição Garantia CNPJ', validators=[
        Length(min=14, max=14, message="O CNPJ deve ter 14 caracteres."),
        Regexp(r'^\d{14}$', message="O CNPJ deve conter apenas números.")
    ])
    
    rating = StringField('Rating', validators=[DataRequired(message="O rating é obrigatório.")])
    emissor = StringField('Emissor', validators=[DataRequired(message="O emissor é obrigatório.")])
    analista = StringField('Analista', validators=[DataRequired(message="O analista é obrigatório.")])
    setor = StringField('Setor', validators=[DataRequired(message="O setor é obrigatório.")])
    grupo = StringField('Grupo', validators=[DataRequired(message="O grupo é obrigatório.")])
    mesa_gestao = StringField('Mesa de Gestão', validators=[DataRequired(message="A mesa de gestão é obrigatória.")])
    submit = SubmitField('Cadastrar Emissor')

class EstruturadosForm(FlaskForm):
    ticker = StringField('Ticker', validators=[DataRequired(), Length(max=10)])
    classe = StringField('Classe', validators=[DataRequired(), Length(max=10)])
    cnpj = StringField('CNPJ', validators=[DataRequired(), Length(max=14)])
    indexador = StringField('Indexador', validators=[DataRequired(), Length(max=50)])
    vencimento = DateTimeField('Vencimento', format='%Y-%m-%d', validators=[DataRequired()])
    duration = FloatField('Duration', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

class EstruturadosEventoForm(FlaskForm):
    ticker = StringField('Ticker', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    data_aprovacao = DateTimeField('Data de Aprovação', format='%Y-%m-%d', validators=[DataRequired()])
    data_vencimento = DateTimeField('Data de Vencimento', format='%Y-%m-%d', validators=[DataRequired()])
    comite = StringField('Comitê', validators=[DataRequired()])
    tipo_oferta = StringField('Tipo de Oferta', validators=[DataRequired()])
    ic_coordenador_lider = BooleanField('Coordenador Líder')
    coordenador_unico = StringField('Coordenador Único', validators=[DataRequired()])
    descricao_evento = StringField('Descrição do Evento', validators=[DataRequired()])
    link_ata = StringField('Link da Ata', validators=[DataRequired()])
    status_esg = StringField('Status ESG', validators=[DataRequired()])
    classificacao_esg = StringField('Classificação ESG', validators=[DataRequired()])
    detalhamento = TextAreaField('Detalhamento', validators=[DataRequired()])
    submit = SubmitField('Salvar')

class EventoEmissorForm(FlaskForm):
    descricao_evento = StringField('Descrição do Evento', validators=[DataRequired()])
    cnpj = StringField('CNPJ', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    data_aprovacao = DateTimeField('Data de Aprovação', format='%Y-%m-%d', validators=[DataRequired()])
    data_vencimento = DateTimeField('Data de Vencimento', format='%Y-%m-%d', validators=[DataRequired()])
    tipo_comite = StringField('Tipo de Comitê', validators=[DataRequired()])
    tipo_oferta = StringField('Tipo de Oferta', validators=[DataRequired()])
    coordenador_unico = StringField('Coordenador Único', validators=[DataRequired()])
    coordenador_lider = StringField('Coordenador Líder', validators=[DataRequired()])
    vl_percentual_divida = StringField('Valor Percentual Dívida', validators=[DataRequired()])
    status_esg = StringField('Status ESG', validators=[DataRequired()])
    classificacao_esg = StringField('Classificação ESG', validators=[DataRequired()])
    detalhamento = TextAreaField('Detalhamento', validators=[DataRequired()])
    submit = SubmitField('Salvar')

class LimiteForm(FlaskForm):
    cd_issuer = StringField('Código do Issuer', validators=[DataRequired()])
    cnpj = StringField('CNPJ', validators=[DataRequired()])
    nivel_controle = StringField('Nível de Controle', validators=[DataRequired()])
    vl_prazo = FloatField('Valor Prazo', validators=[DataRequired()])
    cd_mesa = StringField('Código da Mesa', validators=[DataRequired()])
    vl_terceiros = FloatField('Valor Terceiros', validators=[DataRequired()])
    vl_reserva_tecnica = FloatField('Valor Reserva Técnica', validators=[DataRequired()])
    data_aprovacao = DateField('Data de Aprovação', validators=[DataRequired()], format='%Y-%m-%d')
    data_vencimento = DateField('Data de Vencimento', validators=[DataRequired()], format='%Y-%m-%d')
    ic_caracteristica_holding = BooleanField('Característica Holding')
    ic_run_off = BooleanField('Run-off')