-- https://app.codesignal.com/arcade/db/join-us-at-the-table/nmkfbP6qGo63u6vih

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT u.id, IFNULL(c.country, 'unknown') AS country
	FROM users u
	LEFT JOIN cities c ON u.city = c.city;
END