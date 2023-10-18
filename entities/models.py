from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    role =  db.Column(db.String(50), nullable=False)
    def __init__(self,email, password):
        self.email = email
        self.password = password
        self.role = "admin"

    def __str__(self) -> str:
        return f'{self.email}'
    
    def serialize(self):
        return {"email": self.email, "role" : self.role}
