-- https://app.codesignal.com/arcade/db/time-river-revisited/G9zoZjTzk6JpJGFbd/solutions

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	WITH RECURSIVE cte (alarm_date) AS (
		SELECT input_date as alarm_date FROM userInput
		UNION
		SELECT DATE_ADD(alarm_date, INTERVAL 7 DAY) as alarm_date FROM cte
		WHERE YEAR(DATE_ADD(alarm_date, INTERVAL 7 DAY) ) = YEAR(alarm_date)	
	)
	SELECT * FROM cte;
END