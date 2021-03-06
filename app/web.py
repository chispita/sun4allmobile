# -*- coding: utf8 -*-

from core import app, api, db
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask.ext.restplus import Api, Resource

from sun4all import TaskImagesAPI, TaskImageAPI
from cells import TaskCellsAPI
from mindpaths import TaskMindPathsAPI
from v1_0 import api_v1_0, api_v1_0_bp, API_VERSION_V1_0
from v1_1 import api_v1_1, api_v1_1_bp, API_VERSION_V1_1

import json

API_VERSION = 1

@app.route("/about")
def about():
    """Render the about template"""

    data =  { 'about' : 'Api Socientize application',
             'version' : API_VERSION,
             'IP': request.remote_addr,
             'IP2': request.headers['X-Forwarded-For'],
             'browser': request.headers['User-Agent'],
            }
    return jsonify( data)

app.register_blueprint(
    api_v1_0_bp,
    url_prefix='{prefix}/v{version}'.format(
        prefix='/api',
     version=API_VERSION_V1_0))

app.register_blueprint(
    api_v1_1_bp,
    url_prefix='{prefix}/v{version}'.format(
        prefix='/api',
        version=API_VERSION_V1_1))

if __name__ == "__main__":  # pragma: no cover
    #logging.basicConfig(level=logging.NOTSET)
    app.run(host=app.config['HOST'], port=app.config['PORT'],    
        debug=app.config.get('DEBUG', True))
    
    app.logger.debug('Entro por main')
