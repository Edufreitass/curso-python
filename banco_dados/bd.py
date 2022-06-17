from contextlib import contextmanager

from mysql.connector import connect

parametros = dict(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    database='agenda'
)


@contextmanager
def nova_conexao():
    conexao = connect(**parametros)
    try:
        yield conexao
    finally:
        if conexao and conexao.is_connected():
            conexao.close()
