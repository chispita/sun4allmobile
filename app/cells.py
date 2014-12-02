from flask import jsonify, abort, request
from flask.ext.restful import Resource

import json

import dbmobile_cellresults
import dbmobile_cellmarks

class TaskCellsAPI(Resource):
    def __init__(self):
        pass

    def get(self):
        """ 
        Show all results
        """

        results = dbmobile_cellresults.getall()

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
        
        result = dbmobile_cellresults.init()
        result.from_json(request.json)
        dbmobile_cellresults.add(result)                       

        if request.json['marks']:
            for src in request.json['marks']:
                mark = dbmobile_cellmarks.init()
                mark.result_id = result.id
                mark.typeofmarking = src['typeofmarking']
                mark.x = src['x']
                mark.y = src['y']
        
                dbmobile_cellmarks.add(mark)            

        return jsonify( { 'result': result.to_json() } )

