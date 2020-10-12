from db import db
from flask import session
import users

def add_gig(name,date,time,place,descr,comp):
	sql = "INSERT INTO keikka (nimi,pvm,aika,paikka,kuvaus,kokoonpano) VALUES (:name,:date,:time,:place,:descr,:comp) RETURNING keikka_id"
	db.session.execute(sql, {"name":name,"date":date,"time":time,"place":place,"descr":descr,"comp":comp})
	db.session.commit()
	return True

def gig_list():
	sql = "SELECT keikka_id, nimi, pvm, paikka, kuvaus, aika, kokoonpano FROM keikka"
	result = db.session.execute(sql)
	return result.fetchall()

def my_gigs(id):
	sql = "SELECT K.keikka_id, K.nimi, K.pvm, K.aika, K.paikka, K.kuvaus, K.kokoonpano FROM keikka K, kokoonpano Ko WHERE ko.users_id=:id AND K.keikka_id = Ko.keikka_id"
	result = db.session.execute(sql,{"id":id})
	return result.fetchall()

def del_gig(id):
	sql = "DELETE FROM keikka WHERE keikka_id=:id"
	db.session.execute(sql,{"id":id})
	db.session.commit()

def gig_info(id):
	sql = "SELECT keikka_id, nimi, pvm, aika, paikka, kuvaus, kokoonpano FROM keikka WHERE keikka_id=:id"
	result = db.session.execute(sql,{"id":id})
	return result.fetchall()

def edit_gig(id,name,date,time,place,descr,comp):
	sql = "UPDATE keikka SET nimi = :name, pvm = :date, aika = :time, paikka = :place, kuvaus = :descr, kokoonpano = :comp WHERE keikka_id=:id"
	db.session.execute(sql, {"nimi":name,"pvm":date,"time":time,"paikka":place,"kuvaus":descr,"kokoonpano":comp,"id":id})
	db.session.commit()
	return True

def add_user(gig_id,user_id,instr):
	sql = "SELECT soitin_id FROM soitin WHERE nimi=:instr"
	result = db.session.execute(sql,{"instr":instr})
	instr_id = result.fetchone()[0]
	sql = "INSERT INTO kokoonpano (keikka_id, users_id, soitin_id) VALUES (:gig_id, :user_id, :instr_id)"
	db.session.execute(sql,{"gig_id":gig_id,"user_id":user_id,"instr_id":instr_id})
	db.session.commit()

def delete_user(gig_id,user_id):
	sql = "DELETE FROM kokoonpano WHERE keikka_id=:gig_id AND users_id=:user_id"
	db.session.execute(sql,{"gig_id":gig_id,"user_id":user_id})
	db.session.commit()
	return True

def get_players(gig_id, instr_id): 
	sql = "SELECT username FROM users U, kokoonpano K WHERE K.keikka_id=:gig_id AND U.users_id=K.users_id AND K.soitin_id =:instr_id"
	result = db.session.execute(sql,{"gig_id":gig_id,"instr_id":instr_id})
	players = result.fetchall()
	players = [p[0] for p in players]
	return players
