import sys
import site
import os

site.addsitedir(os.path.join(os.path.dirname(__file__), 'env/local/lib64/python3.4/site-packages/'))
sys.path.insert(0, '/var/www/html/ClosingPage')

activate_env = os.path.expanduser(os.path.join(os.path.dirname(__file__), 'env/bin/activate_this.py'))
exec(open(activate_env).read(), dict(__file__=activate_env))

from cp import app as application
