-- https://app.codesignal.com/arcade/db/group-dishes-by-type/PPNoC7RpXJPGQcqi2

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT DISTINCT director
	FROM moviesInfo
	WHERE (year > 2000)
	GROUP BY director
	HAVING SUM(oscars) > 2
	ORDER BY director ASC;
END