from models.cadastro import Emissor

def get_all_emissores():
    return Emissor.query.all()