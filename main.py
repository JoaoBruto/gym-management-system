import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'gym_management_db'
)

cursor = conexao.cursor()
cursor.execute("CREATE TABLE Alunos (nome VARCHAR(255) NOT NULL, id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, idade INT NOT NULL, telefone VARCHAR(20) NOT NULL, peso FLOAT NOT NULL, altura INT NOT NULL, objetivo VARCHAR(50) NOT NULL, data_matricula DATETIME NOT NULL, mensalidade_paga BOOLEAN DEFAULT TRUE)")
