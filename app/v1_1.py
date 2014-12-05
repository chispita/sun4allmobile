# -*- coding: utf-8 -*-

from flask import Flask, Blueprint
import flask_restful

API_VERSION_V1_1=1.1
API_VERSION=API_VERSION_V1_1

api_v1_1_bp = Blueprint('api_v1_1', __name__)
api_v1_1 = flask_restful.Api(api_v1_1_bp)

class HelloWorld(flask_restful.Resource):
    def get(self):
        return {
                'hello': 'world',
                'version': API_VERSION,
            }

api_v1_1.add_resource(HelloWorld, '/helloworld')

