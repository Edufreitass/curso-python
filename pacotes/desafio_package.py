from app.negocio import nome_existe
from app.negocio.backed import add_nome
from app.utils.gerador import novo_nome


def main():
    while True:
        nome = novo_nome()
        if not nome_existe(nome):
            add_nome(nome)
            break

    print(f'Criado novo nome de testes: "{nome}"')