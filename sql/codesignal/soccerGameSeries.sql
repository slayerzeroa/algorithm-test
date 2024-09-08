-- https://app.codesignal.com/arcade/db/when-was-it-the-case/CZBMSWZTZCHc4rcFo

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT
		CASE
			WHEN first_team_wins > second_team_wins THEN 1
			WHEN second_team_wins > first_team_wins THEN 2
			WHEN first_team_goal_diff > second_team_goal_diff THEN 1
			WHEN second_team_goal_diff > first_team_goal_diff THEN 2
			WHEN first_team_away_goals > second_team_away_goals THEN 1
			WHEN second_team_away_goals > first_team_away_goals THEN 2
			ELSE 0
		END AS winner
	FROM (
		SELECT
			SUM(IF(first_team_score > second_team_score, 1, 0)) AS first_team_wins,
			SUM(IF(second_team_score > first_team_score, 1, 0)) AS second_team_wins,
			
			SUM(first_team_score - second_team_score) AS first_team_goal_diff,
			SUM(second_team_score - first_team_score) AS second_team_goal_diff,
			
			SUM(IF(match_host = 2, first_team_score, 0)) AS first_team_away_goals,
			SUM(IF(match_host = 1, second_team_score, 0)) AS second_team_away_goals
		FROM scores
	) AS stats;

END