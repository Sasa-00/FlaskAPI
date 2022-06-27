from app2 import app
from flask import render_template, session

# Route for main product page
@app.route("/home")
def home():

    # Checking if session exists
    if "USERNAME" in session:
        user = session["USERNAME"]
        # Rendering product page and forwarding user session name
        return render_template('korisnik.html',user = user)
    # Only rendering HTML product template
    return render_template('korisnik.html')
