from flask import Response, request, jsonify
from functools import wraps

def bad_request(msg):  
    return Response(f"{msg}", status=403, mimetype='application/json')

def ok(result):  
    return jsonify(result), 200

def method_not_allowed(msg):  
    return Response(f"{msg}", status=405, mimetype='application/json')

def http_post(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.get_json():
            return bad_request("Post method is null or wrong format")
        return f(*args, **kwargs)          
    return decorated_function  
