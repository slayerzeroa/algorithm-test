-- https://app.codesignal.com/arcade/db/time-river-revisited/a9iNFQxHGDdh8r8Fi

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT id, name, event_date, participants
	FROM events
	ORDER BY
		WEEKDAY(event_date) ASC,
		participants DESC;
END