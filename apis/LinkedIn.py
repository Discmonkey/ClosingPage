import json

import requests

from models.PostgresConnection import PostGres as pg


class LinkedIn:

    def __init__(self):
        self.pg = pg()
        self.pg.connect()

    @staticmethod
    def return_default_values():
        return {
            'email': 'email',
            'username': 'username',
            'first_name': 'first',
            'last_name': 'last',
            'picture_url': '/static/img/defaultIcon.png',
            'job_title': 'awesome',
            'company': 'company',
            'id': '',
            'token': ''
        }

    def insert_token(self, token):
        query = """
            INSERT INTO users (linkedin_token) VALUES (%(token)s)
        """

        self.pg.run_query(query, {'token': token})

    def insert_profile(self, user_obj, token):

        insert_obj = self.return_default_values()

        if 'emailAddress' in user_obj:
            insert_obj['email'] = user_obj['emailAddress']

        if 'firstName' in user_obj:
            insert_obj['first_name'] = user_obj['firstName']
            insert_obj['username'] = user_obj['firstName']

        if 'lastName' in user_obj:
            insert_obj['last_name'] = user_obj['lastName']

        if 'positions' in user_obj:
            if 'values' in user_obj['positions']:
                if len(user_obj['positions']['values']) > 0:
                    pos = user_obj['positions']['values'][0]

                    if 'title' in pos:
                        insert_obj['job_title'] = pos['title']

                    if 'company' in pos and 'name' in pos['company']:
                        insert_obj['company'] = pos['company']['name']

        if 'pictureUrl' in user_obj:
            insert_obj['picture_url'] = user_obj['pictureUrl']

        if 'id' in user_obj:
            insert_obj['id'] = user_obj['id']

        insert_obj['token'] = token

        user_id = self.pg.run_query("""
            WITH upsert AS (UPDATE users
            SET email=%(email)s, username=%(username)s, picture_url=%(picture_url)s,
            job_title=%(job_title)s, company=%(company)s, linkedin_token=%(token)s, first_name=%(first_name)s,
            last_name=%(last_name)s
            WHERE linkedinid=%(id)s or email=%(email)s
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

