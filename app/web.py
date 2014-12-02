from core import app
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask.ext.restful import Api, Resource

from api import TaskImagesAPI, TaskImageAPI
from cells import TaskCellsAPI
from mindpaths import TaskMindPathsAPI

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
    return "Hello, sun4allmobile application1!"


@app.route("/about")
def about():
    """Render the about template"""
    return "Aplicacion de Ibercivis"

class TaskUsersAPeeI(Resource):

    def __init__(self):
        pass

    def get(self):
        return 'User get'

    def post(self):
        return 'User post'

api.add_resource(TaskImagesAPI, "/api/image", endpoint = 'tasks')
api.add_resource(TaskImageAPI, "/api/images/<string:description>", endpoint = 'task')


#api.add_resource(TaskCellsAPI, '/api/1.0/cellresults', endpoint = 'viewcellsresults')

api.add_resource(TaskCellsAPI, "/api/cellresults", endpoint ='cells')

api.add_resource(TaskMindPathsAPI, "/api/mindpathsresults", endpoint ='mindpaths')

if __name__ == "__main__":  # pragma: no cover
    #logging.basicConfig(level=logging.NOTSET)
    app.run(host=app.config['HOST'], port=get_port(),
    debug=app.config.get('DEBUG', True))

