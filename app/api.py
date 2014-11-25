from flask import jsonify, abort, request
from flask.ext.restful import Resource

import json

import dbmobile_images
import dbmobile_points

class TaskImagesAPI(Resource):
    def __init__(self):
        pass

    def get(self):
        """ 
        Show all images
        """
        images = dbmobile_images.getall()

        if images is None:
            abort(404)

        result = []
        for image in images:
            result.append(image.to_json())

        return jsonify( { 'images':  result } )

    def post(self):
        """ 
        Insert a image 
        """

        if not request.json:
            return jsonify( 
                {
                    'status':       'failed',
                    'action':       'POST',
                    'exception_msg':'not request json sent',
                    'status_code':  400
                }),400

        if not 'points' in request.json or not 'description' in request.json:
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


class TaskImageAPI(Resource):
    def __init__(self):
        pass

    def get(self,description):
        """ 
        Get one imagen 
        """

        image = dbmobile_images.get(description)
        if image is None:
            abort(404)

        return jsonify( { 'image': image.to_json() })

