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
        self.is_authenticated = False
        self.is_active = False
        self.is_anonymous = False
        self.id = None

    def load_user(self, user_id):
        row = self.pg.query('SELECT email, username, picture_url, job_title, company '
                             'FROM users where id=%(id)s', {'id': user_id})

        if not row:
            return False

        self.is_authenticated = self.is_active = True
        self.email = row[0][0]
        self.username = row[0][1]
        self.picture_url = row[0][2] if row[0][2] else '/static/img/defaultIcon.png'
        self.job_title = row[0][3]
        self.company = row[0][4]
        self.id = user_id

        return True

    def load_linked_in(self, token):
        user_id_row = self.pg.query('SELECT id FROm users where linkedin_token=%(token)s', {'token': token})[0]
        if user_id_row:
            user_id = user_id_row[0]
            self.load_user(user_id)
        else:
            return False

    def load_username_password(self, username, password):
        row = self.pg.query('SELECT id FROM users where username=%(username)s and password=%(password)s', {
            'username': username,
            'password': password
        })

        if row:
            user_id = row[0]
            return self.load_user(user_id)
        else:
            return False

    def get_id(self):
        return self.id

if __name__ == '__main__':
    u = User()
    u.load_user(10)