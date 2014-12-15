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

