from app2 import app
from flask import jsonify, json, redirect, session, url_for, request
from app2.database2 import Motorcycle, db
import json
import requests

# adding SECRET KEY for session
app.config["SECRET_KEY"] = "fdsfsdvfgAFAadvvfgA"

# API service for getting all motorcycles from database
@app.route('/getmotorcycle', methods=['GET'])
def getmotorcycle():
     if request.method == 'GET':
          all_motorcycles = []
          # Taking all records from table
          motorcycles = Motorcycle.query.all()
          # Looping through list of records
          for motorcycle in motorcycles:
               results = {
                         "id": motorcycle.id,
                         "name": motorcycle.name,
                         "power": motorcycle.power,
                         "torque": motorcycle.torque,
                         "dry_weight": motorcycle.dry_weight,
                         "img_url": motorcycle.img_url
                         }
               # Appending individually record to list
               all_motorcycles.append(results)

          return jsonify(
               all_motorcycles
          )
     else:
          return jsonify({"Error": "Unallowed Method"})


# API service for posting new record into motorcycle table
@app.route("/newmotorcycle", methods=['POST'])
def newmotorcycle():
     if request.method == 'POST':
          # Taking json from body
          input = request.get_json()
          # Making instance of new Motorcycle class, with new attributes
          motorcycle = Motorcycle(id = input["id"], name = input["name"], power = input["power"], torque = input["torque"], 
          dry_weight = input["dry_weight"], img_url = input["img_url"])

          # Adding it to table
          db.session.add(motorcycle)
          db.session.commit()
          return jsonify({"result": "Successfully added to dict"})
     else:
          return jsonify({"Error": "Unallowed Method"})


# API service to delete specific record by ID
@app.route("/deletemotorcycle/<int:id>", methods=['DELETE'])
def deletemotorcycle(id):

     if request.method == 'DELETE':
          # Finding record with same id as out input
          motorcycle_to_delete = Motorcycle.query.get_or_404(id)

          try:
               # If exists, we are deleting it
               db.session.delete(motorcycle_to_delete)
               db.session.commit()
               return jsonify({"result": "Motorcycle DELETED successfully"})

          except:
               return jsonify({"result": "There was a problem..."})
     else:
          return jsonify({"Error": "Unallowed Method"})


# API service to update table, with specific ID
@app.route("/updatemotorcycle/<int:id>", methods=['PUT'])
def updatemotorcycle(id):

     if request.method == 'PUT':
          # Finding record with same id as out input
          motorcycle_to_update = Motorcycle.query.get_or_404(id)
          input = request.get_json()

          # In next few IF statements, we are checking what is in POST method body
          if "name" in input:
               motorcycle_to_update.name = input["name"]
          if "power" in input:
               motorcycle_to_update.power = input["power"]
          if "torque" in input:
               motorcycle_to_update.torque = input["torque"]
          if "dry_weight" in input:
               motorcycle_to_update.dry_weight = input["dry_weight"]
          if "img_url" in input:
               motorcycle_to_update.img_url = input["img_url"]
          
          try:
               # Changing it
               db.session.commit()
               return jsonify({"result": "Motorcycle UPDATED successfully"})
          
          except:
               return jsonify({"result": "There was a problem..."})
     else:
          return jsonify({"Error": "Unallowed Method"})


# This route is for getting user name from another server, but because of some problem with Docker and this response lib, i just skipped this part.
# But this will work if this project start on two different CMD on local machine (start run.py on first, and run2.py on second).
# In this case, only change in code will be, instead redirect('http://127.0.0.1:5001/home') in
# UsersApi, there should be redirect('http://127.0.0.1:5001/ruta'), and all will perfect work.

@app.route("/ruta")
def get_users():
     # Specifying what is URL of another server
     url = "http://127.0.0.1:5000/get_user"

     # Taking data that first server passed to this one
     response = requests.get(url)
     data = response.content
     dict = json.loads(data)

     # Here we expecting user name and after making session
     user = dict["user"]
     session["USERNAME"] = user

     # Redirecting to our product page
     return redirect(url_for("home"))

# Route to sign out and go back to our first FLASK server (Login page)
@app.route("/sign-out")
def sign_out():

     session.pop("USERNAME", None)

     return redirect('http://127.0.0.1:5000/')
