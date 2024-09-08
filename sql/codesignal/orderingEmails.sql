-- https://app.codesignal.com/arcade/db/when-was-it-the-case/KbjWnZy3cpPJxj2st

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT 
        id,
        email_title,
        IF(size >= POWER(2, 20), 
            CONCAT(FLOOR(size / POWER(2, 20)), ' Mb'),
            IF(size >= POWER(2, 10), 
                CONCAT(FLOOR(size / POWER(2, 10)), ' Kb'),
                CONCAT(0, ' Kb')
            )
        ) AS short_size
    FROM 
        emails
    ORDER BY 
        size DESC;
END