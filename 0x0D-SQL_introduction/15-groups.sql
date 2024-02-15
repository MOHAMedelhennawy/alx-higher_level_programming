-- Write a script that lists the number of records with the same score in the table second_table
-- The result should display:
--  = the score
--  = the number of records for this score with the label number
-- The list should be sorted by the number of records (descending)
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score
