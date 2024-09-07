-- https://app.codesignal.com/arcade/db/always-leave-table-in-order/aQJquGtwg4rgXwfqH

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT
		CASE
			WHEN DAYOFWEEK(mischief_date) = 1 THEN 6
			ELSE DAYOFWEEK(mischief_date) - 2
		END AS weekday,
		mischief_date,
		author,
		title
	FROM mischief
	ORDER BY
		weekday ASC,
		FIELD (author, 'Huey', 'Dewey', 'Louie'),
		mischief_date,
		title;
END