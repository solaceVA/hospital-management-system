import pymysql

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='Phoenixwalnut@9094',
        database='hdb'
    )

def create_record(data):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
                INSERT INTO medical_record (Patient_ID, Doctor_ID, Record_Date, Diagnosis, Treatment)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                data['patient_id'], data['doctor_id'], data['date'],
                data['diagnosis'], data['treatment']
            ))
            connection.commit()
            print("Record created successfully.")
    finally:
        connection.close()

def update_diagnosis(record_id, diagnosis):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE medical_record SET Diagnosis = %s WHERE Record_ID = %s"
            cursor.execute(sql, (diagnosis, record_id))
            connection.commit()
            print("Diagnosis updated successfully.")
    finally:
        connection.close()

def update_treatment(record_id, treatment):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE medical_record SET Treatment = %s WHERE Record_ID = %s"
            cursor.execute(sql, (treatment, record_id))
            connection.commit()
            print("Treatment updated successfully.")
    finally:
        connection.close()

x = {'patient_id': 1, 'doctor_id': 1, 'date': '2021-09-01', 'diagnosis': 'Fever', 'treatment': 'Paracetamol'}
update_treatment(1, 'Cetcip')