-- https://app.codesignal.com/arcade/db/time-for-tricks/hB9cqdzPpijpE9ttD

/*Please add ; after each select statement*/
CREATE PROCEDURE solution()
BEGIN
	SELECT COUNT(id) AS number_of_nulls
	FROM departments
	WHERE description IS NULL OR
	TRIM(description) in ('null', 'nil', '-');
END