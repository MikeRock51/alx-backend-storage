-- Write a SQL script that creates a trigger that resets the
-- attribute valid_email only when the email has been changed.

DELIMITER $$
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = CASE
            WHEN NEW.valid_email = 0 THEN 1
            ELSE 0
        END;
    END IF;
END $$
DELIMITER ;
