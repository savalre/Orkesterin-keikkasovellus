from app import app
from flask import flash, render_template, request, redirect, session
import users, db, instrument, gig, admin

#login, logout, registration and admin routes

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/admin")
def admin_page():
	if session.get("user_id",0) != 0:
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
	if session.get("user_id",0) != 0:	
		users_id = request.args.get("sid")
		admin.new_admin(users_id)
		return render_template("adminUpdate.html", message="Adminoikeudet lisätty!") 
	
@app.route("/delAdmin",methods=["get"])
def delAdmin():
	if session.get("user_id",0) != 0:
		users_id = request.args.get("sid")
		admin.del_admin(users_id)
		return render_template("adminUpdate.html",message="Adminoikeudet poistettu!")

@app.route("/login",methods=["get","post"]) 
def login():
		error = None;
		username = request.form["username"]
		password = request.form["password"]
		if users.login(username,password):
			session["username"] = username
			session["user_id"] = users.user_id()
			users_id = users.user_id()
			if admin.get_role(users_id) == True:
				session["role"] = "admin"
			else:
				session["role"] = "normal_user"
			session["active_state"] = users.active_status()[0]
			return redirect("/")
		else:
			error = "Väärä käyttäjätunnus tai salasana!"
			return render_template("index.html",error=error)

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

#user-related routes
		
@app.route("/userinfo",methods=["get","post"])
def userinfo():
		if session.get("user_id",0) != 0:
			instr = users.get_instrument()
			status = users.active_status()
			return render_template("userinfo.html", instr = instr, status=status)

@app.route("/edit_user",methods=["get","post"])
def edit_user():
	if session.get("user_id",0) != 0:
		instr = instrument.get_name_and_id()
		return render_template("edit_user.html", instr=instr)
	
@app.route("/userUpdated", methods=["post"])
def userUpdated():
	if session.get("user_id",0) != 0:
		status = request.form["active"]
		choice = request.form.getlist("soitin")
		users.new_status(status)
		users.change_instrument(choice)
		return render_template("update.html", message="Profiilisi on päivitetty!")

#gig-related routes

@app.route("/gig_index")
def gig_index():
	if session.get("user_id",0) != 0:
		return render_template("gig_index.html")

@app.route("/upcoming_gigs")
def upcoming_gigs():
	if session.get("user_id",0) != 0:
		gig_list = gig.gig_list()
		return render_template("upcoming_gigs.html", gig_list=gig_list)

@app.route("/my_gigs")
def my_gigs():
	if session.get("user_id",0) != 0:
		id = users.user_id()
		gig_list = gig.my_gigs(id)
		return render_template("my_gigs.html",gig_list=gig_list)

@app.route("/newGig")
def new_gig():
	if session.get("user_id",0) != 0:
		return render_template("addgig.html")

@app.route("/gigAdd",methods=["post"])
def gigAdd():
	if session.get("user_id",0) != 0:
		message = None;
		name = request.form["name"]
		date = request.form["date"]
		time = request.form["time"]
		place = request.form["place"]
		descr = request.form["descr"]
		comp = request.form["comp"]
		if comp == "Koko_orkesteri":
			comp = "Koko orkesteri"
		if gig.add_gig(name,date,time,place,descr,comp):
			message = "Keikka lisätty onnistuneesti!"
			gig_list = gig.gig_list()
			return render_template("upcoming_gigs.html", message=message, gig_list=gig_list) 
		else:
			message = "Oho, jotain meni pieleen eikä keikkaa luotu. Yritä uudelleen!"
			gig_list = gig.gig_list()
			return render_template("upcoming_gigs.html",message=message, gig_list=gig_list)

@app.route("/deleteGig")
def deleteGig():
	if session.get("user_id",0) != 0:
		id = request.args.get("sid")
		gig.del_gig(id)
		message = "Keikka poistettu!"
		gig_list = gig.gig_list()
		return render_template("upcoming_gigs.html", message=message, gig_list=gig_list)

@app.route("/editGig")
def editGig():
	if session.get("user_id",0) != 0:
		id = request.args.get("sid")
		list = gig.gig_info(id)
		return render_template("editGig.html",tiedot=list)

@app.route("/gigEdited", methods=["post"])
def gigEdited():
	if session.get("user_id",0) != 0:
		id = request.form["id"]
		name = request.form["name"]
		date = request.form["date"]
		time = request.form["time"]
		place = request.form["place"]
		descr = request.form["descr"]
		comp = request.form["comp"]
		if comp == "Koko_orkesteri":
			comp = "Koko orkesteri"
		if gig.edit_gig(id,name,date,time,place,descr,comp):
			gig_list = gig.gig_list()
			return render_template("upcoming_gigs.html",message="Keikan tiedot päivitetty!", gig_list=gig_list)
		else:
			gig_list = gig.gig_list()
			return render_template("upcoming_gigs.html",message="Humps, ei onnistunut vaan jotain meni pieleen. :/", gig_list=gig_list)

#gig composition and gig registration related routes 
	
@app.route("/gigReg")
def gig_registration():
	if session.get("user_id",0) != 0:
		id = request.args.get("sid")
		userId = users.user_id()
		info = gig.gig_info(id)
		instruments = users.get_instrument()
		return render_template("gigReg.html", info=info, instruments=instruments)

@app.route("/reg_complete", methods=["post"])
def reg_complete():
	if session.get("user_id",0) != 0:	
		instr = request.form["instr"]
		gig_id = request.form["id"]
		user_id = users.user_id()
		gig.add_user(gig_id,user_id,instr)
		gig_list = gig.my_gigs(user_id)
		return render_template("my_gigs.html", message="Ilmoittautuminen onnistui! Tervetuloa keikalle!", gig_list=gig_list)

@app.route("/del")
def del_registration():
	if session.get("user_id",0) != 0:
		gig_id = request.args.get("sid")
		user_id = users.user_id()
		gig.delete_user(gig_id,user_id)
		gig_list = gig.my_gigs(user_id)
		return render_template("my_gigs.html", message= "Ilmoittautuminen poistettu!", gig_list=gig_list)

@app.route("/composition")
def gig_composition():
	if session.get("user_id",0) != 0:
		gig_comp = request.args.get("skp")
		gig_id = request.args.get("sid")
		info = gig.gig_info(gig_id)
		if gig_comp == "Koko orkesteri":
			gig_instr = gig.get_gigcomp_all(gig_id)
			maybes = gig.who_you_gonna_call(gig_id,gig_comp)
			print(maybes)
			return render_template("composition.html", gig_instr = gig_instr, info = info,maybes=maybes)
		else: 
			gig_instr = gig.get_gigcomp_smallgroup(gig_id,gig_comp)
			maybes = gig.who_you_gonna_call(gig_id,gig_comp)
			return render_template("composition.html", gig_instr = gig_instr, info = info, maybes=maybes)
