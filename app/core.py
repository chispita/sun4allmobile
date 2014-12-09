# -*- coding: utf8 -*-

import os
import logging
from flask import Flask
from flask.ext.mail import Mail


def create_app():
    app = Flask(__name__)
    app.debug = True

    configure_app(app)
    setup_error_email(app)
    setup_logging(app)

    return app

def configure_app(app):
    here = os.path.dirname(os.path.abspath( __file__ ))
    config_path = os.path.join(os.path.dirname(here), 'settings_local.py')

    if os.path.exists(config_path): # pragma: no cover
        app.config.from_pyfile(config_path)

from logging.handlers import SMTPHandler
def setup_error_email(app):
    ADMINS = app.config.get('ADMINS', '')
    #if not app.debug and ADMINS: # pragma: no cover
    if ADMINS:
        app.logger.debug( ADMINS ) 

        mail_handler = SMTPHandler(
            mailhost=( app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr= app.config['MAIL_DEFAULT_SENDER'],
            toaddrs = ADMINS, 
            subject=u'Error en Api Socientize'
            )
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

from logging.handlers import RotatingFileHandler
from logging import Formatter
def setup_logging(app):
    log_file_path = app.config.get('LOG_FILE')
    log_level = app.config.get('LOG_LEVEL', logging.WARN)

    if log_file_path: # pragma: no cover
        file_handler = RotatingFileHandler(log_file_path)
        file_handler.setFormatter(Formatter(
            '%(name)s:%(levelname)s:[%(asctime)s] %(message)s '
            '[in %(pathname)s:%(lineno)d]'
            ))
        file_handler.setLevel(log_level)
        app.logger.addHandler(file_handler)
        logger = logging.getLogger('sun4allmobile')
        logger.setLevel(log_level)
        logger.addHandler(file_handler)

app = create_app()    
