import pymysql

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='Ajwin2008',
        database='hdb'
    )

def create_bill(data):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO Bills (Patient_ID, Bill_Date, Payment_Status, Amount) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (data['patient_id'],data['bill_date'],data['payment_status'],data['amount'],))
            connection.commit()
            print("Bill created successfully.")
    finally:
        connection.close()

def get_all_bills():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Bills"
            cursor.execute(sql)
            bills = cursor.fetchall()
            if not bills: 
                print("No bills found.")
            else:
                for bill in bills:
                    print(bill)  # Print each bill entry for visibility
    finally:
        connection.close()

def get_bill(data):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Bills WHERE Bill_ID = %s"
            cursor.execute(sql, (data,))
            bill = cursor.fetchone()
            if not bill:
                print("Bill not found.")
            else:
                print(bill)  # Print the bill details
    finally:
        connection.close()

def update_amount(bill_id, amount):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE Bills SET Amount = %s WHERE Bill_ID = %s"
            cursor.execute(sql, (amount, bill_id))
            connection.commit()
        print("Bill amount updated successfully.")
    finally:
        connection.close()

def update_status(bill_id, status):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE Bills SET Payment_Status = %s WHERE Bill_ID = %s"
            cursor.execute(sql, (status, bill_id))
            connection.commit()
        print("Bill status updated successfully.")
    finally:
        connection.close()
