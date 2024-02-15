-- Use LEFT JOIN
-- Execute: cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT b.title, a.genre_id 
FROM tv_show_genres a 
LEFT JOIN tv_shows b 
ON a.show_id = b.id 
ORDER BY b.title, a.genre_id ASC;
