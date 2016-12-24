import requests
from apis.PostgresConnection import PostGres as pg
import json

class LinkedIn:

    def __init__(self):
        self.pg = pg()
        self.pg.connect()

    def insert_token(self, token):
        query = """
            INSERT INTO users (linkedin_token) VALUES (%(token)s)
        """

        self.pg.run_query(query, {'token': token})

    def insert_profile(self, user_obj, token):

        insert_obj = {
            'email': user_obj['emailAddress'],
            'username': user_obj['firstName'],
            'first_name': user_obj['firstName'],
            'last_name': user_obj['lastName'],
            'picture_url': user_obj['pictureUrl'],
            'job_title': user_obj['positions']['values'][0]['title'],
            'company': user_obj['positions']['values'][0]['company']['name'],
            'id': user_obj['id'],
            'token': token
        }

        user_id = self.pg.run_query("""
            WITH upsert AS (UPDATE users
            SET email=%(email)s, username=%(username)s, picture_url=%(picture_url)s,
            job_title=%(job_title)s, company=%(company)s, linkedin_token=%(token)s, first_name=%(first_name)s,
            last_name=%(last_name)s
            WHERE linkedinid=%(id)s
            RETURNING *)
            
            INSERT INTO users (email, username, picture_url, job_title, company, linkedinid,
            linkedin_token, first_name, last_name)
            SELECT %(email)s, %(username)s, %(picture_url)s, %(job_title)s, %(company)s, %(id)s, %(token)s,
            %(first_name)s, %(last_name)s
            WHERE NOT EXISTS (SELECT * FROM upsert)
        """, insert_obj)

        return user_id

    def get_profile_info(self, token):
        url = 'https://api.linkedin.com/v1/people/~:' \
              '(id,first-name,last-name,headline,picture-url,positions,email-address)' \
              '?format=json&oauth2_access_token={}'.format(token)

        headers = {'x-li-format': 'json', 'x-li-src': 'msdk'}

        res = requests.get(url, headers=headers)
        json_res = json.loads(res.content.decode('UTF-8'))

        return json_res


if __name__ == '__main__':

    test_token = 'AQV0aYuVMQFBokhkbA7vyfD7ApG2hZJZdMxEJCy1fdaHgHT7IR1znjcqsvXalDTvEL0rAluLIdgtnZGu3NQsYqWhH3F-bzHVdE' \
                 'N5JfLvWVTr53S8ykT6vWqK_c3j0gLH3B85J13aMoTz8uxebAJtjVkYpqlnKYsiuGDAnxYSkxGACQ1X8Jk'
    li = LinkedIn()

    response = li.get_profile_info(test_token)

    user_id = li.insert_profile(response, test_token)
    print(user_id)

