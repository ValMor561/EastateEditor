import psycopg2

class BDRequests():

    def __init__(self):
        self.conn = psycopg2.connect(database="Eastate", user="postgres", password="root", host="localhost", port="5432")

    def __del__(self):
        self.conn.close()

    def auth(self, login, password):
        cur = self.conn.cursor()
        cur.execute("SELECT check_user_auth(%s, %s)", (login, password))
        auth_result = cur.fetchone()[0] 
        cur.close()
        return auth_result

    def audit(self,username, event_type):
        cur = self.conn.cursor()
        cur.callproc("log_audit", [username, event_type])
        self.conn.commit()
        cur.close()

    def signup(self, login, password):
        cur = self.conn.cursor()
        cur.execute("SELECT register_user(%s, %s)", (login, password))
        reg_result = cur.fetchone()[0] 
        self.conn.commit()
        cur.close()
        return reg_result
    
    def get_REO(self, page):
        cur = self.conn.cursor()
        # Вызов функции курсора для первой страницы (page_num=1)
        cur.execute('SELECT * FROM get_real_estate_data(%s)', (page,)) 
        results = cur.fetchall()
        # Закрытие соединения с базой данных
        cur.close()
        return results