import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()


def criar_table(cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
    conexao.commit()

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO CLIENTES (nome, email) VALUES(?, ?)", data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE CLIENTES SET nome=?, email=? WHERE id=?;', data)
    conexao.commit()

def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute('DELETE FROM clientes WHERE id=?;', data)
    conexao.commit()

def inserir_muitos(conexao, cursor, dados):
    cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?,?)', dados)
    conexao.commit()

def recuperar_cliente(cursor, id):
    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

# cliente = recuperar_cliente(cursor, 2)
# print(cliente)

def listar_clientes(cursor):
    return cursor.execute("select * from clientes ORDER BY nome DESC;")


clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)

cliente = recuperar_cliente(cursor, 2)
print(dict(cliente))
print(cliente["id"], cliente["nome"], cliente["email"])

print(f'seja bem vindo(a) ao sistema {cliente['nome']}')
      
# dados = [
#     ('Guilherme', 'guilherme@gmail.com'),
#     ('Ana', 'ana@gmail.com'),
#     ('Joao', 'Joao@gmail.com'),
# ]

#inserir_muitos(conexao, cursor, dados)
