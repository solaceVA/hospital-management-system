DELIMITER //
        CREATE PROCEDURE rec_pre()
        BEGIN
            SELECT 
                nr.Record_ID,
                concat(nr.pfn, " " , nr.pln) as Patient_Name,
                concat(nr.dfn, " " , nr.dln) as Doctor_Name,
                pnr.Medicine_ID,
                pnr.Medicine_Name
            FROM 
                (
                    SELECT 
                        mr.Record_ID,
                        p.First_Name as pfn,
                        p.Last_Name as pln,
                        d.First_Name as dfn,
                        d.Last_Name as dln
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
