from db import db
from flask import session
import users, soitin, routes

def lisaaKeikka(nimi,pvm,time,paikka,kuvaus,kokoonpano):
	sql = "INSERT INTO keikka (nimi,pvm,aika,paikka,kuvaus,kokoonpano) VALUES (:nimi,:pvm,:time,:paikka,:kuvaus,:kokoonpano) RETURNING keikka_id"
	db.session.execute(sql, {"nimi":nimi,"pvm":pvm,"time":time,"paikka":paikka,"kuvaus":kuvaus,"kokoonpano":kokoonpano})
	db.session.commit()
	return True

	
def haeKeikkaId(nimi,pvm,time,paikka,kuvaus):
	sql = "SELECT keikka_id FROM keikka WHERE nimi=:nimi,pvm=:pvm,time=:time,paikka=:paikka,kuvaus=:kuvaus"
	db.session.execute(sql, {"nimi":nimi,"pvm":pvm,"time":time,"paikka":paikka,"kuvaus":kuvaus})
	result = db.session.commit()
	return result.fetchone()[0]
	
def keikkaLista():
	sql = "SELECT * FROM keikka"
	result = db.session.execute(sql)
	return result.fetchall()

def poistaKeikka(id):
	sql = "DELETE FROM keikka WHERE keikka_id=:id"
	db.session.execute(sql,{"id":id})
	db.session.commit()
