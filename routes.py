from app import app
from flask import render_template, request, redirect, session
import users, db, soitin, keikka

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
		if users.login(username,password1):
			session["username"] = username
			session["user_id"] = users.user_id()
			session["active_state"] = users.active_state()[0]
			return redirect("/")
		else:
			return render_template("error.html",message="Väärä käyttäjätunnus tai salasana :(")

@app.route("/logout", methods=["get"])
def logout():
	users.logout()
	return redirect("/")

@app.route("/register",methods=["get","post"])
def register():
	if request.method == "GET":
		return render_template("register.html")
	if request.method == "POST":
		username = request.form["username"]
		password1 = request.form["password1"]
		password2 = request.form["password2"]
		if password1 == password2:
			if users.register(username,password1):
				session["username"] = username
				return redirect("/")
			else:
				return render_template("error.html",message="Hups, rekisteröinti ei onnistunut!")
		else: 
			return render_template("error.html",message="Salasanat eivät ole samat! Sosselisos")
		
@app.route("/userinfo",methods=["get","post"])
def userinfo():
		soitin = users.get_soitin()
		tila = users.active_state()
		return render_template("userinfo.html", instrument = soitin, state=tila)

@app.route("/edit_user",methods=["get","post"])
def edit_user():
	return render_template("edit_user.html")
	
@app.route("/userUpdated", methods=["post"])
def userUpdated():
	uusitila = request.form["active"]
	soitinvalinta = request.form["soitin"]
	print("sain tiedon:",uusitila, "ja soitinvalinta on: ", soitinvalinta)
	users.muutatila(uusitila)
	users.muutasoitin(soitinvalinta)
	return render_template("update.html", message="Profiilisi on päivitetty!")

@app.route("/keikkasivu")
def keikkasivu():
	lista = keikka.keikkaLista()
	return render_template("keikka.html", keikat=lista)
	
@app.route("/newGig")
def uusi_keikka():
	return render_template("addgig.html")

@app.route("/gigAdd",methods=["post"])
def gigAdd():
	nimi = request.form["nimi"]
	pvm = request.form["pvm"]
	time = request.form["aika"]
	paikka = request.form["paikka"]
	kuvaus = request.form["kuvaus"]
	kokoonpano = request.form["kokoonpano"]
	print("Keikkaa lisätään seuraavilla tiedoilla: ", nimi, pvm, time, paikka, kuvaus, kokoonpano)
	if keikka.lisaaKeikka(nimi,pvm,time,paikka,kuvaus,kokoonpano):
		return render_template("gigUpdate.html",message="Keikka lisätty onnistuneesti!")
	else:
		return render_template("error.html",message="Oho, jotain meni pieleen eikä keikkaa luotu. Yritä uudelleen!")

@app.route("/deleteGig")
def deleteGig():
	id = request.args.get("sid")
	keikka.poistaKeikka(id)
	return render_template("gigUpdate.html",message="Keikka poistettu!")

@app.route("/editGig")
def editGig():
	id = request.args.get("sid")
	list = keikka.haeTiedot(id)
	print(list)
	return render_template("editGig.html",tiedot=list)

@app.route("/gigEdited", methods=["post"])
def gigEdited():
	id = request.form["keikkaid"]
	nimi = request.form["nimi"]
	pvm = request.form["pvm"]
	time = request.form["aika"]
	paikka = request.form["paikka"]
	kuvaus = request.form["kuvaus"]
	kokoonpano = request.form["kokoonpano"]
	if keikka.muokkaaKeikka(id,nimi,pvm,time,paikka,kuvaus,kokoonpano):
		return render_template("gigUpdate.html",message="Keikan tiedot päivitetty!")
	else:
		return render_template("gigUpdate.html",message="Humps, ei onnistunut vaan jotain meni pieleen. :/")
