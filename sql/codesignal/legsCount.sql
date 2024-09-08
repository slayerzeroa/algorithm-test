-- https://app.codesignal.com/arcade/db/time-for-tricks/kJQWxwkjvTqhAYa9h

DROP PROCEDURE IF EXISTS solution;
CREATE PROCEDURE solution()
    SELECT
        SUM(IF(type='human', 2,
        IF(type='cat', 4,
        IF(type='dog', 4, NULL))))
    as summary_legs
    FROM creatures
    ORDER BY id;
