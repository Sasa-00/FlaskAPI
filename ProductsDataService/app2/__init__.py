from flask import Flask

# Here we make our Flask server, and bring all files together
app = Flask(__name__)

from app2 import BikeAPI
from app2 import views
from app2 import database2
