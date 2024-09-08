-- https://app.codesignal.com/arcade/db/time-river-revisited/DeEnHPtgxR9bH2mZH

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT
		YEAR(date) as year,
		QUARTER(date) as quarter,
		SUM(profit - loss) as net_profit
	FROM accounting
	GROUP BY year, quarter
	ORDER BY year, quarter;
END