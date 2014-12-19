#!/usr/bin/python

import json
from app.core import db
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

