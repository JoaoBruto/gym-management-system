import pymysql
import pymysql.cursors

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'gym_management_db',
    charset = 'utf8mb4',
    cursorclass=pymysql.cursors.DictCursor 
    # DictCursor faz o cursor devolver os resultados como dicionário (nome_coluna: valor),
    # em vez de tupla — facilita acessar os campos pelo nome (ex: aluno['nome'])
)

def cadastrar_aluno():
    """Cadastra um novo aluno no banco, pedindo e validando nome, idade, telefone,
    peso, altura e objetivo. Insere o registro com mensalidade já marcada como paga."""
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
#cadastrar_aluno()

def listar_alunos():
    """Busca todos os alunos cadastrados no banco e exibe cada um formatado,
    um por linha, com todos os campos."""
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos")
    resultado = cursor.fetchall()
    for alunos in resultado:
        print(f"ID: {alunos['id']} | Nome: {alunos['nome']} | Idade: {alunos['idade']} | Telefone: {alunos['telefone']} | Peso: {alunos['peso']} | Altura: {alunos['altura']} | Objetivo: {alunos['objetivo']} | Data da matricula: {alunos['data_matricula']} | Status da mensalidade: {alunos['mensalidade_paga']}")
#listar_alunos()

def buscar_aluno():
    """Pede o ID de um aluno, busca no banco e exibe os dados dele.
    Avisa o usuário caso o ID não corresponda a nenhum aluno cadastrado."""
    while True:
        try:
            request_id = int(input("Digite o id do usuário: ")) #Converter numero para inteiro
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos WHERE id = %s", (request_id,))
    aluno_encontrado = cursor.fetchone()

    if aluno_encontrado is None:
        print("ERRO! Este usuário não está cadastrado.")
    else:
        print(f"ID: {aluno_encontrado['id']} | Nome: {aluno_encontrado['nome']} | Idade: {aluno_encontrado['idade']} | Telefone: {aluno_encontrado['telefone']} | Peso: {aluno_encontrado['peso']} | Altura: {aluno_encontrado['altura']} | Objetivo: {aluno_encontrado['objetivo']} | Data da matricula: {aluno_encontrado['data_matricula']} | Status da mensalidade: {aluno_encontrado['mensalidade_paga']}")

#buscar_aluno()

def buscar_por_mensalidade():
    """Lista todos os alunos filtrados pelo status de mensalidade
    (paga ou pendente), escolhido pelo usuário."""
    opcoes_mensalidade = ["mensalidade paga", "mensalidade pendente"]
    while True:
            escolha_mensalidade = input("Digite 'mensalidade paga' ou 'mensalidade pendente' para ver os status de mensalidade: \n")
            if escolha_mensalidade not in opcoes_mensalidade:
                print("Digite apenas as opções válidas (mensalidade paga ou mensalidade pendente)")
            else:
                break
            
    cursor = conexao.cursor()
    if escolha_mensalidade == 'mensalidade paga':
        mensalidade_numero = 1
    else:
        mensalidade_numero = 0

    cursor.execute("SELECT * FROM alunos WHERE mensalidade_paga = %s", (mensalidade_numero,))
    resultado_mensalidade = cursor.fetchall()
    for aluno in resultado_mensalidade:
        print(f"ID: {aluno['id']} | Nome: {aluno['nome']} | Idade: {aluno['idade']} | Telefone: {aluno['telefone']} | Peso: {aluno['peso']} | Altura: {aluno['altura']} | Objetivo: {aluno['objetivo']} | Data da matricula: {aluno['data_matricula']} | Status da mensalidade: {aluno['mensalidade_paga']}")
#buscar_por_mensalidade()
    
def atualizar_aluno():
     """Pede o ID de um aluno existente e permite atualizar um campo específico
    (nome, idade, telefone, peso, altura, objetivo ou status de mensalidade),
    validando o novo valor antes de salvar no banco."""
    while True:
        try:
            escolha_id = int(input("Digite o ID do aluno que você deseja atualizar: \n")) #Converter numero para inteiro
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos WHERE id = %s", (escolha_id,))
    aluno_encontrado = cursor.fetchone()

    if aluno_encontrado is None:
        print("ERRO! Este usuário não está cadastrado.")
    else:
        escolha_atualizacao = input("O que deseja atualizar? 1-Nome 2-Idade 3-Telefone 4-Peso 5-Altura 6-Objetivo 7-Mensalidade: \n")

        if escolha_atualizacao == "1":
            while True:
                novo_nome = input("Digite o novo nome de usuário: \n")
                nome_sem_espaco = novo_nome.replace(" ", "") 
                if nome_sem_espaco.isalpha():
                    break
                else:
                    print("Nome inválido, digite apenas letras.")
            cursor.execute("UPDATE alunos SET nome = %s WHERE id = %s", (novo_nome, escolha_id),)
            conexao.commit()
            print("Nome atualizado com sucesso!")

        elif escolha_atualizacao == "2":
            while True:
                try:
                    nova_idade = int(input("Digite a nova idade do usuário: \n"))
                    if nova_idade < 10 or nova_idade > 100:
                        print("Digite uma idade válida!")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida! Por favor, digite apenas números.")

            cursor.execute("UPDATE alunos SET idade = %s WHERE id = %s", (nova_idade, escolha_id),)
            conexao.commit()
            print("Idade atualizada com sucesso!")

        elif escolha_atualizacao == "3":
            while True:
                try:
                    novo_telefone = input("Digite o novo número de telefone do usuário: \n")
                    if novo_telefone.isdigit() and len(novo_telefone) == 11:
                        break
                    else:
                        print("Entrada inválida! Por favor, digite um telefone válido.")
                except ValueError:
                    print("Entrada inválida! Por favor, digite apenas números.")

            cursor.execute("UPDATE alunos SET telefone = %s WHERE id = %s", (novo_telefone, escolha_id),)
            conexao.commit()
            print("Telefone atualizado com sucesso!")


        elif escolha_atualizacao == "4":
            while True:
                try:
                    novo_peso = float(input("Digite o novo peso do usuário (kg): \n"))
                    if novo_peso < 10 or novo_peso > 450:
                        print("Digite um peso válido!")
                    else:
                        break
                except ValueError:
                    print("Entrada invalida! Por favor, digite apenas números.")
            cursor.execute("UPDATE alunos SET peso = %s WHERE id = %s", (novo_peso, escolha_id),)
            conexao.commit()
            print("Peso atualizado com sucesso!")

        elif escolha_atualizacao == "5":
            while True:
                try:
                    nova_altura = float(input("Digite a nova altura do usuário: \n"))
                    if nova_altura < 1.15 or nova_altura > 3:
                        print("Digite a altura em metros (Ex.: 1.75): ")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida! Por favor, digite apenas números.")
            cursor.execute("UPDATE alunos SET altura = %s WHERE id = %s", (nova_altura, escolha_id),)
            conexao.commit()
            print("Altura atualizada com sucesso!")

        elif escolha_atualizacao == "6":
            opcoes_validas = ["Hipertrofia", "Emagrecimento", "Manter massa muscular"]
            while True:
                novo_objetivo = input("Digite o novo objetivo do usuário: \n")
                if novo_objetivo not in opcoes_validas:
                    print("Digite apenas as opções válidas (Hipertrofia, Emagrecimento, Manter massa muscular)")
                else:
                    break
            cursor.execute("UPDATE alunos SET objetivo = %s WHERE id = %s", (novo_objetivo, escolha_id),)
            conexao.commit()
            print("Objetivo atualizado com sucesso!")

        elif escolha_atualizacao == "7":
            opcoes_validas = ["Pendente", "Pago"]
            while True:
                novo_status_mensalidade = (input("Digite o novo status da mensalidade do usuário (Pendente e Pago): \n"))
                if novo_status_mensalidade not in opcoes_validas:
                    print("Digite apenas as opções válidas: Pendente ou Pago")
                else:
                    break
            if novo_status_mensalidade == "Pendente":
                cursor.execute("UPDATE alunos SET mensalidade_paga = 0 WHERE id = %s", ( escolha_id),)
                conexao.commit()
                print("Status de mensalidade atualizado com sucesso!")
            else:
                cursor.execute("UPDATE alunos SET mensalidade_paga = 1 WHERE id = %s", ( escolha_id),)
                conexao.commit()
                print("Status de mensalidade atualizado com sucesso!")
#atualizar_aluno()
        
def excluir_aluno():
    """Pede o ID de um aluno, exibe os dados dele para confirmação e,
    caso o usuário confirme, remove o registro do banco permanentemente."""
    while True:
        try:
            id_do_usuario = int(input("Digite o ID do usuário: "))
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos WHERE id = %s", (id_do_usuario,),)
    aluno_encontrado = cursor.fetchone()

    if aluno_encontrado is None:
        print("ERRO! Este usuário não está cadastrado.")

    else:
        print(f"ID: {aluno_encontrado['id']} | Nome: {aluno_encontrado['nome']} | Idade: {aluno_encontrado['idade']} | Telefone: {aluno_encontrado['telefone']} | Peso: {aluno_encontrado['peso']} | Altura: {aluno_encontrado['altura']} | Objetivo: {aluno_encontrado['objetivo']} | Data da matricula: {aluno_encontrado['data_matricula']} | Status da mensalidade: {aluno_encontrado['mensalidade_paga']}")

        confirmacao_exclusao = input("Tem certeza que deseja excluir o usuário? (s/n) \n")
        if confirmacao_exclusao == "s":
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM alunos WHERE  id = %s", (id_do_usuario, ),)
            conexao.commit()
            print("Usuário excluido com sucesso!")
        elif confirmacao_exclusao == "n":
            print("Exclusão cancelada!")
        else:
            print("Digite apenas as opções válidas (s ou n) \n")
excluir_aluno()            