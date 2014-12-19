#!/usr/bin/env python
from app.core import db
from model.images import Images

def init(ip=None,browser=None):
    image=Images()
    image.browser=browser
    image.source_ip=ip  
    return image

def add(image):
    db.session.add(image)
    db.session.commit()

def first():
    image=Images.query.first()

def last():
    return Images.query.last()

def remove(value):
     Images.query.filter_by(id=value).delete()

def get(value):
    return Images.query.filter_by(description=value).first()

def getall():
    return Images.query.all()
