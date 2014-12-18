# -* coding: utf-8 -*-

from flask import jsonify, abort, request
from flask.ext.restplus import Resource, fields
from core import app, api
import json

import db_cellresults
import db_cellmarks
from utilities import getRequestValues

mark_fields = api.model('cellmarks', {
    'x': fields.Integer,
    'y': fields.Integer,
    'typeofmarking': fields.Float
})

cell_fields = api.model('cells', {
    'image_name' : fields.String(), 
    'browser': fields.String(required=False),
    'deleted': fields.String(required=False),
    'source_ip': fields.String(required=False),
    'cellmarks': fields.List(fields.Nested(mark_fields)),
    'created': fields.DateTime
    })

class TaskCellsAPI(Resource):
    def __init__(self):
        pass

    @api.doc(responses={404: 'Cell not found'})
    @api.marshal_list_with(cell_fields)
    def get(self):
        """ 
        Show all results
        """
        results = db_cellresults.getall()

        if results is None:
            abort(404)

        return [result.to_json() for result in results]

    def post(self):
        """ 
        Save a result 
        """

        if not request.json:
            return jsonify( 
                {
                    'status':       'failed',
                    'action':       'POST',
                    'exception_msg':'not request json sent',
                    'status_code':  400
                }),400


        if not 'image_name' in request.json:
            return jsonify( 
                {
                    'status':       'failed',
                    'action':       'POST',
                    'exception_msg':'image_name field Not Found',
                    'status_code':  400
                }),400

        if not 'marks' in request.json:
            return jsonify( 
                {
                    'status':       'failed',
                    'action':       'POST',
                    'exception_msg':'marks field Not Found',
                    'status_code':  400
                }),400

        get_server= getRequestValues(request)
        ip=None
        browser=None
        if get_server:
            if 'ip' in get_server:
                ip=get_server['ip']
            if 'browser' in get_server:
                browser=get_server['browser']
        
        result = db_cellresults.init(
            ip=ip,
            browser=browser)
        result.from_json(request.json)
        db_cellresults.add(result)                       

        if request.json['marks']:
            for src in request.json['marks']:
                mark = db_cellmarks.init(
                    ip=ip,
                    browser=browser)
                mark.result_id = result.id
                mark.typeofmarking = src['typeofmarking']
                mark.x = src['x']
                mark.y = src['y']
        
                db_cellmarks.add(mark)            

        return result.to_json()
