from mysql.connector import connect

conexao = connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='root'
)

print(conexao)
