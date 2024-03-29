-- foreign key state for table CITY
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT AUTO_INCREMENT NOT NULL,
	state_id INT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES states(id)
);
