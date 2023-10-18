import bcrypt
import json
import jwt

private_key = "qzdqazdp$*ihqjzdiopqzhndôuqizjdh"

def hash_password(password): 
    salt = bcrypt.gensalt() 
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def check_pw(pw, hashedpw):
    return bcrypt.checkpw(pw.encode('utf-8'), hashedpw.encode('utf-8'))

def generate_token(user):
    return jwt.encode(user.serialize(), private_key, algorithm="HS256")