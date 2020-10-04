CREATE TABLE users(
	users_id SERIAL PRIMARY KEY,
	username TEXT UNIQUE,
	password TEXT,
	active_status BOOLEAN,
	role TEXT
);

CREATE TABLE soitin(
	soitin_id SERIAL PRIMARY KEY,
	nimi TEXT,
	sektio TEXT
);

CREATE TABLE soittajat(
	users_id INTEGER REFERENCES users(users_id),
	soitin_id INTEGER REFERENCES soitin(soitin_id)
);

CREATE TABLE keikka(
	keikka_id SERIAL PRIMARY KEY,
	nimi TEXT,
	pvm  DATE,
	paikka TEXT,
	kuvaus TEXT
	aika TIME
	kokoonpano TEXT
);

CREATE TABLE kokoonpano(
keikka_id INTEGER REFERENCES keikka(keikka_id) ON DELETE CASCADE,
users_id INTEGER REFERENCES users(users_id),
soitin_id INTEGER REFERENCES soitin(soitin_id),
UNIQUE (keikka_id,users_id)
);
