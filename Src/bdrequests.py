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
    
    def get_data(self, page, function):
        cur = self.conn.cursor()
        cur.execute(f'SELECT * FROM {function}(%s)', (page,)) 
        results = cur.fetchall()
        cur.close()
        return results
    
    def delete_data(self, function, id):
        cur = self.conn.cursor()
        cur.callproc(function, [id])
        self.conn.commit()
        cur.close()

    def block_data(self, function, id):
        cur = self.conn.cursor()
        cur.callproc(function, [id])
        cur.close()

    def edit_data(self, function, id, values):
        cur = self.conn.cursor()
        cur.callproc(function, [id] + values)
        self.conn.commit()
        cur.close()

    
    def add_data(self, function, values):
        cur = self.conn.cursor()
        cur.callproc(function, values)
        self.conn.commit()
        cur.close()

    def getValues(self, function):
        cur = self.conn.cursor()
        cur.execute(f'SELECT * FROM {function}();') 
        results = cur.fetchall()
        res  = [val1[0] for val1 in results]
        cur.close()
        return res
    
    def get_login(self):
        cur = self.conn.cursor()
        cur.execute(f'SELECT * FROM get_last_login();') 
        result = cur.fetchall()[0]
        cur.close()
        return result