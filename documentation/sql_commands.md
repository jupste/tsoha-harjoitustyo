CREATE TABLE choretype (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
)

CREATE TABLE household (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
)

CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	points INTEGER NOT NULL, 
	household INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(household) REFERENCES household (id)
)

CREATE INDEX name_index ON account (name)

CREATE TABLE weekly_chore (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	choretype INTEGER NOT NULL, 
	householdid INTEGER NOT NULL, 
	interval INTEGER NOT NULL, 
	points INTEGER NOT NULL, 
	last_made DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(choretype) REFERENCES choretype (id), 
	FOREIGN KEY(householdid) REFERENCES household (id)
)

CREATE TABLE chore (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	householdid INTEGER NOT NULL, 
	points INTEGER NOT NULL, 
	maxpoints INTEGER NOT NULL, 
	choretype INTEGER NOT NULL, 
	message VARCHAR(144), 
	PRIMARY KEY (id), 
	FOREIGN KEY(householdid) REFERENCES household (id), 
	FOREIGN KEY(choretype) REFERENCES choretype (id)
)

CREATE INDEX type_index ON chore (choretype)

CREATE TABLE done_chore (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	userid INTEGER NOT NULL, 
	choreid INTEGER NOT NULL, 
	points INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(userid) REFERENCES account (id), 
	FOREIGN KEY(choreid) REFERENCES chore (id)
)

