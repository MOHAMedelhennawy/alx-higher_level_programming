-- Create a table
-- Execute: cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
CREATE TABLE IF NOT EXISTS `force_name`
(
	id INT,
	name VARCHAR(256) NOT NULL
);
