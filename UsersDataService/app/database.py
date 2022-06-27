from app import app
from flask_sqlalchemy import SQLAlchemy


# Making SQLite database for storage Users
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'password'

# Making class of table User
class User(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password

