# CRUD no banco de dados MySQL
# Create Read Update Delete
# Criar, Ler, Atualizar e Deletar informações em um banco de dados

# Através do conector é possível interagir com o banco de dados utilizando linguagem SQL

import mysql.connector
from mysql.connector import errorcode

# CONTROLE DE ACESSO
print(f" ==== Acesso ao Banco de Dados do MySQL ==== ")

# Configurações do banco de dados MySQL

nome_banco = "db_python"
nome_host = "localhost"
usuario = "root"
senha = "rootpassword"

# Conexão ao banco de dados MySQL
try:
    conexao = mysql.connector.connect(host= nome_host, user= usuario, password= senha, database= nome_banco)
except mysql.connector.Error as erro:
    if erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Erro! Usuário ou senha inválidos")
    elif erro.errno == errorcode.ER_BAD_DB_ERROR:
        print("Erro! O banco de dados não existe")
    else:
        print(erro)
else:
    print("Conexão realizada com sucesso!")
    cursor = conexao.cursor()

    print(f" ==== Operações com Tabelas ==== ")
    nome_tabela = 'nova_tabela'

    # Deletar uma tabela do banco de dados
    print(f'Deletando a tabela {nome_tabela}')
    delete_tabela = f'DROP TABLE IF EXISTS {nome_tabela}'
    cursor.execute(delete_tabela)  # execução do comando SQL

    # Criar uma nova tabela no banco de dados
    print(f'Criando a tabela {nome_tabela}')
    campos = 'Nome VARCHAR(45), Idade INT'
    nova_tabela = f'CREATE TABLE IF NOT EXISTS {nome_tabela} ({campos})'
    cursor.execute(nova_tabela)  # execução do comando SQL


    # CRUD
    print(f" ==== CRUD - Banco de Dados {conexao.database} ==== ")

    # CREATE
    nome1 = 'Sandy Junior'
    idade1 = 31
    nome2 = 'Eddie Murphy'
    idade2 = 67

    # definição do comando SQL
    comando1 = f'INSERT INTO {nome_tabela} (Nome, Idade) VALUES ("{nome1}", "{idade1}")'
    cursor.execute(comando1)  # execução do comando SQL

    comando2 = f'INSERT INTO {nome_tabela} (Nome, Idade) VALUES ("{nome2}", "{idade2}")'
    cursor.execute(comando2)  # execução do comando SQL

    conexao.commit()  # edita o banco de dados

    # READ
    ler = f'SELECT * FROM {nome_tabela}'
    cursor.execute(ler)
    resultado = cursor.fetchall()  # ler o banco de dados
    print(resultado)

    # UPDATE
    # fazer....

    # DELETE
    # fazer....

    # Fecha a conexão
    cursor.close()
    conexao.close()