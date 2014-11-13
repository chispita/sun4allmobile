#!/usr/bin/python
import dbmobile_model

from config import database
from sqlalchemy import orm
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dbmobile_model import Base, Images, Points

connection_string ="mysql://%s:%s@%s/%s" % (
    database['user'], 
    database['pass'],
    database['server'],
    database['name'])

engine = create_engine(connection_string, echo=True)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
session = DBSession()



#image = session.query(Images).filter_by(id=1).first()

'''
qry = session.query(Images)\
    .join(Images.points)\
    .filter(Images.id==1)\
    .filter( Points.id==4)\
    .one()

#image = session.query(Images).filter(Images.id==1, Points.images_id==3).first()


if qry:
    print 'image  : %s' % qry
    #print 'points : %s' % qry.points

    #print 'point: %s'% image.points
    #print 'id:%s,-> image_id: %s, x:%s, y:%s' % ( image.points[0].id, image.points[0].images_id,image.points[0].x, image.points[0].y)
'''
