CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT id, a, b, operation, c
	FROM expressions
	WHERE
		(operation = '+' and c = a + b) OR
		(operation = '-' and c = a - b) OR
		(operation = '*' and c = a * b) OR
		(operation = '/' and c = a / b)
	ORDER BY id ASC;
END