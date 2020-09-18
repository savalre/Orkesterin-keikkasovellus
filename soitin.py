from db import db
import users

def get_vasket():
	sql = "SELECT nimi FROM soitin WHERE sektio='Vasket'"
	result = db.session.execute(sql)
	return result.fetchall()

def get_jouset():
    sql = "SELECT nimi FROM soitin WHERE sektio='Jouset'"
    result = db.session.execute(sql)
    return result.fetchall()

def get_puut():
    sql = "SELECT nimi FROM soitin WHERE sektio='Puut'"
    result = db.session.execute(sql)
    return result.fetchall()

def get_rytmi():
    sql = "SELECT nimi FROM soitin WHERE sektio='Rytmiryhmä'"
    result = db.session.execute(sql)
    return result.fetchall()

def get_soittimet():
    sql = "SELECT * FROM soitin ORDER BY nimi"
    result = db.session.execute(sql)
    return result.fetchall()
