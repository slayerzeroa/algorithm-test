-- https://app.codesignal.com/arcade/db/group-dishes-by-type/fmKsqx7Aafhh6wqmq

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT item_name, item_type, COUNT(*) AS item_count
	FROM availableitems
	GROUP BY item_name, item_type
	ORDER BY item_type ASC, item_name ASC;
END