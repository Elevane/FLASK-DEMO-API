from flask import Flask, request, jsonify
from utils.http_helpers import *
from utils.auth_helpers import *
from flask_sqlalchemy import SQLAlchemy
from utils.security_helpers import *
from entities.models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost/rspublisher'
db.init_app(app)



@app.route('/login', methods=["POST"])
@http_post
def login():
    data = request.get_json()
    existing_user = User.query.filter_by(email=data["email"]).first()
    if not existing_user:
        return bad_request(f'Wrong credentials.')
    good_password = check_pw(data["password"], existing_user.password)
    if not good_password:
        return bad_request(f'Wrong credentials .')
    token = generate_token(existing_user)
    return ok({"jwt_token" : token})

@app.route('/register', methods=["POST"])
def register():
    data = request.get_json()
    new_user = User(email=data["email"], password=hash_password(data["password"]))
    db.session.add(new_user)
    db.session.commit()
    token = generate_token(new_user)
    return ok({"jwt_token" : token})

@app.route('/', methods=["GET"])
@secured_route
def home():
    return 'secured route'


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
    




