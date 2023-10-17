from flask import  request, Response
from functools import wraps

def secured_route(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.headers.get('Authorization'):
            return Response('Unauthorized route', status=401, mimetype="application/json")      
        ## check des privileges 
        return f(*args, **kwargs)          
    return decorated_function  
