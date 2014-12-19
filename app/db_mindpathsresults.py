#!/usr/bin/env python
from core import db
from model.mindpathsresults import MindPathsResults

def init(ip=None,browser=None):
    result=MindPathsResults()
    result.pair_id=None
    result.length=None
    result.words=None
    result.ids=None
    result.source_ip=ip
    result.browser=browser 
    return result

def add(result):
    db.session.add(result)
    db.session.commit()

def first():
    result=MindPathsResults.query.first()

def last():
    return MindPathsResults.query.last()

def remove(value):
     MindPathsResults.query.filter_by(id=value).delete()

def get(value):
    return MindPathsResults.query.filter_by(pair_id=value).first()

def getall():
    return MindPathsResults.query.all()
