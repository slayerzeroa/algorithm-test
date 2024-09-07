-- https://app.codesignal.com/arcade/db/would-you-like-the-second-meal/qLGqhPwQtsrKRzEgv

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT DISTINCT subscriber 
	FROM full_year
	WHERE newspaper LIKE "%Daily%"

	UNION
	SELECT DISTINCT subscriber
	FROM half_year
	WHERE newspaper LIKE "%Daily%"

	ORDER BY subscriber ASC;
END