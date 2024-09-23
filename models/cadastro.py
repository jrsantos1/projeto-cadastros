from config import db

class Emissor(db.Model):
    cnpj = db.Column(db.String(14), primary_key=True)
    instituicao_garantia_cnpj = db.Column(db.String(14), db.ForeignKey('emissor.cnpj'), nullable=True)
    rating = db.Column(db.String(50), nullable=False)
    emissor = db.Column(db.String(50), nullable=False)
    analista = db.Column(db.String(50), nullable=False)
    setor = db.Column(db.String(50), nullable=False)
    grupo = db.Column(db.String(50), nullable=False)
    mesaGestao = db.Column(db.String(50), nullable=False)
    dtAtualizacao = db.Column(db.DateTime, nullable=False)

class EventoEmissor(db.Model):
    eventoId = db.Column(db.Integer,  primary_key=True, autoincrement=True)
    descricaoEvento = db.Column(db.String(50), nullable=False)
    cnpj = db.Column(db.String(14), db.ForeignKey('emissor.cnpj'), nullable=False)
    rating = db.Column(db.String(50), nullable=False)
    dataAprovacao = db.Column(db.DateTime, nullable=False)
    dataVencimento = db.Column(db.DateTime, nullable=False)
    tipoComite = db.Column(db.String(50), nullable=False)
    tipoOferta = db.Column(db.String(50), nullable=False)
    coordenadorUnico = db.Column(db.String(50), nullable=False)
    coordenadorLider = db.Column(db.String(50), nullable=False)
    vlPercentualDivida = db.Column(db.Float, nullable=False)
    cdStatusESG = db.Column(db.String(50), nullable=False)
    cdClassificacaoESG = db.Column(db.String(50), nullable=False)
    dsOberservacao = db.Column(db.String(50), nullable=False)
    



class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Cadastro(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    estado_civil = db.Column(db.String(20), nullable=False)
    endereco = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    cep = db.Column(db.String(9), nullable=False)
    profissao = db.Column(db.String(50), nullable=False)
    empresa = db.Column(db.String(50), nullable=False)
    cargo = db.Column(db.String(50), nullable=False)
    salario = db.Column(db.Float, nullable=False)
    data_cadastro = db.Column(db.DateTime, nullable=False)