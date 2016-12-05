from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')


@app.route('/login')
def login():
    return render_template('login.pug')


if __name__ == '__main__':
    app.run()
