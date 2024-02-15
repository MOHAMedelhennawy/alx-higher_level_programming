-- Create a table with constrains and FOREING KEY
-- Execute: cat 7-cities.sql | mysql -hlocalhost -uroot -p
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS `cities`
(
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
	state_id INT NOT NULL,
	name VARCHAR(256),
	FOREIGN KEY(state_id) REFERENCES states(id)
);
