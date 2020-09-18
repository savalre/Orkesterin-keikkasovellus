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
			session["active_state"] = users.active_state()[0]
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

@app.route("/userinfo",methods=["get","post"])
def userinfo():
		soitin = users.get_soitin()
		tila = users.active_state()
		return render_template("userinfo.html", instrument = soitin, state=tila)

@app.route("/edit_user",methods=["get","post"])
def edit_user():
	soittimet = soitin.get_soittimet()
	print(soittimet)
	return render_template("edit_user.html", soitin=soittimet)
	
@app.route("/userUpdated", methods=["post"])
def userUpdated():
	uusitila = request.form["active"]
	soitinvalinta = request.form["soitin"]
	print("sain tiedon:",uusitila, "ja soitinvalinta on: ", soitinvalinta)
	users.muutatila(uusitila)
	users.muutasoitin(soitinvalinta)
	return render_template("update.html", message="Profiilisi on päivitetty!")

