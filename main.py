import pymysql
import pymysql.cursors

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'gym_management_db',
    charset = 'utf8mb4',
    cursorclass=pymysql.cursors.DictCursor 
)

 def cadastrar_aluno():
    while True:
        nome = input("Digite seu nome: ")
        nome_sem_espaco = nome.replace(" ", "") 
        if nome_sem_espaco.isalpha():
            break
        else:
            print("Nome inválido, digite apenas letras.")

    while True:
        try:
            idade = int(input("Digite sua idade: ")) #Converter numero para inteiro
            if idade < 10 or idade > 100:
                print("Digite uma idade válida!")
            else:
                break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")


    while True:
        telefone = input("Digite seu telefone: ")
       if telefone.isdigit() and len(telefone) == 11:
            break
        else:
            print("Entrada inválida! Por favor, digite um telefone válido.")

    while True:
        try:
            peso = float(input("Digite seu peso (kg): ")) 
            if peso < 10 or peso > 450:
                print("Digite um peso válido!")
            else:
                break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")

    while True:
        try:
            altura = float(input("Digite sua altura (m): "))
            if altura < 1 or altura > 3:
                print("Digite a altura em metros (Ex.: 1.75): ")
            else:
                break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")

    opcoes_validas = ["Hipertrofia", "Emagrecimento", "Manter massa muscular"]
    while True:
           objetivo = input("Digite seu objetivo: ")
            if objetivo not in opcoes_validas:
                print("Digite apenas as opções válidas (Hipertrofia, Emagrecimento, Manter massa muscular)")
            else:
                break
    
    cursor = conexao.cursor()
    com_sql = "INSERT INTO alunos(nome, idade, telefone, peso, altura, objetivo, mensalidade_paga) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    valor = nome, idade, telefone, peso, altura, objetivo, True
    cursor.execute(com_sql, valor)

    conexao.commit()

    print(cursor.rowcount, "Inseridas com sucesso")
cadastrar_aluno()

def listar_alunos():
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos")
    resultado = cursor.fetchall()
    for alunos in resultado:
        print(f"ID: {alunos['id']} | Nome: {alunos['nome']} | Idade: {alunos['idade']} | Telefone: {alunos['telefone']} | Peso: {alunos['peso']} | Altura: {alunos['altura']} | Objetivo: {alunos['objetivo']} | Data da matricula: {alunos['data_matricula']} | Status da mensalidade: {alunos['mensalidade_paga']}")
listar_alunos()