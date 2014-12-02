#!/usr/bin/env python
from dbmobile_conn import session
from dbmobile_model import Images, Points


def test01():
    '''
    Test to check query to description
    '''
    qry = session.query(Images)\
        .filter_by(description='carlos11')\
        .first()

    if qry:
        print qry


def test02():

    user = dict(
                id=1, 
                fullname=2,
                name=3)

    return user



if __name__ == '__main__':
    print test02()
