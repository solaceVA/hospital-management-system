import pymysql

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='Phoenixwalnut@9094',
        database='hdb'
    )

def get_medicines():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM medications')
    medicines = cursor.fetchall()
    if not medicines:
        print("No medicines found.")
    else:
        for i in medicines:
            print(i)
    conn.close()

def add_medicine(data):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO medications (medicine_name, dosage, frequency, price) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (data['name'],data['dosage'],data['frequency'],data['price']))
    conn.commit()
    conn.close()

def update_price(med_id, new_price):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE medications SET price = %s WHERE medicine_id = %s"
    cursor.execute(sql, (new_price, med_id))
    conn.commit()
    conn.close()

def delete_medicine(med_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM medications WHERE medicine_id = %s"
    cursor.execute(sql, med_id)
    conn.commit()
    conn.close()

def update_dosage(med_id, new_dosage):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE medications SET dosage = %s WHERE medicine_id = %s"
    cursor.execute(sql, (new_dosage, med_id))
    conn.commit()
    conn.close()

def update_frequency(med_id, new_frequency):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE medications SET frequency = %s WHERE medicine_id = %s"
    cursor.execute(sql, (new_frequency, med_id))
    conn.commit()
    conn.close()