from db import db
import users

def get_soittimet():
	sql = "SELECT nimi FROM soitin"
	result = db.session.execute(sql)
	return result.fetchall()


