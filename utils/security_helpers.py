import bcrypt

def hash_password(password):
    private_key = "qzdqazdp$*ihqjzdiopqzhndôuqizjdh"
    salt = bcrypt.gensalt()
    
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def check_pw(pw, hashedpw):
    return bcrypt.checkpw(pw.encode('utf-8'), hashedpw.encode('utf-8'))