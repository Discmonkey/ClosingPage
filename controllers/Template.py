from models.PostgresConnection import PostGres
import json


class Template:

    def __init__(self):
        self.pg = PostGres()
        self.pg.connect()

    def save_template(self, template, number, user_id):
        template_name = template['inputs']['Subject']
        template_json = json.dumps(template)

        query = """
            WITH upsert AS (UPDATE templates
            SET info=%(template_json)s, name=%(template_name)s
            WHERE number=%(number)s and status=0 and user_id=%(user_id)s
            RETURNING *)

            INSERT INTO templates (user_id, info, number, status, name)
            SELECT %(user_id)s, %(template_json)s, %(number)s, 0, %(template_name)s
            WHERE NOT EXISTS (SELECT * FROM upsert)"""

        self.pg.run_query(query, {'template_json': template_json,
                                  'template_name': template_name,
                                  'user_id': user_id,
                                  'number': number})

        # will need to change.
        rows = self.pg.query("SELECT max(id) from templates "
                             "where number=%(number)s and user_id=%(user_id)s", {'number': number,
                                                                               'user_id': user_id})
        return rows[0][0]

    def load_template(self, status, number, user_id, name=''):

        params = {
            'status': status,
            'number': number,
            'user_id': user_id
        }

        if status == 0:
            query = """
                SELECT template_json FROM templates
                WHERE number=%(number)s and status=%(status)s and user_id=%(user_id)s
            """
        else:
            query = """
                SELECT template_json FROM templates
                WHERE number=%(number)s and status=%(status)s and user_id=%(user_id)s and name=%(name)s
            """
            params['name'] = name

        row = self.pg.query(query, params)

        if row:
            return row[0][0]

        return False

    def load_template_from_id(self, id):

        params = {
            'id': id
        }

        row = self.pg.query("SELECT info from templates where id = %(id)s", params)

        if row:
            return row[0][0]
