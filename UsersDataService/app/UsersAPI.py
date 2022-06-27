from app import app
from flask import request, redirect, flash, url_for, jsonify, session
from app.database import db, User



# Registration, back-end side
@app.route("/register_check", methods = ['POST'])
def register_check():

     # Bringing inputs from HTML form
     input = request.form.to_dict()
    # Separating inputs
     input_email = input['email']
     input_password = input['password']
     input_repassword = input['re-password']

     # Checking if passwords are the same
     if input_password != input_repassword:
          flash("Please, Enter the password correctly!", "error")
          return redirect(url_for("register"))
        
     else:
          # If all alright, adding records to table
          user = User(id=int(User.query.count()), email=input_email, password=input_password)
          db.session.add(user)
          db.session.commit()

          flash("You have been registered succesfully! Please Log In", "info")
          return redirect(url_for("login"))



# Logging in, back-end side
@app.route("/login_check", methods = ['POST'])
def login_check():

     # Bringing inputs from HTML form
     input = request.form.to_dict()
     # Separating inputs
     input_email = input['email']
     input_password = input['password']

     # Query to take all records from table User
     users = User.query.all()

     # for loop to check if the email and password match with the pair in the table
     for user in users:
          if str(input_email) == str(user.email) and str(input_password) == str(user.password):

               # Making varibale usser global because we reuse it in /get_user route
               global usser
               # We want only part that is next to @ sign
               usser = (user.email).split("@")[0]

               # Redirecting our application to another Flask server
               return redirect('http://127.0.0.1:5001/home')
          else:
               pass
     # Going back because of wrong input
     flash("Wrong email or password!", "error")
     return redirect(url_for("login"))


# API route for getting all users from table
@app.route('/getusers', methods=['GET'])
def getusers():
     if request.method == 'GET':
          all_users = []
          # Taking all records from table
          users = User.query.all()
          # Looping through list of records
          for user in users:
               results = {
                         "id": user.id,
                         "email": user.email,
                         "password": user.password
                         }
               # Appending individually record to list
               all_users.append(results)

          return jsonify(
               all_users
          )
     else:
          return jsonify({"Error": "Unallowed Method"})


# API route for deleting specific user from table by ID
@app.route("/deleteuser/<int:id>", methods=['DELETE'])
def deleteuser(id):

     if request.method == 'DELETE':
          # Finding record with same id as out input
          user_to_delete = User.query.get_or_404(id)

          try:
               # If exists, we are deleting it
               db.session.delete(user_to_delete)
               db.session.commit()
               return jsonify({"result": "User DELETED successfully"})

          except:
               return jsonify({"result": "There was a problem..."})
     else:
          return jsonify({"Error": "Unallowed Method"})

# Forwarding usser variable to another Flask server
@app.route("/get_user", methods = ['GET'])
def get_user():

        return jsonify({"user": usser})