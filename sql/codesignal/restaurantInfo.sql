-- https://app.codesignal.com/arcade/db/table-metamorphoses/7JdR5aZ8zkTBcyoMd

CREATE PROCEDURE solution()
BEGIN
    ALTER TABLE restaurants
    ADD description VARCHAR(100) DEFAULT "TBD",
    ADD active INT DEFAULT 1;

    SELECT * FROM restaurants ORDER BY id;
END
