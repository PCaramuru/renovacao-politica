import psycopg2
import pandas as pd
import json
from sqlalchemy import create_engine


class Config:
    def __init__(self):
        with open('config.json') as json_file:
            json_values = json.load(json_file)

            database = json_values['projetos_db']['database']
            user = json_values['projetos_db']['user']
            password = json_values['projetos_db']['password']
            host = json_values['projetos_db']['host']
            port = json_values['projetos_db']['port']

        self.config = {"postgres": {"database": database,
                                    "user": user,
                                    "password": password,
                                    "host": host,
                                    "port": port}}
        
        conn_str_sqlalchemy = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
                    
        conn_str_sqlalchemy = conn_str_sqlalchemy.format(database = database,
                                                         user = user,
                                                         host = host,
                                                         password = password,
                                                         port = port)   

        engine_sqlalchemy = create_engine(conn_str_sqlalchemy)

        self.engine = engine_sqlalchemy
        self.connect = engine_sqlalchemy.connect()

class Connection(Config):
    def __init__(self):
        Config.__init__(self)
        try:
            self.conn = psycopg2.connect(**self.config["postgres"])
            self.cur = self.conn.cursor()
        except Exception as e:
            print("Erro na conexão:", e)
            exit(1)

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self.conn
        
    @property
    def cursor(self):
        return self.cur
        
    def commit(self):
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()
        
    def execute(self, sql, params = None):
        #self.cursor.execute(sql, params, ())
        self.cursor.execute(sql, params)

    def query(self, sql, params = None):
        #self.cursor.execute(sql, params, ())
        self.cursor.execute(sql, params)
        return self.fetchall()
        
class Projetos(Connection):
    def __init__(self):
        Connection.__init__(self)

    def insert(self, *args):
        try:
            sql = f"INSERT INTO tb_projetos_candidatos_clean {args} VALUES (%s)"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("Erro ao inserir:", e)

    def insert_df(self, table, df):
        if (df.shape[0]>0 and len(table)>0):
            try:
                engine_sqlalchemy = create_engine(f"postgresql+psycopg2://{self.config['postgres']['user']}:{self.config['postgres']['password']}@{self.config['postgres']['host']}:{self.config['postgres']['port']}/{self.config['postgres']['database']}")
                self.engine = engine_sqlalchemy
                self.connect = engine_sqlalchemy.connect()                
                df.to_sql(table, self.connect, if_exists='append', index=False)
                return f"Dataframe {df} apensado à tabela {table}"
            except AssertionError as error:
                print(error)
                print("Método create_insert_data falhou")
                return None
        else:
           print("create_insert_data missing:", table, ", insert_str or df null")

    def delete(self, id):
        try:
            sql_s = f"SELECT * FROM tb_projetos_candidatos_clean WHERE id = {id}"
            if not self.query(sql_s):
                return "Registro não encontrado para deletar"
            sql_d = f"DELETE FROM tb_projetos_candidatos_clean WHERE id = {id}"
            self.execute(sql_d)
            self.commit()
            return "Registro deletado."
        except Exception as e:
            print("Erro ao deletar:", e)

    def update(self, id, *args):
        try:
            sql = f"UPDATE tb_projetos_candidatos_clean SET name = %s WHERE id = {id}"
            self.execute(sql, args)
            self.commit()
            return f"Registro atualizado"
        except Exception as e:
            print("Erro ao atualizar", e)

    def search(self, *args, type_s = "name"):
        sql = "SELECT * FROM tb_projetos_candidatos_clean WHERE name LIKE %s"
        if type_s == "id":
            sql = "SELECT * FROM tb_projetos_candidatos_clean WHERE id LIKE %s"
        data = self.query(sql, args)
        if data:
            return data
        return f"Registro não encontrado"
    
    def read_col(self, *col_names):
        try:
            response = pd.DataFrame()
            for i in col_names:
                sql_query = f"SELECT \"{i}\" FROM tb_projetos_candidatos_clean"
                sql_query = sql_query.format(table_value = "tb_projetos_candidatos_clean")
                query_set = pd.read_sql_query(sql_query, self.connection)
                response[i] = pd.DataFrame(query_set)
            self.connection.close
            return response
        except AssertionError as error:
            print(error)
            print("Leitura de coluna falhou")
            return None

    #? revisar implementação
    def tb_exists(self, *tb_name):
        sql_query = "SELECT * FROM public.tables WHERE table_name LIKE %s"
        sql_query = sql_query.format(table_value = tb_name)
        query_set = None
        try:
            query_set = self.query(sql_query, *tb_name)
            #query_set = pd.read_sql_query(sql_query, self.connection)
            if query_set != None:
                return True
            else:
                print(f"Tabela {tb_name} não encontrada.")
                return False
        except AssertionError as error:
            print("Procura de tabela falhou:", error)
        return None


#    def insert_csv(self, filename):
#        try:
#            data = csv.DictReader(open(filename, encoding = "utf-8"))
#            for row in data:
#                self.insert(row['name'], row['email'])
#                print("Registro inserido.")
#        except Exception as e:
#            print("", e)

if __name__ == "__main__":

    with open('config.json') as json_file:
        json_values = json.load(json_file)

    database = json_values['projetos_db']['database']
    user = json_values['projetos_db']['user']
    password = json_values['projetos_db']['password']
    host = json_values['projetos_db']['host']
    port = json_values['projetos_db']['port']

    conexao = psycopg2.connect(database = database,
                            host = host,
                            user = user,
                            password = password,
                            port = port)

    print(conexao.info)
    print(bool(conexao.status))