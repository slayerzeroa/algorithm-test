-- https://app.codesignal.com/arcade/db/time-river-revisited/7T48qZTwkBTtWAiEz

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT name, event_date
	FROM Events
	WHERE
        event_date > (SELECT MAX(event_date) FROM Events) - INTERVAL 8 DAY
	ORDER BY event_date DESC
	LIMIT 1000 OFFSET 1;
END