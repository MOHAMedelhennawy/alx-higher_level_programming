-- Use LEFT JOIN and COUNT
-- Execute: cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT b.name AS genre, count(a.show_id) AS number_of_shows
FROM tv_show_genres a 
LEFT JOIN tv_genres b 
ON a.genre_id = b.id
GROUP BY a.genre_id
ORDER BY 2 DESC;
