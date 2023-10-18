import bcrypt
import json
import jwt
import datetime
import os


SECRET_KEY = os.getenv("SECURITY_SCRRRT_KEY")


def hash_password(password): 
    salt = bcrypt.gensalt() 
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def check_pw(pw, hashedpw):
    return bcrypt.checkpw(pw.encode('utf-8'), hashedpw.encode('utf-8'))

def generate_token(user):
    exp_date =datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=1)
    token_data = {
        "user" : user.serialize(),
        "expiration_date" : exp_date.isoformat()
    } 
    return jwt.encode(token_data, key=SECRET_KEY, algorithm="HS256")