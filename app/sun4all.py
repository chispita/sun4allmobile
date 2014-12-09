# -*- coding: utf-8 -*-

from flask import jsonify, abort, request
from flask.ext.restful import Resource
import json

import dbmobile_images
import dbmobile_points

#@api.route('/api/image', endpoint='tasks')
class TaskImagesAPI(Resource):
    def __init__(self):
        pass

    #@api.doc(responses={404: 'Doesn\'t exist'})
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

    #@api.doc(responses={400: 'not request json sent'})
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

        if not 'description' in request.json:
            return jsonify( 
                {
                    'status':       'failed',
                    'action':       'POST',
                    'exception_msg':'description field Not Found',
                    'status_code':  400
                }),400
        
        image = dbmobile_images.init()
        image.from_json(request.json)
        dbmobile_images.add(image)                       

        if request.json['points']:
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

    def post(self):
        pass


