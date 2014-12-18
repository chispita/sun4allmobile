# -*- coding: utf8 -*-
from flask import jsonify, abort, request
from flask.ext.restplus import Resource, fields

import json
from core import app,api
import db_mindpathsresults
from utilities import getRequestValues

mind_fields = api.model('minds', {
    'pair_id' : fields.Integer,
    'length' : fields.String,
    'words' : fields.String,
    'ids' : fields.String,
    'deleted': fields.String(required=False),
    'source_ip': fields.String(required=False),
    'browser': fields.String(required=False),
    'created': fields.DateTime
})

mind_parser = api.parser()
mind_parser.add_argument('body', type=mind_fields, required=True, help='The description of the image')

class TaskMindPathsAPI(Resource):
    def __init__(self):
        pass

    @api.doc(responses={404: 'MindPath not found'})
    @api.marshal_list_with(mind_fields)
    def get(self):
        """ 
        Show all results
        """
        results = db_mindpathsresults.getall()

        if results is None:
            abort(404)

        results_array = []
        for result in results:
            results_array.append(result.to_json())

        return [ result.to_json() for  result in results]

    @api.doc(parser=mind_parser)
    @api.doc(responses={400: 'Bad sending data'})
    @api.marshal_with(mind_fields)
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


        if not 'pair_id' in request.json:
            return jsonify( 
                {
                    'status':       'failed',
                    'action':       'POST',
                    'exception_msg':'pair_id field Not Found',
                    'status_code':  400
                }),400

        if not 'length' in request.json:
            return jsonify( 
                {
                    'status':       'failed',
                    'action':       'POST',
                    'exception_msg':'length field Not Found',
                    'status_code':  400
                }),400

        if not 'words' in request.json:
            return jsonify( 
                {
                    'status':       'failed',
                    'action':       'POST',
                    'exception_msg':'words field Not Found',
                    'status_code':  400
                }),400

        if not 'ids' in request.json:
            return jsonify( 
                {
                    'status':       'failed',
                    'action':       'POST',
                    'exception_msg':'ids field Not Found',
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

        result = db_mindpathsresults.init(
            ip=ip,
            browser=browser)
        result.from_json(request.json)
        db_mindpathsresults.add(result)                       

        return result.to_json()

