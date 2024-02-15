-- Select 2 LEFT JOIN with Where clausule
-- Execute: cat 15-comedy_only.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT A.title
FROM tv_shows A
LEFT JOIN tv_show_genres B
ON A.id = B.show_id
LEFT JOIN tv_genres C
ON B.genre_id = C.id
WHERE C.name = 'Comedy'
ORDER BY 1 ASC;
