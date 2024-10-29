import pymysql

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='Ajwin2008',
        database='hdb'
    )

def create_prescription(data):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO prescriptions (Record_ID, Medicine_ID, Quantity, Start_Date, End_Date) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (data['record_id'],data['medicine_id'],data['quantity'],data['start_date'],data['end_date']))
            connection.commit()
            print("Prescription created successfully.")
    finally:
        connection.close()

def get_all_prescriptions():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Prescriptions"
            cursor.execute(sql)
            prescriptions = cursor.fetchall()
            if not prescriptions: 
                print("No prescriptions found.")
            else:
                for prescription in prescriptions:
                    print(prescription)
    finally:
        connection.close()

def get_prescription(record, medicine):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Prescriptions WHERE Record_ID = %s AND Medicine_ID = %s"
            cursor.execute(sql, (record, medicine))
            prescription = cursor.fetchone()
            if not prescription:
                print("Prescription not found.")
            else:
                print(prescription)
    finally:
        connection.close()

def update_quantity(record_id, medicine_id, quantity):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
                    UPDATE Prescriptions 
                    SET Quantity = %s
                    WHERE Record_ID = %s AND Medicine_ID = %s
                  """
            cursor.execute(sql, (quantity, record_id, medicine_id))  # Corrected parameter order
            connection.commit()
        print("Medicine quantity updated successfully.")
    finally:
        connection.close()

def update_end_date(record_id, medicine_id, end_date):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
                    UPDATE Prescriptions 
                    SET End_Date = %s 
                    WHERE Record_ID = %s AND Medicine_ID = %s
                  """
            cursor.execute(sql, (end_date, record_id, medicine_id))  # Corrected parameter order
            connection.commit()
        print("End date updated successfully.")
    finally:
        connection.close()
