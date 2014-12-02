from flask import jsonify, abort, request
from flask.ext.restful import Resource

import json

import dbmobile_mindpathsresults

class TaskMindPathsAPI(Resource):
    def __init__(self):
        pass

    def get(self):
        """ 
        Show all results
        """

        results = dbmobile_mindpathsresults.getall()

        if results is None:
            abort(404)

        results_array = []
        for result in results:
            results_array.append(result.to_json())

        return jsonify( { 'results':  results_array } )


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

        result = dbmobile_mindpathsresults.init()
        result.from_json(request.json)
        dbmobile_mindpathsresults.add(result)                       

        return jsonify( { 'result': result.to_json() } )

