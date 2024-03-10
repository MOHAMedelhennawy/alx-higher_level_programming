-- script that creates the database hbtn_0d_usa
-- and the table states (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE hbtn_0d_usa;
CREATE TABLE hbtn_0d_usa.states (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
