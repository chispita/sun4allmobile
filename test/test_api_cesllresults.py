#!/usr/bin/python
# -*- coding: utf-8 -*-

from app.web import app
import unittest
import json
import requests
from default import init_db

class APITestCellResults(unittest.TestCase):

    def setUp(self):
        self.test_app = app.test_client()
    
    def test_01_Get_CellResults(self):
        response = self.test_app.get('/api/cellresults')
        assert 200 == response.status_code
    
    def test_02_Add_CellImage(self):
        data = { 'image_name1': 'zoe'}

        res = self.test_app.post(
            '/api/cellresults',
            data=json.dumps(data),
            headers = { 'Content-type': 'application/json',  'Accept': 'text/plain'} 
            )

        err = json.loads(res.data)

        err_msg = "AddImage excepcion grabando la imagen"

        print res.status_code
        assert 200 == res.status_code, err_msg

