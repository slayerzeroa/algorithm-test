-- https://app.codesignal.com/arcade/db/specialties/Kux26wwi4vNpbJhno

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT name
	FROM people_hobbies
	WHERE hobbies LIKE "%reading%" AND
	hobbies LIKE "%sports%"
	ORDER BY name;
END