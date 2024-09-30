from server import db
from datetime import datetime
from sqlalchemy import Integer, DOUBLE
from flask_login import UserMixin

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     password_hash = db.Column(db.String(150), nullable=False)
#     def check_password(self, password):
#         return self.password_hash == password

class Base():
    def update_from_form(self, form):
        campos = list(self.__dict__.keys())[1:]
        if 'data_atualizacao' in campos:
            campos.remove('data_atualizacao')
            self.data_atualizacao = datetime.now()
        for campo in campos:
            setattr(self, campo, getattr(form, campo).data)
class Emissor(db.Model, Base):
    cnpj = db.Column(db.Integer, primary_key=True, unique=True)
    instituicao_garantia_cnpj = db.Column(db.Integer, db.ForeignKey('emissor.cnpj'))
    cd_issuer = db.Column(db.String(50), nullable=False)
    ic_garantia_aval = db.Column(db.Boolean, nullable=False)
    rating = db.Column(db.String(50))
    emissor = db.Column(db.String(50))
    analista = db.Column(db.String(50))
    setor = db.Column(db.String(50), nullable=False)
    grupo = db.Column(db.String(50), nullable=False)
    mesa_gestao = db.Column(db.String(50))
    data_atualizacao = db.Column(db.DateTime, nullable=False)

class Ativo(db.Model, Base):
    ticker = db.Column(db.String(10), primary_key=True, nullable=False, unique=True)
    rating = db.Column(db.String(50))
    classe = db.Column(db.String(10), nullable=False)
    cnpj = db.Column(db.Integer, db.ForeignKey('emissor.cnpj'), nullable=False)
    indexador = db.Column(db.String(50))
    data_vencimento = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Float)

class AtivoEvento(db.Model, Base):
    evento_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticker = db.Column(db.String(10), db.ForeignKey('ativo.ticker'), nullable=False)
    rating = db.Column(db.String(50), nullable=False)
    data_aprovacao = db.Column(db.DateTime, nullable=False)
    data_vencimento = db.Column(db.DateTime, nullable=False)
    comite = db.Column(db.String(50), nullable=False)
    tipo_oferta = db.Column(db.String(50))
    ic_coordenador_unico = db.Column(db.Boolean)
    coordenador_lider = db.Column(db.String(50))
    descricao_evento = db.Column(db.String(50))
    link_ata = db.Column(db.String(50))
    cd_status_esg = db.Column(db.String(50), nullable=False)
    cd_classificacao_esg = db.Column(db.String(50))
    detalhamento_evento = db.Column(db.String(100)) 

class EventoEmissor(db.Model, Base):
    evento_id = db.Column(db.Integer,  primary_key=True, autoincrement=True)
    descricao_evento = db.Column(db.String(50), nullable=False)
    cnpj = db.Column(db.Integer, db.ForeignKey('emissor.cnpj'), nullable=False)
    rating = db.Column(db.String(50), nullable=False)
    data_aprovacao = db.Column(db.DateTime, nullable=False)
    data_vencimento = db.Column(db.DateTime, nullable=False)
    tipo_comite = db.Column(db.String(50), nullable=False)
    tipo_oferta = db.Column(db.String(50), nullable=False)
    ic_coordenador_unico = db.Column(db.Boolean)
    coordenador_lider = db.Column(db.String(50))
    vl_percentual_divida = db.Column(db.Float, nullable=False)
    vl_percentual_divida_pl = db.Column(db.Float, nullable=False)
    cd_status_esg = db.Column(db.String(50), nullable=False)
    cd_classificacao_esg = db.Column(db.String(50), nullable=False)
    detalhamento_evento = db.Column(db.String(100), nullable=False)
    link_ata = db.Column(db.String(400))

class Limite(db.Model, Base):
    limite_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cd_issuer = db.Column(db.String(50), nullable=False)
    cnpj = db.Column(db.Integer, db.ForeignKey('emissor.cnpj'), nullable=False)
    nivel_controle = db.Column(db.String(50), nullable=False)
    vl_prazo = db.Column(db.Float, nullable=False)
    cd_mesa = db.Column(db.String(50), nullable=False)
    vl_terceiros = db.Column(db.Float, nullable=False)
    vl_reserva_tecnica = db.Column(db.Float, nullable=False)
    data_aprovacao = db.Column(db.DateTime, nullable=False)
    data_vencimento = db.Column(db.DateTime, nullable=False)
    ic_caracteristica_holding = db.Column(db.Boolean, nullable=False)   
    ic_run_off = db.Column(db.Boolean, nullable=False)