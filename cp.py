from flask import Flask, render_template, request, redirect
from apis.PostgresConnection import PostGres
import json

app = Flask(__name__)
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
pg = PostGres()
pg.connect()


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
    return json.dumps(request)

if __name__ == '__main__':
    app.run()
