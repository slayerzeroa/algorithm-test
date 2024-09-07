-- https://app.codesignal.com/arcade/db/group-dishes-by-type/QnrrbsfdAjNLwkRL2

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT continent, SUM(users) AS users
	FROM countries
	GROUP BY continent
	ORDER BY users DESC, continent ASC;
END