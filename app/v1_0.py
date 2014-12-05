# -*- coding: utf-8 -*-

from flask import Flask, Blueprint
import flask_restful

API_VERSION_V1_0=1.0
API_VERSION=API_VERSION_V1_0

api_v1_0_bp = Blueprint('api_v1_0', __name__)
api_v1_0 = flask_restful.Api(api_v1_0_bp)

class HelloWorld(flask_restful.Resource):
    def get(self):
        return {
                'hello': 'world',
                'version': API_VERSION,
            }

api_v1_0.add_resource(HelloWorld, '/helloworld')

