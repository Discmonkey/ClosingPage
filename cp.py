import json
import os

import requests
from flask import Flask, render_template, request, redirect, session, flash
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from werkzeug.utils import secure_filename

from apis.ConvertApi import ConvertApi
from apis.LinkedIn import LinkedIn

from controllers.File import FileController
from controllers.user import User
from controllers.Template import Template
from controllers.simple_email import Email
from models.PostgresConnection import PostGres

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
ALLOWED_EXTENSIONS = {'ppt', 'gif', 'pdf', 'jpg', 'png'}


app = Flask(__name__)
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.secret_key = 'not_so_secret, eh?'


pgModel = PostGres()
pgModel.connect()
liApi = LinkedIn()
caApi = ConvertApi()
uploadCtrl = FileController(ALLOWED_EXTENSIONS)
emailCtrl = Email()
temp = Template()

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    usr = User()
    valid = usr.load_user(user_id)
    if valid:
        user_id = usr.get_id()
        file_path = CURRENT_DIRECTORY + '/static/files/user_{}'.format(user_id)
        FileController.create_directory(file_path)
        return usr
    else:
        return None


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')


@app.route('/')
def home():
    return render_template('home.pug')


@app.route('/create')
@login_required
def index():
    user = User()
    user.load_user(session['user_id'])
    return render_template('index.pug', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.pug')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User()
        if user.load_username_password(username, password):
            login_user(user)
            session['user_id'] = user.id
            flash('Login Success', 'success')
            return redirect('/create')
        else:
            flash('Login Failed', 'error')
            return redirect('/login')


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    if username and password and email:
        user_id = pgModel.register_user(username, email, password)
        if user_id:
            user = User()
            user.load_user(user_id)
            login_user(user)
            session['user_id'] = user_id
            return redirect('/create')
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
        info = liApi.get_profile_info(token)
        liApi.insert_profile(info, token)
        user = User()
        user.load_linked_in(token)
        login_user(user)
        session['user_id'] = user.id
        return redirect('/create')


@app.route('/get-in-touch', methods=['POST'])
def get_in_touch():
    first = request.form['first_name']
    last = request.form['last_name']
    email = request.form['email']

    message = "{} {} is interested in trying out closingpage, he can be contacted at {}".format(first,
                                                                                                last,
                                                                                                email)
    emailCtrl.send(message, 'Demo Request', ['maxmgrinchenko@gmail.com',
                                             'kp@closingpage.com',
                                             'sharath@closingpage.com'])

    return redirect('/')


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user = User()
    user.load_user(session['user_id'])
    if request.method == 'POST':
        user.email = request.form['email']
        user.company = request.form['business']
        user.first_name = request.form['firstname']
        user.last_name = request.form['lastname']
        user.job_title = request.form['position']
        user.company = request.form['business']
        # user.picture_url = request.form['filebutton']
        user.phone = request.form['phone']
        user.calendly = request.form['calendly']
        user.signature = request.form['signature']
        user.address = request.form['address']

        user.save_user()
    return render_template('views/profile.pug', user=user)


@app.route('/partials/<partial>')
def partials(partial):
    return render_template('partials/' + partial)


@app.route('/partials/<partial_dir>/<partial>')
def partials_dir(partial_dir, partial):
    return render_template('partials/' + partial_dir + '/' + partial)


@app.route('/angular-components/<partial>')
def components(partial):
    return render_template('angular-components/' + partial)


@app.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect('/login')


@app.route('/tests/<component>')
def directive_test_suite(component):
    return render_template('tests/test-component.pug', test_component=component)


@app.route('/contact')
@login_required
def contact():
    return render_template('views/contact.pug')


@app.route('/upload', methods=['POST'])
@login_required
def upload():
    if 'file' not in request.files:
        return '[]', 400, {'Content-Type': 'application/json'}

    file = request.files['file']
    filename = secure_filename(file.filename)
    if filename == '':
        return '[]', 400, {'Content-Type': 'application/json'}

    if not uploadCtrl.is_file_allowed(filename):
        return '[]', 415, {'Content-Type': 'application/json'}

    file_ext = uploadCtrl.get_file_ext(filename)
    file_dir = 'static/files/user_{}/'.format(current_user.get_id())

    if file_ext in ['pdf', 'ppt', 'gif', 'jpg', 'png']:

        rand_file_name = uploadCtrl.create_file_name(filename)
        resource_path = file_dir + rand_file_name
        save_path = os.path.join(CURRENT_DIRECTORY, resource_path)
        file.save(save_path)

        if file_ext in ['gif', 'jpg', 'png']:

            json_res = {
                'display': file_ext,
                'source': '/' + resource_path
            }
            return json.dumps(json_res), 200

        else:
            img_paths = caApi.convert_and_extract(rand_file_name, file_dir, CURRENT_DIRECTORY, file_ext)
            json_res = {
                'display': 'ppt',
                'source': list(map(lambda x: '/' + x, img_paths))
            }

            return json.dumps(json_res), 200


@app.route('/removeFile', methods=['POST'])
@login_required
def remove():
    filename = secure_filename(request.json['filename'])
    user_id = current_user.get_id()
    file_path = 'static/files/user_{}/'.format(user_id) + filename
    uploadCtrl.remove_file(file_path)


@app.route('/save-template/<num>', methods=['POST'])
@login_required
def save_template(num):
    template = request.data
    template = json.loads(template.decode('utf-8'))
    user_id = current_user.get_id()
    temp.save_template(template, num, user_id)
    return 'success'


@app.route('/publish-from-create', methods=['POST'])
@login_required
def publish_from_create():
    template = request.data
    template = json.loads(template.decode('utf-8'))
    user_id = current_user.get_id()
    template_id = temp.save_template(template, 1, user_id)
    temp.publish_template(template_id)
    user_name = current_user.username
    return_json = {'url': 'http://closingpage.com/{}/{}'.format(user_name, template_id)}

    return json.dumps(return_json), 200, {'Content-Type': 'application/json'}


@app.route('/publish-template/<num>', methods=['POST'])
@login_required
def publish_template(num):
    template = json.loads(request.data.decode('utf-8'))
    user_id = current_user.get_id()
    temp.save_template(template, num, user_id)
    return redirect('/login')


@app.route('/publish-direct/<template_id>', methods=['POST'])
def publish_direct(template_id):
    if temp.publish_template(template_id):
        user_name = current_user.username
        return_json = {'url': 'http://closingpage.com/{}/{}'.format(user_name, template_id)}

        return json.dumps(return_json), 200, {'Content-Type': 'application/json'}

    return "template not found", 404, {'Content-Type': 'application/json'}


@app.route('/preview/<num>', methods=['POST', 'GET'])
@login_required
def preview_template(num):
    if request.method == 'POST':
        template = json.loads(request.data.decode('utf-8'))
        user_id = current_user.get_id()
        temp_id = temp.save_template(template, num, user_id)
        data = json.dumps({'template_id': temp_id})

        return data, 200, {'Content-Type': 'application/json'}

    elif request.method == 'GET':
        template = temp.load_template_from_id(num)
        return render_template("pages/preview.pug", template=template, template_id=num)


@app.route('/<user_name>/<template_id>', methods=['POST', 'GET'])
def view_template(user_name, template_id):
    template = temp.load_template_from_id(template_id, True)

    if template:
        return render_template("pages/published_template.pug", template=template)
    else:
        return render_template("pages/template_not_found.pug")


@app.route('/test')
def test():
    return render_template('tests/test-page.pug')


@app.context_processor
def inject_user():
    return dict(user=current_user)

if __name__ == '__main__':
    app.run()
