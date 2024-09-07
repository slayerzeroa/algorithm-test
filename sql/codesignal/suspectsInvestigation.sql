-- https://app.codesignal.com/arcade/db/would-you-like-the-second-meal/L3FekSnxCGMpK34bd

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT id, name, surname
	FROM Suspect
	WHERE
		height <= 170
		AND LOWER(name) LIKE 'b%'      -- The first letter of the name must be 'B' (case-insensitive)
		AND LOWER(surname) LIKE 'gre_n' -- The surname must match 'Gre?n' (case-insensitive)
	ORDER BY id ASC;
END