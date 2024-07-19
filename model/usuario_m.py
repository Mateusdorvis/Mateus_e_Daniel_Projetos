import mariadb
import sys

class UsuarioModel:
    def __init__(self, db_name='dan_database', user='root', password='', host='localhost', port=3306):
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

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS jogos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                usuario VARCHAR(100),
                senha VARCHAR(100)
            )
        ''')
        self.conn.commit()

    def verifica_senha(self, nome, senha):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM jogos WHERE usuario = ? AND senha = ?', (nome, senha))
            user = cursor.fetchone()
            return user is not None
    
    

    def cria_usuario(self, usuario, senha):
        try:
            self.cursor.execute('SELECT * FROM jogos WHERE usuario = %s', (usuario,))
            if self.cursor.fetchone():
                return False
            
            self.cursor.execute('INSERT INTO jogos (usuario, senha) VALUES (%s, %s)', (usuario, senha))
            self.conn.commit()
            return True
        except mariadb.Error as e:
            print(f"Erro ao criar usuário: {e}")
            return False
    

    def deletar_usuario(self,id):
        cursor = self.conn.cursor()
        cursor.execute(f'''
            delete from usuarios 
            where id = ? 
        ''',(id,))

        self.conn.commit()


    def atualiza_usuario(self,nome,idade,id):
        cursor = self.conn.cursor()
        cursor.execute(f'''
            update usuarios
            set nome = ?,idade = ?
            where id = ?
        ''',(nome,idade,id,))
       
        self.conn.commit()
    def selecionar_usuarios(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM usuarios')
        return cursor.fetchall()

    def fechar_conexao(self):
        self.conn.close()



# Exemplo de uso
if __name__ == "__main__":
    modelo = UsuarioModel(db_name='seu_banco', user='seu_usuario', password='sua_senha')
    modelo.inserir_usuario('João', 25)
    usuarios = modelo.selecionar_usuarios()
    print("Usuários na tabela:")
    for usuario in usuarios:
        print(usuario)
    modelo.fechar_conexao()