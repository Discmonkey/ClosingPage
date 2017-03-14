from models.PostgresConnection import PostGres


class User:

    def __init__(self):
        self.pg = PostGres()
        self.pg.connect()
        self.picture_url = None
        self.username = None
        self.first_name = None
        self.last_name = None
        self.email = None
        self.job_title = None
        self.company = None
        self.phone = None
        self.calendly = None
        self.signature = None
        self.address = None
        self.is_authenticated = False
        self.is_active = False
        self.is_anonymous = False
        self.id = None

    def load_user(self, user_id):
        row = self.pg.query("""SELECT email, username, picture_url, job_title, company, first_name, last_name, phone,
                            calendly, signature, address
                            FROM users where id=%(id)s""", {'id': user_id})

        if not row:
            return False

        self.is_authenticated = self.is_active = True
        self.email = row[0][0]
        self.username = row[0][1]
        self.picture_url = row[0][2] if row[0][2] else '/static/img/defaultIcon.png'
        self.job_title = row[0][3]
        self.company = row[0][4]
        self.first_name = row[0][5]
        self.last_name = row[0][6]
        self.phone = row[0][7]
        self.calendly = row[0][8]
        self.signature = row[0][9]
        self.address = row[0][10]
        self.id = user_id

        return True

    def save_user(self):
        return self.pg.run_query('''UPDATE users
        SET email = %(email)s, picture_url = %(picture_url)s, job_title = %(job_title)s, company = %(company)s,
          first_name = %(first_name)s, last_name = %(last_name)s, phone = %(phone)s, calendly = %(calendly)s,
          signature = %(signature)s, address = %(address)s, username = %(username)s
        WHERE id=%(id)s''', {'id': self.id, 'email': self.email, 'picture_url': self.picture_url,
                             'job_title': self.job_title, 'company': self.company, 'first_name': self.first_name,
                             'last_name': self.last_name, 'phone': self.phone, 'calendly': self.calendly,
                             'signature': self.signature, 'address': self.address, 'username': self.username})

    def load_linked_in(self, token):
        user_id_row = self.pg.query('SELECT id FROm users where linkedin_token=%(token)s', {'token': token})[0]
        if user_id_row:
            user_id = user_id_row[0]
            self.load_user(user_id)
        else:
            return False

    def load_username_password(self, username, password):
        row = self.pg.query('SELECT id FROM users where (username=%(username)s or email=%(username)s) and password=%(password)s', {
            'username': username,
            'password': password
        })

        if row:
            user_id = row[0][0]
            return self.load_user(user_id)
        else:
            return False

    def get_id(self):
        return self.id

if __name__ == '__main__':
    u = User()
    u.load_user(10)