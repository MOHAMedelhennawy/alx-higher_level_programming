-- Select with 2 LEFT JOIN return NULL
-- Execute: cat 16-shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT A.title, C.name
FROM tv_shows A
LEFT JOIN tv_show_genres B
ON A.id = B.show_id
LEFT JOIN tv_genres C
ON B.genre_id = C.id
ORDER BY 1,2 ASC;
