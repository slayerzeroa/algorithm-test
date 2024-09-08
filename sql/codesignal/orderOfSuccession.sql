-- https://app.codesignal.com/arcade/db/when-was-it-the-case/QGQGJF96JDN9bgprX

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT CONCAT(IF(gender='F', 'Queen', 'King'), ' ', name)
	AS name
	FROM Successors
	ORDER BY birthday;
END