from core import app
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask.ext.restful import Api, Resource

from sun4all import TaskImagesAPI, TaskImageAPI
from cells import TaskCellsAPI
from mindpaths import TaskMindPathsAPI
from v1_0 import api_v1_0, api_v1_0_bp, API_VERSION_V1_0
from v1_1 import api_v1_1, api_v1_1_bp, API_VERSION_V1_1

import json

API_VERSION = 1

# other views ...
api = Api(app)


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route('/')
@app.route('/index')
def index():
    """
    Home page
    """
    
    data =  { 'hello' : 'Hello socientize api',
             'version' : API_VERSION,
            }

    return jsonify( data)


@app.route("/about")
def about():
    """Render the about template"""
    return "Aplicacion de Ibercivis"

api.add_resource(TaskImagesAPI, "/api/image", endpoint = 'tasks')
api.add_resource(TaskImageAPI, "/api/images/<string:description>", endpoint = 'task')
api.add_resource(TaskCellsAPI, "/api/cellresults", endpoint ='cells')
api.add_resource(TaskMindPathsAPI, "/api/mindpathsresults", endpoint ='mindpaths')

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
    app.run(host=app.config['HOST'], port=get_port(),
    debug=app.config.get('DEBUG', True))
