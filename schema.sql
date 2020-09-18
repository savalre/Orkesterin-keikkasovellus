CREATE TABLE users(
	id SERIAL PRIMARY KEY,
	username TEXT UNIQUE,
	password TEXT,
	active_status BOOLEAN,
	role TEXT
);

CREATE TABLE soitin(
	id SERIAL PRIMARY KEY,
	nimi TEXT,
	sektio TEXT
);

CREATE TABLE soittajat(
	users_id INTEGER REFERENCES users(id),
	soitin_id INTEGER REFERENCES soitin(id)
);

CREATE TABLE keikka(
	id SERIAL PRIMARY KEY,
	nimi TEXT,
	aika DATE,
	paikka TEXT,
	kuvaus TEXT
);

CREATE TABLE kokoonpano(
keikka_id INTEGER REFERENCES keikka(id),
users_id INTEGER REFERENCES users(id),
soitin_id INTEGER REFERENCES soitin(id),
UNIQUE (keikka_id,users_id)
);
