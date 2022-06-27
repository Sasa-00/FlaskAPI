from urllib import response
from app import app
from flask import render_template, Response, flash

# Rendering template for registration page
@app.route("/register")
def register():
        return render_template('register.html')
    

# Rendering template for login/first page
@app.route("/")
def login():
    return render_template('index.html')

