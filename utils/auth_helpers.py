from flask import  request, Response
from functools import wraps
import jwt

def secured_route(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.headers.get('Authorization'):
            return Response('Unauthorized route', status=401, mimetype="application/json")    
        ##print(request.headers.get('Authorization'))
        token = request.headers.get('Authorization').split("Bearer")[1]
        user = jwt.decode(token, options={"verify_signature": False})
        print(user["role"])
        if "role" in user and not user["role"] == "admin":
            return Response('Unauthorized route', status=401, mimetype="application/json")   
        if "role" in kwargs:
            if kwargs["role"] == "admin" and not user["role"] == "admin":
                return Response('Unauthorized route', status=401, mimetype="application/json")   
        return f(*args, **kwargs)          
    return decorated_function  
