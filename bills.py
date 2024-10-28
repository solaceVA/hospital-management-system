import pymysql

def get_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ajwin2008',
        database='hdb'
        )
    return connection


def create_bill(patient_id, amount, status):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO bills (patient_id, amount, status) VALUES (%s, %s, %s)"
            cursor.execute(sql, (patient_id, amount, status))
            connection.commit()
            print("Bill created successfully.")
    finally:
        connection.close()

def get_all_bills():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM bills"
            cursor.execute(sql)
            bills = cursor.fetchall()
            if not bills: 
                print("No bills found.")
    finally:
        connection.close()

def get_bill(bill_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM bills WHERE id = %s"
            cursor.execute(sql, (bill_id,))
            bill = cursor.fetchone()
            if not bill:
                print("Bill not found.")
    finally:
        connection.close()

def update_bill(bill_id, amount=None, status=None):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            updates = []
            params = []
            if amount is not None:
                updates.append("amount = %s")
                params.append(amount)
            if status is not None:
                updates.append("status = %s")
                params.append(status)
            
            if updates:
                sql = "UPDATE bills SET {', '.join(updates)} WHERE id = %s"
                params.append(bill_id)
                cursor.execute(sql, params)
                connection.commit()
                print("Bill updated successfully.")
    finally:
        connection.close()
