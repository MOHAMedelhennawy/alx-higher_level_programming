-- Use RIGHT JOIN
-- Execute: cat 11-genre_id_all_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT b.title, a.genre_id 
FROM tv_show_genres a 
RIGHT JOIN tv_shows b 
ON a.show_id = b.id 
ORDER BY b.title, a.genre_id ASC;
