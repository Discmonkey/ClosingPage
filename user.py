from apis.PostgresConnection import PostGres

class User:

    def __init__(self):
        self.pg = PostGres()
        self.pg.connect()
