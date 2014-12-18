#!/usr/bin/python

import json
from core import db
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy  import Integer,String, DateTime,Float

class Images(db.Model):
    __tablename__ = 'images'
    id = db.Column(Integer, primary_key = True)
    description = Column(String, nullable=False)
    browser = Column(String(100), default='')
    source_ip = Column(String, default='')
    created = Column(DateTime)
    deleted = Column(DateTime, default=0)
    points = relationship('Points', cascade='all, delete, delete-orphan', backref='images')

    def __repr__(self):
        return '<Imagen: %s-%s>' % (self.id, self.description)

    def to_json(self):
        image = { 
                'id'            : self.id,
                'description'   : self.description,
                'browser'       : self.browser,
                'source_ip'     : self.source_ip,
                'created'       : self.created,
                'deleted'       : self.deleted
                }
        
        if self.points:
            image['points']=[]
            for point in self.points:
                image['points'].append({ 'x':point.x, 'y':point.y, 'width':point.width})

        return image
    
    def from_json(self,source):
        if 'id' in source:
            self.id = source['id']
        if 'description' in source:
            self.description = source['description']
        if 'delete' in source:
            self.delete = source['deleted']

class Points(db.Model):
    __tablename__ = 'points'
    id = Column(Integer, primary_key = True)
    x = Column(Float(precision=2), default=0)
    y = Column(Float(precision=2), default=0)
    width = Column(Float(precision=2), default=0)
    browser = Column(String(100), default='')
    source_ip = Column(String, default='')
    created = Column(DateTime)
    deleted = Column(DateTime, default=0)
    images_id = Column(Integer, ForeignKey('images.id'), nullable=False)

    def __repr__(self):
        return '<Points: %s-%s: x:%s, y:%s, width:%s>' % (self.id, self.images_id,self.x,self.y,self.width)

class CellResults(db.Model):
    __tablename__ = 'cellresults'
    id = Column(Integer, primary_key = True)
    image_name = Column(String, nullable=False)
    browser = Column(String, default='')
    source_ip = Column(String, default='')
    created = Column(DateTime)
    deleted = Column(DateTime, default=0)
    cellmarks = relationship('CellMarks', cascade='all, delete, delete-orphan', backref='cellresults')

    def __repr__(self):
        return '<Cell Result: %s-%s>' % (self.id, self.image_name)

    def to_json(self):
        result = { 
                'id'            : self.id,
                'image_name'      : self.image_name,
                'browser'       : self.browser,
                'source_ip'     : self.source_ip,
                'created'       : self.created,
                'deleted'       : self.deleted
                }
        
        
        if self.cellmarks:
            result['cellmarks']=[]
            for mark in self.cellmarks:
                result['cellmarks'].append({ 'typeofmarking': mark.typeofmarking, 'x':mark.x, 'y':mark.y})

        return result
    
    def from_json(self,source):

        if 'id' in source:
            self.id = source['id']
        if 'image_name' in source:
            self.image_name = source['image_name']
        if 'deleted' in source:
            self.deleted = source['deleted']

class CellMarks(db.Model):
    __tablename__ = 'cellmarks'
    id = Column(Integer, primary_key = True)
    typeofmarking = Column(db.Integer)
    x = Column(Integer)
    y = Column(Integer)
    source_ip = Column(String, default='')
    created = Column(DateTime)
    deleted = Column(DateTime, default=0)
    result_id = Column(Integer, ForeignKey('cellresults.id'), nullable=False)

    def __repr__(self):
        return '<CellMarks: %s-%s: typeofmarking:%s x:%s, y:%s>' % (self.id, self.result_id,self.typeofmarking,self.x,self.y)

class MindPathsResults(db.Model):
    __tablename__ = 'mindpathsresults'
    id = Column(Integer, primary_key = True)
    pair_id = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    words = Column(String, nullable=False)
    ids = Column(String, nullable=False)
    browser = Column(String, default='')
    source_ip = Column(String, default='')
    created = Column(DateTime)
    deleted = Column(DateTime, default=0)

    def __repr__(self):
        return '<Mind Paths Result: %s-%s-%s>' % (self.id, self.pair_id, self.words)

    def to_json(self):
        result = { 
                'id'            : self.id,
                'pair_id'       : self.pair_id,
                'length'        : self.length,
                'words'         : self.words,
                'ids'           : self.ids,
                'browser'       : self.browser,
                'source_ip'     : self.source_ip,
                'created'       : self.created,
                'deleted'       : self.deleted
                }
        
        return result

    def from_json(self,source):

        if 'id' in source:
            self.id = source['id']
        if 'pair_id' in source:
            self.pair_id = source['pair_id']
        if 'length' in source:
            self.length = source['length']
        if 'words' in source:
            self.words = json.dumps(source['words'])
        if 'ids' in source:
            self.ids = json.dumps(source['ids'])
        if 'deleted' in source:
            self.deleted = source['deleted']
