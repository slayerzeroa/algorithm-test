-- https://app.codesignal.com/arcade/db/join-us-at-the-table/zoJksWsAGX8NiimFN

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT 
		d.dep_name, 
		e.emp_name
	FROM 
		departments d
	CROSS JOIN 
		employees e
	ORDER BY 
		d.dep_name, 
		e.emp_name;
END