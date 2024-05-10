import pymysql

class SQLreader:
    def __init__(self, host, user, password, db, port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.db = db
    def connect(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port, db=self.db)
    def close(self):
        self.conn.close()
        self.conn = None
        
if __name__ == '__main__':
    sqlreader = SQLreader('100.67.158.142', 'root', '123456', 'EyeProtection_Lab', 336)
    # del sqlreader