from db import db
import users


def haePienryhmaSoittimet(kp):
	sql = "SELECT nimi FROM soitin WHERE sektio=:kp"
	result = db.session.execute(sql,{"kp":kp})
	soittimet = result.fetchall()
	string_list = map(' '.join,soittimet)
	return string_list

def haePienryhmaIdt(kp):
	sql = "SELECT soitin_id FROM soitin WHERE sektio=:kp"
	result = db.session.execute(sql,{"kp":kp})
	return result.fetchall()

def haeKokoOrkkaSoittimet():
	sql = "SELECT nimi FROM soitin ORDER BY soitin_id"
	result = db.session.execute(sql)
	soittimet = result.fetchall()
	string_list = map(' '.join,soittimet)
	return string_list

def haeKokoOrkkaId():
	sql = "SELECT soitin_id FROM soitin"
	result = db.session.execute(sql)
	return result.fetchall()
	
