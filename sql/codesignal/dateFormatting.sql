-- https://app.codesignal.com/arcade/db/time-river-revisited/kDhEa99vsWN5apGt8

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT
        IF(date_str LIKE '____-_-_', CONCAT(LEFT(date_str,5), '0', MID(date_str,6, 2), '0', RIGHT(date_str, 1)), 
        IF(date_str LIKE '____-__-_', CONCAT(LEFT(date_str, 7), '-', '0', RIGHT(date_str, 1)), 
        IF(date_str LIKE '____-_-__', CONCAT(LEFT(date_str, 5), '0', MID(date_str, 6, 5)), date_str)
        )) AS date_iso
	FROM documents
	ORDER BY(id);
END