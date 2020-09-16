from app import app
from flask import render_template, request, redirect, session
import users, db, soitin

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login",methods=["get","post"])
def login():
    if request.method == "GET":
        return render_template("/")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            session["username"] = username
            session["active_state"] = users.active_state()
            return redirect("/")
        else:
            return render_template("error.html",message="Väärä käyttäjätunnus tai salasana!")

@app.route("/logout")
def logout():
	del session["user_id"]
	return redirect("/")

@app.route("/register",methods=["get","post"])
def register():
	if request.method == "GET":
		return render_template("register.html")
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		if users.register(username,password):
			return redirect("/")
		else:
			return render_template("error.html",message="Rekisteröinti ei onnistunut")

@app.route("/userinfo",methods=["get"])
def userinfo():
	return render_template("userinfo.html")
