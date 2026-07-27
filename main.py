import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'gym_management_db'
)

cursor = conexao.cursor()
cursor.execute("ALTER TABLE alunos MODIFY COLUMN data_matricula TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP")