CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT EXTRACTVALUE(xml_doc, '(catalog[1]/book[1]/author)') AS author FROM catalogs ORDER BY author;
END