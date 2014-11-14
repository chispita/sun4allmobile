#!/usr/bin/python

from sqlalchemy.ext.declarative import declarative_base
from flask.ext.jsontools import JsonSerializableBase
from sqlalchemy import orm
import datetime
from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.types import Integer,Unicode,TIMESTAMP,Float
from sqlalchemy.schema import MetaData, Sequence
from sqlalchemy.orm import relationship


Base = declarative_base()


class Images(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key = True)
    description = Column(String, nullable=False)
    browser = Column(String, default='')
    source_ip = Column(String, default='')
    created = Column(DateTime)
    deleted = Column(DateTime, default=0)
    points = relationship('Points')

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
                image['points'].append({ 'x':point.x, 'y':point.y})

        return image


    def from_json(self,source):
        if 'id' in source:
            self.id = source['id']
        if 'description' in source:
            self.description = source['description']
        if 'delete' in source:
            self.delete = source['deleted']


class Points(Base):
    __tablename__ = 'points'
    id = Column(Integer, primary_key = True)
    x = Column(Integer)
    y = Column(Integer)
    source_ip = Column(String, default='')
    created = Column(DateTime)
    deleted = Column(DateTime, default=0)
    images_id = Column(Integer, ForeignKey('images.id'))

    def __repr__(self):
        return '<Points: %s-%s: x:%s, y:%s>' % (self.id, self.images_id,self.x,self.y)

