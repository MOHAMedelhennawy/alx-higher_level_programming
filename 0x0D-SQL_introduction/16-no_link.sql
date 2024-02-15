-- Write a script that lists all records of the table second_table
SELECT score, name FROM second_table WHERE name!='' OR name IS NOT NULL ORDER BY score DESC;