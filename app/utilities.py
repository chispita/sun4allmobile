# -* coding: utf-8 -*-

def getRequestValues(request):
    '''
    Get Values from request
    '''
    try:
        result=(dict(
            ip=request.headers['X-Forwarded-For'],
            browser=request.headers['User-Agent']))
    except:
        result=None

    return result

