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
	
def haeTiedot(id):
	print("pääsin hakemaan keikan tietoja")
	sql = "SELECT keikka_id, nimi, pvm, aika, paikka, kuvaus, kokoonpano FROM keikka WHERE keikka_id=:id"
	result = db.session.execute(sql,{"id":id})
	return result.fetchall()

def muokkaaKeikka(id, nimi,pvm,time,paikka,kuvaus,kokoonpano):
	sql = "UPDATE keikka SET nimi = :nimi, pvm = :pvm, aika = :time, paikka = :paikka, kuvaus = :kuvaus, kokoonpano = :kokoonpano WHERE keikka_id=:id"
	db.session.execute(sql, {"nimi":nimi,"pvm":pvm,"time":time,"paikka":paikka,"kuvaus":kuvaus,"kokoonpano":kokoonpano,"id":id})
	db.session.commit()
	return True

def lisaaSoittaja(keikkaId,userId,soitin):
	sql = "SELECT soitin_id FROM soitin WHERE nimi=:soitin"
	soitinId = db.session.execute(sql,{"soitin":soitin})
	sql = "INSERT INTO kokoonpano (keikka_id, users_id, soitin_id) VALUES (:keikkaId, :userId, :soitinId)"
	db.session.execute(sql,{"keikkaId":keikkaId,"userId":userId,"soitinId":soitinId})
	db.session.commit()
