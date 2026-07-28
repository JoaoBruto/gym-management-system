import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'gym_management_db'
)

def cadastrar_aluno():
    nome = input("Digite seu nome: ")

    while True:
        try:
            idade = int(input("Digite sua idade: ")) #Converter numero para inteiro
            if idade < 10 or idade > 100:
                print("Digite uma idade válida!")
            else:
                break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")

    telefone = input("Digite seu telefone: ")
    
    while True:
        try:
            peso = float(input("Digite seu peso (kg): "))
            if peso < 10 or peso > 450:
                print("Digite um peso válido!")
            else:
                break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")

    altura = float(input("Digite sua altura (m): "))
    objetivo = input("Digite seu objetivo: ")

    
    cursor = conexao.cursor()
    com_sql = "INSERT INTO alunos(nome, idade, telefone, peso, altura, objetivo, mensalidade_paga) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    valor = nome, idade, telefone, peso, altura, objetivo, True
    cursor.execute(com_sql, valor)

    conexao.commit()

    print(cursor.rowcount, "Inseridas com sucesso")
cadastrar_aluno()