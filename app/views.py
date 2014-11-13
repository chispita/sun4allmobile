#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask.ext.httpauth import HTTPBasicAuth

import json

import dbmobile_images
import dbmobile_points
 
app = Flask(__name__, static_url_path = "")
auth = HTTPBasicAuth()
 
@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None
 
@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog
    
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

@app.route('/api/images', methods = ['GET'])
#@auth.login_required
def get_images():
    """
    Get all images
    """ 
    images = dbmobile_images.getall()

    result = []

    if images is None:
        abort(404)

    for image in images:
        result.append( image.to_json())

    return jsonify( { 'images':  result } )
 
@app.route('/api/images/<int:image_id>', methods = ['GET'])
#@auth.login_required
def get_image(image_id):
    """
    Search a image by id 
    """
    image = dbmobile_images.get(image_id)
    if image is None:
        abort(404)

    return jsonify( { 'image': image.to_json() } )

@app.route('/api/images/<int:image_id>/<int:point_id>', methods = ['GET'])
#@auth.login_required
def get_point(image_id,point_id):
    """ 
    Get Data of one point
    """

    """
    image = filter(lambda t: t['id'] == image_id, images)
    if len(image) == 0:
        abort(404)

    if point_id-1 < 0:
        abort(404)

    if point_id -1 >= len(image[0]['points']):
        abort(404)

    image_tmp = {
        'id': images[0]['id'],
        'description': images[0]['description'],
        'done': images[0]['done'],
        'points': images[0]['points'][point_id-1]
    }
    """

    return jsonify( { 'image' : image_tmp } )
 
@app.route('/api/images', methods = ['POST'])
#@auth.login_required
def create_image():
    """ 
    Create a new element
    """

    if not request.json or not 'points' in request.json or not 'description' in request.json :
        return jsonify( 
            {
                'status':       'failed',
                'action':       'POST',
                'exception_msg':'description or points field Not Found',
                'status_code':  400
            }),400

    image = dbmobile_images.init()
    image.from_json(request.json)
    dbmobile_images.add(image)

    for src in request.json['points']:
        point = dbmobile_points.init()
        point.images_id = image.id
        
        point.x = src['x']
        point.y = src['y']

        dbmobile_points.add(point)

    return jsonify( { 'image': image.to_json() } )
    
if __name__ == '__main__':
    app.debug = True
    app.run()
