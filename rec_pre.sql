DELIMITER //
        CREATE PROCEDURE rec_pre()
        BEGIN
            SELECT 
                nr.Record_ID,
                nr.Patient_ID,
                CONCAT(IFNULL(nr.pfn, ''), ' ', IFNULL(nr.pln, '')) AS Patient_Name,
                nr.Doctor_ID,
                CONCAT(IFNULL(nr.dfn, ''), ' ', IFNULL(nr.dln, '')) AS Doctor_Name,
                pnr.Medicine_ID,
                pnr.Medicine_Name
            FROM 
                (
                    SELECT 
                        mr.Record_ID,
                        p.First_Name as pfn,
                        p.Last_Name as pln,
                        p.Patient_ID,
                        d.First_Name as dfn,
                        d.Last_Name as dln,
                        d.Doctor_ID
                    FROM 
                        medical_record as mr
                    INNER JOIN 
                        patients AS p ON mr.Patient_ID = p.Patient_ID
                    INNER JOIN 
                        doctors AS d ON mr.Doctor_ID = d.Doctor_ID
                ) AS nr
            INNER JOIN
                (
                    SELECT
                        pr.Record_ID,
                        pr.Medicine_ID,
                        meds.Medicine_Name
                    FROM
                        prescriptions AS pr
                    INNER JOIN
                        medications as meds on pr.Medicine_ID = meds.Medicine_ID
                ) AS pnr ON nr.Record_ID = pnr.Record_ID;
        END //

        DELIMITER ;
