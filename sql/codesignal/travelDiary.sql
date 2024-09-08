-- https://app.codesignal.com/arcade/db/group-dishes-by-type/p7k9JJ5fqyD6DdFZJ

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT GROUP_CONCAT(DISTINCT country ORDER BY country SEPARATOR ';') AS countries
	FROM diary;
END