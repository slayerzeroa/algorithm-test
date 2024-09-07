-- https://app.codesignal.com/arcade/db/would-you-like-the-second-meal/RuKPyy3zx6H3h66sG

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT
		id, name, surname
	FROM Suspect
	WHERE
		height <= 170
		OR LOWER(name) NOT LIKE "b%"
		OR LOWER(surname) NOT LIKE "gre_n"
	ORDER BY id ASC;
END