import imp
from flask import Flask

# Here we make our Flask server, and bring all files together
app = Flask(__name__)

from app import database
from app import views
from app import UsersAPI

