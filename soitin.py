from db import db
import users


def haePienryhmaSoittimet(kp):
	sql = "SELECT nimi FROM soitin WHERE sektio=:kp"
	result = db.session.execute(sql,{"kp":kp})
	return result.fetchall()

def haePienryhmä_idt(kp):
	sql = "SELECT soitin_id FROM soitin WHERE sektio=:kp"
	return result.fetchall()

def haeKokoOrkkaSoittimet():
    sql = "SELECT soitin_id, nimi FROM soitin ORDER BY soitin_id"
    result = db.session.execute(sql)
    return result.fetchall()

def haeKokoOrkkaId():
	sql = "SELECT soitin_id FROM soitin"
	result = db.session.execute(sql)
	return result.fetchall()
	
