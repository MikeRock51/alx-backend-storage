-- Write a SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUserthat computes and
-- store the average weighted score for a student.
-- Requirements:
	-- Procedure ComputeAverageScoreForUser is taking 1 input:
	-- user_id, a users.id value (you can assume user_id
	-- is linked to an existing users)

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE totalWeight INT;
	DECLARE totalScore INT;

	SELECT SUM(corrections.score * projects.weight) INTO totalScore FROM corrections
	INNER JOIN projects ON projects.id = corrections.project_id
	WHERE corrections.user_id = user_id;

	SELECT SUM(weight) INTO totalWeight FROM corrections
	INNER JOIN projects ON corrections.project_id = projects.id
	WHERE corrections.user_id = user_id;

	UPDATE users
	SET average_score = totalScore / totalWeight
	WHERE users.id = user_id;
END$$
DELIMITER ;
