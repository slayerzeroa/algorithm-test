-- https://app.codesignal.com/arcade/db/time-for-tricks/qAXNmPJATv6vQJ4DH

CREATE PROCEDURE solution()
    SELECT id,login,name
    FROM users
    WHERE type='user'
    OR type != 'user'
    ORDER BY id