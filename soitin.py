from db import db
import users

#näitä käytetään keikka.lisääKokoonpano-metodissa

def get_vasket():
	sql = "SELECT soitin_id FROM soitin WHERE sektio='Vasket'"
	result = db.session.execute(sql)
	return result.fetchall()

def get_jouset():
    sql = "SELECT soitin_id FROM soitin WHERE sektio='Jouset'"
    result = db.session.execute(sql)
    return result.fetchall()

def get_puut(): 
    sql = "SELECT soitin_id FROM soitin WHERE sektio='Puut'"
    result = db.session.execute(sql)
    return result.fetchall()

def get_rytmi():
    sql = "SELECT soitin_id FROM soitin WHERE sektio='Rytmiryhmä'"
    result = db.session.execute(sql)
    return result.fetchall()

def get_soittimet():
    sql = "SELECT soitin_id FROM soitin ORDER BY nimi"
    result = db.session.execute(sql)
    return result.fetchall()
