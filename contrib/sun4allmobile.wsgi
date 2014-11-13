activate_this = '/var/www/sun4allmobile/flask/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
# Import sys to add the path of PyBossa
import sys
sys.path.insert(0,'/var/www/sun4allmobile')
# Run the web-app
from app.views import app as application
