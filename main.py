import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'gym_management_db'
)

cursor = conexao.cursor()
cursor.execute("ALTER TABLE alunos MODIFY COLUMN altura FLOAT NOT NULL ")
