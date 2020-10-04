from db import db
from flask import session
import users, soitin, routes


def isAdmin(id):
	sql = "SELECT role FROM users WHERE users_id=:id"
	result = db.session.execute(sql,{"id":id})
	if result == "admin":
		return True
	else:
		return False

def listaaAdmin():
	sql = "SELECT users_id, username FROM users WHERE role='admin'"
	result = db.session.execute(sql)
	adminit = result.fetchall()
	return adminit
	

def lisaaAdmin(id):
	sql = "UPDATE users SET rooli='admin' WHERE users_id=:id"
	db.session.execute(sql,{"id":id})
	db.session.commit()

def poistaAdmin(id):
	sql = "UPDATE users SET rooli='' WHERE users_id=:id"
	db.session.execute(sql,{"id":id})
	db.session.commit()
