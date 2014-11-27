import unittest
import json
import requests
from bs4 import BeautifulSoup
#from app import views

from app.views import app
from default import init_db


SERVER_URL = "http://sun4allmobile.socientize.eu"

class WebServiceTestCase(unittest.TestCase):


    def test_00_Home(self):
        self.test_app = app.test_client()

        # Asert response is 200 OK
        res = self.test_app.get()

        dom = BeautifulSoup(res.data)

        print 'DATOS:' + res.status
        print 'BEAU' + str(dom)

        assert 200 == res.status_code

    '''
    def test_01_Get_Images(self):
        self.test_app = app.test_client()

        url = '/api/images'
        res = self.test_app.get( url )

        assert 200 == res.status_code
    '''

    def test_02_Add_Image(self):
        self.test_app = app.test_client()

        #num_images = len(images)

        url = '/api/images'

        data = { 
                    'description': 'zoe', 
                    'points':'99'}

        data['points'] = []
        point = { 
                    'x' : 1,
                    'y' : 2}

        data['points'].append( point)

        point = { 
                    'x' : 1.1,
                    'y' : 2.3}

        data['points'].append( point)
        
        print data

        res = self.test_app.post(
            url, 
            data=json.dumps(data),
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'} 
            )

        #err = json.loads(res.data)
        err_msg = "AddImage excepcion grabando la imagen"

        
        assert 200 == res.status_code, err_msg
        #assert err['image']['description'] ==  data['description']
        

        #assert 
        #dom = BeautifulSoup(res.data)

    '''
    def test_03_Get_Image_NonExists(self):
        self.test_app = app.test_client()

        url = '/api/images/%s' % '75252'
        res = self.test_app.get( url )

        err_msg = "Image_NonExits  excepcion buscando una imagen inexistente"
        assert 404 == res.status_code, err_msg

    def test_04_Get_Image_Exits(self):
        self.test_app = app.test_client()

        url = '/api/images/%s' % 'carlos11'
        res = self.test_app.get( url )

        assert 200 == res.status_code
    '''
