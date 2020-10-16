from db import db
from flask import session

def get_role(id):
	sql = "SELECT role FROM users WHERE users_id=:id"
	result = db.session.execute(sql, {"id":id})
	role = result.fetchone()[0]
	if role == "admin":
		return True
	else:
		return False

def admin_list():
	sql = "SELECT users_id, username FROM users WHERE role='admin' ORDER BY username"
	result = db.session.execute(sql)
	admins = result.fetchall()
	return admins	

def user_list():
	sql = "SELECT users_id, username FROM users WHERE role ISNULL ORDER BY username"
	result = db.session.execute(sql)
	users_list = result.fetchall()
	return users_list

def new_admin(id):
	sql = "UPDATE users SET role='admin' WHERE users_id=:id"
	db.session.execute(sql, {"id":id})
	db.session.commit()

def del_admin(id):
	sql = "UPDATE users SET role=NULL WHERE users_id=:id"
	db.session.execute(sql, {"id":id})
	db.session.commit()
