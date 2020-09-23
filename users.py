from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
import soitin

def register(username,password):
	hash_value = generate_password_hash(password)
	try:
		sql = "INSERT INTO users (username,password,active_status) VALUES (:username,:password, 'true')"
		db.session.execute(sql, {"username":username,"password":hash_value,"active_status":'true'})
		db.session.commit()
	except:
		return False
	return login(username,password)

def login(username,password):
	sql = "SELECT password, users_id FROM users WHERE username=:username"
	result = db.session.execute(sql, {"username":username})
	user = result.fetchone()
	if user == None:
		return False
	else:
		hash_value = user[0]
		if check_password_hash(hash_value,password):
			session["user_id"] = user[1]
			return True
		else:
			return False

def logout():
	del session["user_id"]

def user_id():
	return session.get("user_id",0)

def active_state():
	id = user_id()
	sql = "SELECT active_status FROM users WHERE users_id=:user_id"
	result = db.session.execute(sql, {"user_id":id})
	state = result.fetchone()[0]
	print("Olen def active_state(). State = ",state)
	if state == True:
		tila = "Kyllä"
		return tila
	if state == False:
		tila = "Ei"
		return tila

def get_soitin():
	id = user_id()
	sql = "SELECT S.nimi FROM soitin S, soittajat So WHERE So.users_id=:user_id AND So.soitin_id = S.soitin_id"
	result = db.session.execute(sql, {"user_id":id})
	soitin = result.fetchone()
	print(soitin)
	if soitin == None:
		palautus = "Ei vielä valittu"
		print(palautus)
		return palautus
	else:
		return soitin

def muutatila(uusitila):
	id = user_id()
	sql = "UPDATE users SET active_status = :uusitila WHERE users_id = :user_id"
	db.session.execute(sql, {"uusitila":uusitila,"user_id":id})
	print("Uusi tila on:",uusitila)
	db.session.commit()

def muutasoitin(soitinvalinta):
	id = user_id()
	sql = "DELETE FROM soittajat WHERE users_id=:user_id"
	db.session.execute(sql, {"user_id":id})
	sql = "SELECT soitin_id FROM soitin WHERE soitin_id=:soitinvalinta"
	result = db.session.execute(sql, {"soitinvalinta":soitinvalinta})
	print("olen lisäämässä tällaista kun: ", soitinvalinta)
	sql = "INSERT INTO soittajat (users_id, soitin_id) VALUES (:user_id, :soitinvalinta)"
	db.session.execute(sql, {"user_id":id,"soitinvalinta":soitinvalinta})
	print("lisäsin soittajiin: ", soitinvalinta)
	db.session.commit()
