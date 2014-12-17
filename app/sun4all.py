# -* coding: utf-8 -*-

from flask import jsonify, abort, request
from flask.ext.restplus import Resource, reqparse, fields
import json

from core import app, api, ns
import dbmobile_images
import dbmobile_points
from utilities import getRequestValues

point_fields = api.model('points', {
    'x': fields.Float,
    'y': fields.Float,
    'width': fields.Float
    })

image_fields = api.model('Image', {
        'description': fields.String,
        'browser': fields.String(required=False),
        'deleted': fields.String(required=False),
        'source_ip': fields.String(required=False),
        'points': fields.List(fields.Nested(point_fields)),
        'created': fields.DateTime
    })

class TaskImagesAPI(Resource):
    
    @api.doc(responses={404: 'Image not found'})
    @api.marshal_list_with(image_fields)
    def get(self):
        """ 
        Show all images
        """
        images = dbmobile_images.getall()

        if images is None:
            api.abort(404)

        return [ image.to_json() for  image in images]

image_parser = api.parser()
image_parser.add_argument('body', type=image_fields, required=True, help='The description of the image')

class TaskImageAPI(Resource):
    @api.doc(parser=image_parser)
    @api.doc(responses={400: 'Bad sending data'})
    @api.doc(responses={404: 'Image not save'})
    @api.marshal_with(image_fields)
    def post(self):
        """ 
        Save an image
        """
        if not request.json:
            return jsonify( 
                {
                    'status':       'failed',
                    'action':       'POST',
                    'exception_msg':'not request json sent',
                    'status_code':  400
                })

        if not 'description' in request.json:
            return jsonify( 
                {
                    'status':       'failed',
                    'action':       'POST',
                    'exception_msg':'description field Not Found',
                    'status_code':  400
                })
        
        get_server= getRequestValues(request)
        ip=None
        browser=None
        if get_server:
            if 'ip' in get_server:
                ip=get_server['ip']

            if 'browser' in get_server:
                browser=get_server['browser']
       
        image = dbmobile_images.init(
            ip=ip,
            browser=browser)

        image.from_json(request.json)
        dbmobile_images.add(image)                       

        if request.json['points']:
            for src in request.json['points']:
                point = dbmobile_points.init(
                    ip=ip,
                    browser=browser)
                point.images_id = image.id
                point.x = src['x']
                point.y = src['y']
                point.width = src['width']
                            
                dbmobile_points.add(point)     

        return image.to_json() 

class TaskImageAPI_byDescription(Resource):
    @api.doc(params={'description': 'The description of the image'})
    @api.doc(responses={404: 'Image not found'})
    @api.marshal_with(image_fields)
    def get(self,description):
        """ 
        Get one imagen 
        """
        image = dbmobile_images.get(description)
        if image is None:
            return jsonify( 
                {
                    'code':         1,
                    'message':      'Image not found',
                    'type':         'error'
                }), 404

        return image.to_json()
