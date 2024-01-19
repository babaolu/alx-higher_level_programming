-- Query genres and their number of occurrences
SELECT tv_shows.title, IFNULL(tv_genres.name, 'NULL') AS name
	FROM tv_genres
	RIGHT OUTER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
	RIGHT OUTER JOIN tv_shows
	ON tv_show_genres.show_id = tv_shows.id
	ORDER BY tv_shows.title, name;
