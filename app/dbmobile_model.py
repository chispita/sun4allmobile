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
    description = Column(String)
    browser = Column(String)
    source_ip = Column(String)
    created = Column(DateTime)
    deleted = Column(DateTime)
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
    source_ip = Column(String)
    created = Column(DateTime)
    deleted = Column(DateTime)
    images_id = Column(Integer, ForeignKey('images.id'))
    #image = relationship(Images)

    def __repr__(self):
        return '<Points: %s-%s: x:%s, y:%s>' % (self.id, self.images_id,self.x,self.y)

'''
metadata = MetaData()

def now():
    return datetime.datetime.now()

images_table = Table('images', metadata,
    Column('id',             Integer, 
        Sequence('user_id', optional=True), primary_key=True),
    Column('description',    Integer,      default=u''),
    Column('browser',        Unicode(100), default=u''),
    Column('source_ip',      Unicode(15),  default=u''),
    Column('created',        TIMESTAMP(),  default=now()),
    Column('deleted',        TIMESTAMP(),  default=0)
)

points_table = Table('points', metadata,
    Column('id',             Integer, 
        Sequence('id', optional=True), primary_key=True),
    Column('images_id',      Integer,
        ForeignKey('images.id'), nullable=False),
    Column('x',              Float,        default=0),
    Column('y',              Float,        default=0),
    Column('browser',        Unicode(100), default=u''),
    Column('source_ip',      Unicode(15),  default=u''),
    Column('created',        TIMESTAMP(),  default=now()),
    Column('deleted',        TIMESTAMP(),  default=0)
)

    

# Options:
#  primary_key
#  foreign_key
#  sequence
#  unique=True -> To enforce UNIQUE constraints

# Create a class per table without data
class Images(object):
    def to_json(self):
        

        return str(self.Points)

        
        return { 
                "id"            : self.id,
                "description"   : self.description,
                "browser"       : self.browser,
                "source_ip"     : self.source_ip,
                "created"       : self.created,
                "deleted"       : self.deleted
                }
    def from_json(self,source):
        if 'id' in source:
            self.id = source['id']
        if 'description' in source:
            self.description = source['description']
        if 'delete' in source:
            self.delete = source['deleted']

    pass

class Points(object):
    pass

# Map the class with its table
#orm.mapper(Images, images_table, properties={
#    'points':orm.relation(Points, backref='images')
#})


orm.mapper(Images, images_table)
orm.mapper(Points, points_table)
'''
