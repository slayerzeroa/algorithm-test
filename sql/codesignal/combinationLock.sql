-- https://app.codesignal.com/arcade/db/time-for-tricks/wcjiSDNohjXc2tpQM

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT ROUND(EXP(SUM(LOG(LENGTH(characters))))) AS combinations
	FROM discs;
END