from db import db
from flask import session

def get_smallgroup_instruments(gig_comp):
	sql = "SELECT nimi FROM soitin WHERE sektio=:gig_comp"
	result = db.session.execute(sql, {"gig_comp":gig_comp})
	instruments = result.fetchall()
	instruments = [i[0] for i in instruments]
	return instruments

def get_instruments():
	sql = "SELECT nimi FROM soitin ORDER BY soitin_id"
	result = db.session.execute(sql)
	instruments = result.fetchall()
	instruments = [i[0] for i in instruments]
	return instruments

def get_instrument_id(instrument):
	sql = "SELECT soitin_id from soitin WHERE nimi=:instrument"
	result = db.session.execute(sql, {"instrument":instrument})
	return result.fetchone()[0]

def get_name_and_id():
	sql = "SELECT soitin_id, nimi from soitin"
	result = db.session.execute(sql)
	return result
	
	
