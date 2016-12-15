from flask import Flask, render_template, request
import json

app = Flask(__name__)
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')


@app.route('/')
def index():
    return render_template('index.pug')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.pug')
    elif request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']


@app.route('/register', methods=['POST'])
def register():
    user_name = request.form['user_name']
    password = request.form['password']


@app.route('/linkedInAuth')
def linked_in_auth():
    return json.dumps(request)

if __name__ == '__main__':
    app.run()
