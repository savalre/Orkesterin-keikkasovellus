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
	sql = "SELECT password, id FROM users WHERE username=:username"
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
    user_id = user_id()
    sql ="SELECT active_state FROM users WHERE users_id=:user_id"
    result = db.session.execute(sql, {"users_id":user_id})
    state = result.fetchone()
    return state



