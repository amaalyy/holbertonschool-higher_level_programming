-- script that lists all shows contained in hbtn_0d_tvshows
SELECT tv_show_title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_show.id = tv_show_genres.genre_id
ORDER BY tv_show_title, tv_show_genres.genre_id ASC;
