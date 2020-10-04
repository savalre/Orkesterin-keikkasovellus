from db import db
import users


def haePienryhmaSoittimet(kp):
	sql = "SELECT nimi FROM soitin WHERE sektio=:kp"
	result = db.session.execute(sql,{"kp":kp})
	soittimet = result.fetchall()
	return soittimet

def haePienryhmaIdt(kp):
	sql = "SELECT soitin_id FROM soitin WHERE sektio=:kp"
	result = db.session.execute(sql,{"kp":kp})
	return result.fetchall()

def haeKaikkiSoittimet():
	sql = "SELECT nimi FROM soitin ORDER BY soitin_id"
	result = db.session.execute(sql)
	soittimet = result.fetchall()
	return soittimet

def haeKokoOrkkaId():
	sql = "SELECT soitin_id FROM soitin"
	result = db.session.execute(sql)
	return result.fetchall()
	
def haeSoitinid(soitin):
	print("olen haeSOitinid. soitin on: ",soitin)
	sql = "SELECT soitin_id from soitin WHERE nimi=:soitin"
	result = db.session.execute(sql,{"soitin":soitin})
	return result.fetchone()[0]
	
