from db import db
from flask import session
import users, soitin, routes


def haerooli(id):
	print("admin haussa! id:", id)
	sql = "SELECT role FROM users WHERE users_id=:id"
	result = db.session.execute(sql,{"id":id})
	rooli = result.fetchone()[0]
	print("hain roolin, se on: ",rooli)
	if rooli == "admin":
		print(id," on admin, rooli: ", rooli)
		return True
	else:
		print("palautan false")
		return False

def listaaAdmin():
	sql = "SELECT users_id, username FROM users WHERE role='admin' ORDER BY username"
	result = db.session.execute(sql)
	adminit = result.fetchall()
	return adminit	

def listaaKayttajat():
	sql = "SELECT users_id, username FROM users WHERE role ISNULL ORDER BY username"
	result = db.session.execute(sql)
	kayttajat = result.fetchall()
	print("löysin käyttäjät: ",kayttajat)
	return kayttajat

def lisaaAdmin(id):
	print("löysin lisaaAdminiin! id on: ",id)
	sql = "UPDATE users SET role='admin' WHERE users_id=:id"
	db.session.execute(sql,{"id":id})
	db.session.commit()
	print("admin lisätty!")

def poistaAdmin(id):
	sql = "UPDATE users SET role=NULL WHERE users_id=:id"
	db.session.execute(sql,{"id":id})
	db.session.commit()
