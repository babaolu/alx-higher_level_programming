-- Queries cities of California
SELECT * FROM cities WHERE id = 
	(SELECT id FROM states WHERE name = "California") ORDER BY id ASC;
