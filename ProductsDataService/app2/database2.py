from app2 import app
from flask_sqlalchemy import SQLAlchemy

# Making SQLite database for storage Motorcycles
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///motorcycle_database.db'
app.config['SECRET_KEY'] = 'password'

# Making class of table Motorcycle
class Motorcycle(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    power = db.Column(db.String(80), nullable=False)
    torque = db.Column(db.String(80), nullable=False)
    dry_weight = db.Column(db.String(80), nullable=False)
    img_url = db.Column(db.String(200), nullable=False)


    def __init__(self, id, name, power, torque, dry_weight, img_url):
        self.id = id
        self.name = name
        self.power = power
        self.torque = torque
        self.dry_weight = dry_weight
        self.img_url = img_url
