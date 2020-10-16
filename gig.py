from db import db
from flask import session
import users, instrument

def add_gig(name,date,time,place,descr,comp):
	sql = "INSERT INTO keikka (nimi,pvm,aika,paikka,kuvaus,kokoonpano) VALUES (:name,:date,:time,:place,:descr,:comp) RETURNING keikka_id"
	db.session.execute(sql, {"name":name,"date":date,"time":time,"place":place,"descr":descr,"comp":comp})
	db.session.commit()
	return True

def gig_list():
	sql = "SELECT keikka_id, nimi, to_char(pvm, 'DD/MM/YYYY'), paikka, kuvaus, to_char(aika, 'HH24:MI'), kokoonpano FROM keikka ORDER BY pvm, aika"
	result = db.session.execute(sql)
	return result.fetchall()

def my_gigs(id):
	sql = """SELECT K.keikka_id, K.nimi, to_char(K.pvm, 'DD/MM/YYYY'), to_char(K.aika, 'HH24:MI'), K.paikka, K.kuvaus, K.kokoonpano 
			FROM keikka K, kokoonpano Ko WHERE ko.users_id=:id AND K.keikka_id = Ko.keikka_id ORDER BY K.pvm, K.aika"""
	result = db.session.execute(sql, {"id":id})
	return result.fetchall()

def del_gig(id):
	sql = "DELETE FROM keikka WHERE keikka_id=:id"
	db.session.execute(sql, {"id":id})
	db.session.commit()

def gig_info(id):
	sql = "SELECT keikka_id, nimi, pvm, aika, paikka, kuvaus, kokoonpano FROM keikka WHERE keikka_id=:id"
	result = db.session.execute(sql, {"id":id})
	return result.fetchall()

def edit_gig(id,name,date,time,place,descr,comp):
	sql = """UPDATE keikka SET nimi = :name, pvm = :date, aika = :time, paikka = :place, 
			kuvaus = :descr, kokoonpano = :comp WHERE keikka_id=:id"""
	db.session.execute(sql, {"name":name,"date":date,"time":time,"place":place,"descr":descr,"comp":comp,"id":id})
	db.session.commit()
	return True

def add_user(gig_id,user_id,instr):
	sql = "SELECT soitin_id FROM soitin WHERE nimi=:instr"
	result = db.session.execute(sql, {"instr":instr})
	instr_id = result.fetchone()[0]
	sql = "INSERT INTO kokoonpano (keikka_id, users_id, soitin_id) VALUES (:gig_id, :user_id, :instr_id)"
	db.session.execute(sql, {"gig_id":gig_id,"user_id":user_id,"instr_id":instr_id})
	db.session.commit()

def delete_user(gig_id,user_id):
	sql = "DELETE FROM kokoonpano WHERE keikka_id=:gig_id AND users_id=:user_id"
	db.session.execute(sql, {"gig_id":gig_id,"user_id":user_id})
	db.session.commit()
	return True

def get_players(gig_id, instr_id): 
	sql = "SELECT U.username FROM users U, kokoonpano K WHERE K.keikka_id=:gig_id AND U.users_id=K.users_id AND K.soitin_id =:instr_id"
	result = db.session.execute(sql, {"gig_id":gig_id,"instr_id":instr_id})
	players = result.fetchall()
	players = [p[0] for p in players]
	return players

def get_gigcomp_all(gig_id):
	gig_instr = instrument.get_instruments()
	y = len(gig_instr) * 2
	for x in range(0,y,2):
		instr = gig_instr[x]
		instr_id = instrument.get_instrument_id(instr)
		kp = get_players(gig_id, instr_id)
		gig_instr.insert(x+1, kp)
		x = x+2
	return gig_instr

def get_gigcomp_smallgroup(gig_id,gig_comp):
	gig_instr = instrument.get_smallgroup_instruments(gig_comp)
	y = len(gig_instr) * 2
	for x in range(0,y,2):
		instr = gig_instr[x]
		instr_id = instrument.get_instrument_id(instr)
		kp = get_players(gig_id, instr_id)
		gig_instr.insert(x+1, kp)
		x = x+2
	return gig_instr
		
def who_you_gonna_call(gig_id,gig_comp):
	if gig_comp == "Koko orkesteri":
		maybes = instrument.get_instruments()
		y = len(maybes) * 2
		for x in range(0,y,2):
			instr = maybes[x]
			instr_id = instrument.get_instrument_id(instr)
			kp = call_me(gig_id, instr_id)
			maybes.insert(x+1, kp)
			x = x+2
	else:
		maybes = instrument.get_smallgroup_instruments(gig_comp)
		y = len(maybes) * 2
		for x in range(0,y,2):
			instr = maybes[x]
			instr_id = instrument.get_instrument_id(instr)
			kp = call_me(gig_id, instr_id)
			maybes.insert(x+1, kp)
			x = x+2
	return maybes

def call_me(gig_id,instr_id):
	sql= """SELECT U.username FROM users U, soittajat SO 
		WHERE SO.users_id=U.users_id AND SO.soitin_id =:instr_id 
		AND U.active_status=true AND U.username NOT IN (SELECT username FROM users U, kokoonpano K 
		WHERE K.keikka_id=:gig_id AND U.users_id=K.users_id AND U.username IS NOT NULL)"""
	result = db.session.execute(sql,{"gig_id":gig_id,"instr_id":instr_id})
	maybes = result.fetchall()
	maybes = [m[0] for m in maybes]
	return maybes
	
