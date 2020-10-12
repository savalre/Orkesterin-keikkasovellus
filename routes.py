from app import app
from flask import render_template, request, redirect, session
import users, db, instrument, gig, admin

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/admin")
def admin_page():
	enter = False
	users_id = session.get("user_id",0)
	if admin.get_role(users_id):
		enter = True
		admins = admin.admin_list()
		normal_users = admin.user_list()
		return render_template("admin.html", admins=admins, normal_users=normal_users)
	else:
		return render_template("error.html", message="Sinulla ei ole oikeuksia tälle sivulle, otathan yhteyttä ylläpitoon jos tämä on virhe")

@app.route("/addAdmin",methods=["get"])
def addAdmin():
	users_id = request.args.get("sid")
	admin.new_admin(users_id)
	return render_template("adminUpdate.html", message="Adminoikeudet lisätty!") 
	
@app.route("/delAdmin",methods=["get"])
def delAdmin():
	users_id = request.args.get("sid")
	admin.del_admin(users_id)
	return render_template("adminUpdate.html",message="Adminoikeudet poistettu!")

@app.route("/login",methods=["get","post"]) 
def login():
		username = request.form["username"]
		password = request.form["password"]
		if users.login(username,password):
			session["username"] = username
			session["user_id"] = users.user_id()
			users_id = users.user_id()
			
			if admin.get_role(users_id) == True:
				session["role"] = "admin"
			else:
				session["role"] = "peruskäyttäjä"
				
			session["active_state"] = users.active_status()[0]
			return redirect("/")
		else:
			return render_template("error.html",message="Väärä käyttäjätunnus tai salasana")

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
			password = password1;
			if users.register(username,password):
				session["username"] = username
				return redirect("/")
			else:
				return render_template("error.html",message="Hups, rekisteröinti ei onnistunut!")
		else: 
			return render_template("error.html",message="Salasanat eivät ole samat! Kokeile uudestaan")
		
@app.route("/userinfo",methods=["get","post"])
def userinfo():
		instr = users.get_instrument()
		status = users.active_status()
		return render_template("userinfo.html", instr = instr, status=status)

@app.route("/edit_user",methods=["get","post"])
def edit_user():
	instr = instrument.get_name_and_id()
	return render_template("edit_user.html", instr=instr)
	
@app.route("/userUpdated", methods=["post"])
def userUpdated():
	status = request.form["active"]
	choice = request.form.getlist("soitin")
	users.new_status(status)
	users.change_instrument(choice)
	return render_template("update.html", message="Profiilisi on päivitetty!")

@app.route("/keikkasivu")
def keikkasivu():
	lista = gig.gig_list()
	return render_template("keikka.html", keikat=lista)

@app.route("/tulevatKeikat")
def tulevatKeikat():
	lista = gig.gig_list()
	return render_template("tulevatKeikat.html", keikat=lista)

@app.route("/omatKeikat")
def my_gigs():
	id = users.user_id()
	lista = gig.my_gigs(id)
	return render_template("omatKeikat.html",keikat=lista)

@app.route("/newGig")
def uusi_keikka():
	return render_template("addgig.html")

@app.route("/gigAdd",methods=["post"])
def gigAdd():
	name = request.form["name"]
	date = request.form["date"]
	time = request.form["time"]
	place = request.form["place"]
	descr = request.form["descr"]
	comp = request.form["comp"]
	if gig.add_gig(name,date,time,place,descr,comp):
		return render_template("gigUpdate.html",message="Keikka lisätty onnistuneesti!")
	else:
		return render_template("error.html",message="Oho, jotain meni pieleen eikä keikkaa luotu. Yritä uudelleen!")

@app.route("/deleteGig")
def deleteGig():
	id = request.args.get("sid")
	gig.del_gig(id)
	return render_template("gigUpdate.html",message="Keikka poistettu!")

@app.route("/editGig")
def editGig():
	id = request.args.get("sid")
	list = gig.gig_info(id)
	return render_template("editGig.html",tiedot=list)

@app.route("/gigEdited", methods=["post"])
def gigEdited():
	id = request.form["id"]
	name = request.form["name"]
	date = request.form["date"]
	time = request.form["time"]
	place = request.form["place"]
	descr = request.form["descr"]
	comp = request.form["comp"]
	if gig.edit_gig(id,name,date,time,place,descr,comp):
		return render_template("gigUpdate.html",message="Keikan tiedot päivitetty!")
	else:
		return render_template("gigUpdate.html",message="Humps, ei onnistunut vaan jotain meni pieleen. :/")
		
@app.route("/ilmo")
def ilmo():
	id = request.args.get("sid")
	userId = users.user_id()
	tiedot = gig.gig_info(id)
	soittimet = users.get_instrument()
	return render_template("ilmo.html", tiedot=tiedot, soittimet=soittimet)

@app.route("/ilmoDone", methods=["post"])
def ilmoDone():
	instr = request.form["soitin"]
	gig_id = request.form["id"]
	user_id = users.user_id()
	gig.add_user(gig_id,user_id,instr)
	return render_template("gigUpdate.html", message="Ilmoittautuminen onnistui! Tervetuloa keikalle!")

@app.route("/del")
def poistaIlmo():
	gig_id = request.args.get("sid")
	user_id = users.user_id()
	gig.delete_user(gig_id,user_id)
	return render_template("gigUpdate.html", message= "Poistit ilmoittautumisesi keikalle")

@app.route("/kokoonpano")
def kokoonpano():
	gig_comp = request.args.get("skp")
	gig_id = request.args.get("sid")
	keikanTiedot = gig.gig_info(gig_id)
	if gig_comp == "Koko_orkesteri":
		keikanSoittimet = instrument.get_instruments()
		y = len(keikanSoittimet) * 2
		for x in range(0,y,2):
				instr = keikanSoittimet[x]
				instr_id = instrument.get_instrument_id(instr)
				kp = gig.get_players(gig_id, instr_id)
				keikanSoittimet.insert(x+1, kp)
				x = x+2
		return render_template("kokoonpano.html", keikanSoittimet = keikanSoittimet, keikanTiedot = keikanTiedot)
	else: 
		keikanSoittimet = instrument.get_smallgroup_instruments(gig_comp)
		y = len(keikanSoittimet) * 2
		for x in range(0,y,2):
				instr = keikanSoittimet[x]
				instr_id = instrument.get_instrument_id(instr)
				kp = gig.get_players(gig_id, instr_id)
				keikanSoittimet.insert(x+1, kp)
				x = x+2
		return render_template("kokoonpano.html", keikanSoittimet = keikanSoittimet, keikanTiedot = keikanTiedot)
		
