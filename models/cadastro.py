from server import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    def check_password(self, password):
        return self.password_hash == password

class Emissor(db.Model):
    cnpj = db.Column(db.String(14), primary_key=True)
    instituicao_garantia_cnpj = db.Column(db.String(14), db.ForeignKey('emissor.cnpj'), nullable=True)
    rating = db.Column(db.String(50), nullable=False)
    emissor = db.Column(db.String(50), nullable=False)
    analista = db.Column(db.String(50), nullable=False)
    setor = db.Column(db.String(50), nullable=False)
    grupo = db.Column(db.String(50), nullable=False)
    mesa_gestao = db.Column(db.String(50), nullable=False)
    data_atualizacao = db.Column(db.DateTime, nullable=False)

class Estruturados(db.Model):
    ticker = db.Column(db.String(10), primary_key=True, nullable=False)
    classe = db.Column(db.String(10), nullable=False)
    cnpj = db.Column(db.String(14), db.ForeignKey('emissor.cnpj'), nullable=False)
    indexador = db.Column(db.String(50), nullable=False)
    vencimento = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Float, nullable=False)

class EstruturadosEvento(db.Model):
    evento_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticker = db.Column(db.String(10), db.ForeignKey('estruturados.ticker'), nullable=False)
    rating = db.Column(db.String(50), nullable=False)
    data_aprovacao = db.Column(db.DateTime, nullable=False)
    data_vencimento = db.Column(db.DateTime, nullable=False)
    comite = db.Column(db.String(50), nullable=False)
    tipo_oferta = db.Column(db.String(50), nullable=False)
    ic_coordenador_lider = db.Column(db.Boolean, nullable=False)
    coordenador_unico = db.Column(db.String(50), nullable=False)
    descricao_evento = db.Column(db.String(50), nullable=False)
    link_ata = db.Column(db.String(50), nullable=False)
    status_esg = db.Column(db.String(50), nullable=False)
    classificacao_esg = db.Column(db.String(50), nullable=False)
    detalhamento = db.Column(db.String(100), nullable=False) 

class EventoEmissor(db.Model):
    evento_id = db.Column(db.Integer,  primary_key=True, autoincrement=True)
    descricao_evento = db.Column(db.String(50), nullable=False)
    cnpj = db.Column(db.String(14), db.ForeignKey('emissor.cnpj'), nullable=False)
    rating = db.Column(db.String(50), nullable=False)
    data_aprovacao = db.Column(db.DateTime, nullable=False)
    data_vencimento = db.Column(db.DateTime, nullable=False)
    tipo_comite = db.Column(db.String(50), nullable=False)
    tipo_oferta = db.Column(db.String(50), nullable=False)
    coordenador_unico = db.Column(db.String(50), nullable=False)
    coordenador_lider = db.Column(db.String(50), nullable=False)
    vl_percentual_divida = db.Column(db.Float, nullable=False)
    status_esg = db.Column(db.String(50), nullable=False)
    classificacao_esg = db.Column(db.String(50), nullable=False)
    detalhamento = db.Column(db.String(100), nullable=False) 
    
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Limite():
    id_limite = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cd_issuer = db.Column(db.String(50), nullable=False)
    cnpj = db.Column(db.String(14), db.ForeignKey('emissor.cnpj'), nullable=False)
    nivel_controle = db.Column(db.String(50), nullable=False)
    vl_prazo = db.Column(db.Float, nullable=False)
    cd_mesa = db.Column(db.String(50), nullable=False)
    vl_terceiros = db.Column(db.Float, nullable=False)
    vl_reserva_tecnica = db.Column(db.Float, nullable=False)
    data_aprovacao = db.Column(db.DateTime, nullable=False)
    data_vencimento = db.Column(db.DateTime, nullable=False)
    ic_caracteristica_holding = db.Column(db.Boolean, nullable=False)   
    ic_run_off = db.Column(db.Boolean, nullable=False)