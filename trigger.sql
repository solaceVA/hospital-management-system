DELIMITER //

        CREATE TRIGGER neo
        AFTER INSERT ON medical_record
        FOR EACH ROW
        BEGIN
            CALL rec_pre();
        END //

        DELIMITER;
