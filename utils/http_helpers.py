from flask import Response, request
from functools import wraps

def bad_request(msg):  
    return Response(f"{msg}", status=403, mimetype='application/json')

def method_not_allowed(msg):  
    return Response(f"{msg}", status=405, mimetype='application/json')

def http_post(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.get_json():
            return bad_request("Post method is null or wrong format")
        return f(*args, **kwargs)          
    return decorated_function  



class Result:
    is_failure : bool
    result : object
    error_message : str

    def __init__(self, is_failure, result, error_message) -> None:
        self.is_failure = is_failure
        self.error_message = error_message
        self.result = result

    def success(obj:object):
        return Result(False, obj, None)