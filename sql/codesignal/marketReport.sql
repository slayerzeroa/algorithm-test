-- https://app.codesignal.com/arcade/db/group-dishes-by-type/47JJ5SEJHSdLusQeQ

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT country, COUNT(competitor) AS competitors
	FROM foreignCompetitors
	GROUP BY country
	
	UNION ALL
	SELECT 'Total:', COUNT(competitor)
	FROM foreignCompetitors
	
	ORDER BY
		CASE WHEN country = 'Total:' THEN 1 ELSE 0 END,
		country
	;
	
END