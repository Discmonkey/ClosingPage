from flask import Flask, render_template, request, redirect
from flask_login import LoginManager
from apis.PostgresConnection import PostGres
import requests
import json
from user import User

app = Flask(__name__)
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
pg = PostGres()
pg.connect()

login_manager = LoginManager()
login_manager.init(app)


@login_manager.user_loader
def load_user(user_id):
    usr = User()
    valid = usr.load_user(user_id)
    if valid:
        return usr
    else:
        return None







@app.route('/')
def index():
    return render_template('index.pug')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.pug')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if pg.login_user(username, password):
            return redirect('/')


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    if username and password and email:
        if pg.register_user(username, email, password):
            return redirect('/')
        else:
            return redirect('/login')


@app.route('/linkedInAuth')
def linked_in_auth():
    if request.method == 'GET':
        code = request.values['code']
        payload = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': 'http://closingpage.com/linkedInAuth',
            'client_id': '78c1zfn9rje6f4',
            'client_secret': 'ijSehCeY9DmRIEWw'
        }

        res = requests.post('https://www.linkedin.com/oauth/v2/accessToken', data=payload)

        token = json.loads(res.content.decode('UTF-8'))['access_token']


        return redirect('/')

if __name__ == '__main__':
    app.run()
