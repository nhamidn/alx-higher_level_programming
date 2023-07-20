-- lists all genres from the database hbtn_0d_tvshows and displays the number of shows linked to each genre.
SELECT tv_genres.genre AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
