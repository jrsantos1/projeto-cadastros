import random
from datetime import datetime
from faker import Faker
from config import app, db
from models.cadastro import Emissor

# Inicializa o Faker para gerar dados aleatórios
fake = Faker()

# Exemplo de lista de ratings e setores para a geração de dados aleatórios
ratings = ['AAA', 'AA+', 'AA', 'A', 'BBB', 'BB', 'B']
setores = ['Financeiro', 'Industrial', 'Tecnologia', 'Saúde', 'Comércio']
grupos = ['Grupo A', 'Grupo B', 'Grupo C', 'Grupo D']
mesas = ['Mesa 1', 'Mesa 2', 'Mesa 3', 'Mesa 4']

# Função para gerar um CNPJ aleatório
def gerar_cnpj():
    return ''.join([str(random.randint(0, 9)) for _ in range(14)])

# Inserindo dados aleatórios
with app.app_context():
    # Criando 5 emissores aleatórios
    for _ in range(5):
        cnpj = gerar_cnpj()
        emissor = Emissor(
            cnpj=cnpj,
            instituicao_garantia_cnpj=None,  # Podemos adicionar isso depois, se for necessário
            rating=random.choice(ratings),
            emissor=fake.company(),
            analista=fake.name(),
            setor=random.choice(setores),
            grupo=random.choice(grupos),
            mesa_gestao=random.choice(mesas),
            data_atualizacao=datetime.now()
        )
        db.session.add(emissor)

    # Commitando as alterações no banco de dados
    db.session.commit()

    # Adicionando instituicoes de garantia aleatórias (auto-referência)
    emissores = Emissor.query.all()
    for emissor in emissores:
        emissor.instituicao_garantia_cnpj = random.choice(emissores).cnpj
        db.session.commit()

    print("Dados aleatórios inseridos com sucesso!")