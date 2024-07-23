import mariadb
import sys

class UsuarioModel:
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
       
        self.create_table()

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

    def verifica_senha(self,nome,data_de_nascimento,senha):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM usuario WHERE nome = ?, data_de_nascimento = ? AND senha = ?', (nome,data_de_nascimento,senha))
            user = cursor.fetchone()
            return user is not None
    
    

    def cria_usuario(self,nome,data_de_nascimento,senha):
        try:
            self.cursor.execute('SELECT * FROM usuario WHERE nome = ?', (nome,))
            if self.cursor.fetchone():
                return False
            
            self.cursor.execute('INSERT INTO usuario (nome, data_de_nascimento, senha) VALUES (?, ?, ?)', (nome,data_de_nascimento,senha))
            self.conn.commit()
            return True
        except mariadb.Error as e:
            print(f"Erro ao criar o usuário {e}. O usuário já existe!")
            return False
    

    def deletar_usuario(self,id):
        cursor = self.conn.cursor()
        cursor.execute(f'''
            delete from usuarios 
            where id = ? 
        ''',(id,))

        self.conn.commit()


    def atualiza_usuario(self,nome_novo,data_de_nascimento,senha,nome):
        cursor = self.conn.cursor()
        cursor.execute(f'''
            update usuario
            set nome = ?, data_de_nascimento = ? AND senha = ?
            where nome = ?
        ''',(nome_novo,data_de_nascimento,senha,nome))
       
        self.conn.commit()
        
    def selecionar_usuarios(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM usuario')
        return cursor.fetchall()

    def fechar_conexao(self):
        self.conn.close()