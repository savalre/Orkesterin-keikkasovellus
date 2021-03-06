from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def active_status():
	id = user_id()
	sql = "SELECT active_status FROM users WHERE users_id=:user_id"
	result = db.session.execute(sql, {"user_id":id})
	state = result.fetchone()[0]
	if state == True:
		status = "Kyllä"
		return status
	if state == False:
		status = "Ei"
		return status

def get_instrument():
	id = user_id()
	sql = "SELECT S.nimi FROM soitin S, soittajat So WHERE So.users_id=:user_id AND So.soitin_id = S.soitin_id"
	result = db.session.execute(sql, {"user_id":id})
	instrument = result.fetchall() 
	if instrument == None:
		value = "Ei vielä valittu"
		return value
	else:
		string_list = [i[0] for i in instrument]
		return string_list

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
	
def change_instrument(choice): 
	id = user_id()
	sql = "DELETE FROM soittajat WHERE users_id=:user_id"
	db.session.execute(sql, {"user_id":id})
	list_length = len(choice)
	for s in range(list_length):
		sql = "INSERT INTO soittajat (users_id, soitin_id) VALUES (:user_id, :s)"
		db.session.execute(sql, {"user_id":id,"s":choice[s]})
	db.session.commit()

def new_status(status):
	id = user_id()
	sql = "UPDATE users SET active_status = :status WHERE users_id = :user_id"
	db.session.execute(sql, {"status":status,"user_id":id})
	db.session.commit()
		
def user_id():
	return session.get("user_id",0)

def register(username,password):
	hash_value = generate_password_hash(password)
	try:
		sql = "INSERT INTO users (username,password,active_status) VALUES (:username,:password, 'true')"
		db.session.execute(sql, {"username":username,"password":hash_value,"active_status":'true'})
		db.session.commit()
	except:
		return False
	return login(username,password)
