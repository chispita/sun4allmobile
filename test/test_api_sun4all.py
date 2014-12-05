#!/usr/bin/python
# -*- coding: utf-8 -*-

from app.web import app
import unittest
import json
import requests
#from bs4 import BeautifulSoup

from default import init_db

class APITestSun4All(unittest.TestCase):

    def setUp(self):
        self.test_app = app.test_client()
    
    def test_00_Home(self):
        data = json.loads(self.test_app.get().data)

        assert data.get('version') == 1
        assert data.get('hello') == 'Hello socientize api'       

    def test_01_Get_Images(self):
        url = '/api/image'
        res = self.test_app.get( url )
        assert 200 == res.status_code

    def test_02_Add_Image(self):
        data = {'description': 'zoe', 
                'points':'99'}

        data['points'] = []
        point = {'x' : 1,
                 'y' : 2}
        data['points'].append( point)
        point = {'x' : 1.1,
                 'y' : 2.3}
        data['points'].append( point)
        
        url = '/api/image'

        res = self.test_app.post(
            url, 
            data=json.dumps(data),
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'} 
            )

        err_msg = "AddImage excepcion grabando la imagen"

        
        assert 200 == res.status_code, err_msg
    
    def test_03_Get_Image_NonExists(self):
        self.test_app = app.test_client()

        url = '/api/images/%s' % '75252'
        res = self.test_app.get( url )

        err_msg = "Image_NonExits  excepcion buscando una imagen inexistente"
        assert 404 == res.status_code, err_msg

