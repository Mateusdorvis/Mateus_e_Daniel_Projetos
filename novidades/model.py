import mariadb
import sys

class Model:
    def __init__(self, db_name='app_jogos', user='root', password='', host='localhost', port=3306):
        try:
            self.conn = mariadb.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=db_name
            )
        except mariadb.Error as e:
            print(f"Erro de conexão ao MariaDB: {e}")
            sys.exit(1)
       
        self.create_table_usuario()

    def create_table_usuario(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuario (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) UNIQUE,
                data_de_nascimento VARCHAR(50),
                senha VARCHAR(100)
            )
        ''')
        self.conn.commit()

    def inserir_usuario(self, nome, data_de_nascimento, senha):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM usuario WHERE nome = ?', (nome,))
            if cursor.fetchone():
                return False
            
            cursor.execute('INSERT INTO usuario (nome, data_de_nascimento, senha) VALUES (?, ?, ?)', (nome, data_de_nascimento, senha))
            self.conn.commit()
            return True
        except mariadb.Error as e:
            print(f"Erro ao criar o usuário {e}.")
            return False

    def selecionar_usuarios(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM usuario')
        return cursor.fetchall()

    def fechar_conexao(self):
        self.conn.close()
