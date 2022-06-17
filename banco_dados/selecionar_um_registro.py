from bd import nova_conexao

sql = 'SELECT tel, nome FROM contatos'

with nova_conexao() as conexao:
    cursor = conexao.cursor(buffered=True)
    cursor.execute(sql)

    print(cursor.fetchone())
