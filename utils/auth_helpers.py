from flask import  request, Response, session
from functools import wraps
import jwt
import os
import datetime

SECRET_KEY = os.getenv("SECURITY_SCRRRT_KEY")

def secured_route(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.headers.get('Authorization'):
            return Response('Unauthorized route', status=401, mimetype="application/json")    
        ##print(request.headers.get('Authorization'))
        token = request.headers.get('Authorization').split("Bearer")[1]
        data = jwt.decode(jwt=token, key=SECRET_KEY, options={"verify_signature": False})
        print(data["user"]["role"])
        if "role" in data["user"] and not data["user"]["role"] == "admin":
            return Response('Unauthorized route', status=401, mimetype="application/json")   
        if "role" in kwargs:
            if kwargs["role"] == "admin" and not data["user"]["role"] == "admin":
                return Response('Unauthorized route', status=401, mimetype="application/json")
        if not data["expiration_date"] and datetime.fromisoformat( data["expiration_date"]) < datetime.now():
            return Response('Unauthorized route : The expiration date has passed', status=401, mimetype="application/json")
        session["user"] = data["user"]
        return f(*args, **kwargs)          
    return decorated_function  
