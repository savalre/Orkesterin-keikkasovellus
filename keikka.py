from db import db
from flask import session
import users, soitin, routes

def lisaaKeikka(nimi,pvm,time,paikka,kuvaus,kokoonpano):
	sql = "INSERT INTO keikka (nimi,pvm,aika,paikka,kuvaus) VALUES (:nimi,:pvm,:time,:paikka,:kuvaus) RETURNING keikka_id"
	db.session.execute(sql, {"nimi":nimi,"pvm":pvm,"time":time,"paikka":paikka,"kuvaus":kuvaus})
	db.session.commit()




