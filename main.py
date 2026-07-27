import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'gym_management_db'
)

def cadastrar_aluno():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: ")) #Converter numero para inteiro
    telefone = input("Digite seu telefone: ")
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    objetivo = input("Digite seu objetivo: ")

    
    cursor = conexao.cursor()
    com_sql = "INSERT INTO alunos(nome, idade, telefone, peso, altura, objetivo, mensalidade_paga) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    valor = nome, idade, telefone, peso, altura, objetivo, True
    cursor.execute(com_sql, valor)

    conexao.commit()

    print(cursor.rowcount, "Inseridas com sucesso")
cadastrar_aluno()