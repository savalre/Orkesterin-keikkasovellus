from db import db
from flask import session
import users

def add_gig(nimi,pvm,time,paikka,kuvaus,kokoonpano):
	sql = "INSERT INTO keikka (nimi,pvm,aika,paikka,kuvaus,kokoonpano) VALUES (:nimi,:pvm,:time,:paikka,:kuvaus,:kokoonpano) RETURNING keikka_id"
	db.session.execute(sql, {"nimi":nimi,"pvm":pvm,"time":time,"paikka":paikka,"kuvaus":kuvaus,"kokoonpano":kokoonpano})
	db.session.commit()
	return True

def haeKeikkaId(nimi,pvm,time,paikka,kuvaus):
	sql = "SELECT keikka_id FROM keikka WHERE nimi=:nimi,pvm=:pvm,time=:time,paikka=:paikka,kuvaus=:kuvaus"
	db.session.execute(sql, {"nimi":nimi,"pvm":pvm,"time":time,"paikka":paikka,"kuvaus":kuvaus})
	result = db.session.commit()
	return result.fetchone()[0]

def gig_list():
	sql = "SELECT * FROM keikka"
	result = db.session.execute(sql)
	return result.fetchall()

def my_gigs(id):
	sql = "SELECT K.keikka_id, K.nimi, K.pvm, K.aika, K.paikka, K.kuvaus, K.kokoonpano FROM keikka K, kokoonpano Ko WHERE ko.users_id=:id AND K.keikka_id = Ko.keikka_id"
	result = db.session.execute(sql,{"id":id})
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
	result = db.session.execute(sql,{"soitin":soitin})
	soitinId = result.fetchone()[0]
	print("hainko id:n? HEI= ",soitinId)
	sql = "INSERT INTO kokoonpano (keikka_id, users_id, soitin_id) VALUES (:keikkaId, :userId, :soitinId)"
	db.session.execute(sql,{"keikkaId":keikkaId,"userId":userId,"soitinId":soitinId})
	db.session.commit()

def poistaSoittaja(keikkaId,userId):
	sql = "DELETE FROM kokoonpano WHERE keikka_id=:keikkaId AND users_id=:userId"
	db.session.execute(sql,{"keikkaId":keikkaId,"userId":userId})
	db.session.commit()
	return True


def haeSoittaja(id, soitinId): 
	sql = "SELECT username FROM users U, kokoonpano K WHERE K.keikka_id=:id AND U.users_id=K.users_id AND K.soitin_id =:soitinId"
	result = db.session.execute(sql,{"id":id,"soitinId":soitinId})
	soittajat = result.fetchall()
	soittajat = [s[0] for s in soittajat]
	return soittajat
	
