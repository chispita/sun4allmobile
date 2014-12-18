# Check the official documentation http://flask.pocoo.org/docs/deploying/mod_wsgi/
# Activate the virtual env (we assume that virtualenv is in the env folder)
activate_this = '/var/www/sun4allmobile/flask/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
# Import sys to add the path
import sys
sys.path.insert(0,'/var/www/sun4allmobile')

# Run the web-app
from app.web import app as application
#from run import app as application


