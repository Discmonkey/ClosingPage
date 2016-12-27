import psycopg2

class PostGres:

    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = psycopg2.connect("dbname='cp_dev' user='other_user' host='34.194.214.210' password='4ngel_J4c0b'")
            self.cur = self.conn.cursor()
        except Exception as e:
            print("I am unable to connect to the database:", e)

    def is_connected(self):
        return self.cur is not None

    def register_user(self, username, email, password):
        hashed = self.hash(password)
        try:
            self.cur.execute("INSERT INTO users (username, email, password) VALUES (%(username)s, %(email)s, %(pass)s) "
                             "RETURNING id",
                             {'email': email, 'pass': hashed, 'username': username})
            self.conn.commit()

            return self.cur.fetchall()[0][0]

        except Exception as e:
            print(e)
            return False

    def login_user(self, username, password):
        hashed = self.hash(password)
        self.cur.execute("SELECT 1 FROM users WHERE email=%(username)s and password=%(password)s",
                         {'username': username, 'password': hashed})

        if self.cur.fetchall():
            return True

        return False

    def query(self, query, args):
        self.cur.execute(query, args)
        rows = self.cur.fetchall()
        return rows


    def run_query(self, query, args):
        self.cur.execute(query, args)
        num_rows = self.cur.rowcount
        self.conn.commit()

        return num_rows

    @staticmethod
    def hash(password):
        return password


if __name__ == '__main__':
    pg = PostGres()
    pg.connect()
    u_id = pg.register_user('Test2', 'test2', 'test3')
    print(u_id)