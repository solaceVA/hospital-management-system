import bcrypt
import pymysql

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='Phoenixwalnut@9094',
        database='hdb'
    )

def register_patient(data):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            hashed_password = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt()).decode('utf-8')
            sql = """
                INSERT INTO patients (First_Name, Last_Name, Date_of_Birth, Gender, Phone_Number, Email, Address, Password)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                data['first_name'], data['last_name'], data['dob'], data['gender'],
                data['phone_number'], data['email'], data['address'], hashed_password
            ))
            connection.commit()
            print("Patient registered successfully.")
    finally:
        connection.close()

def register_doctor(data):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            hashed_password = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            sql = """
                INSERT INTO doctors (First_Name, Last_Name, Phone_Number, Email, Dept_ID, Password)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                data['first_name'], data['last_name'], data['phone_number'],
                data['email'], data['dept_id'], hashed_password
            ))
            connection.commit()
            print("Doctor registered successfully.")
    finally:
        connection.close()

def delete_patient(patient_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM patients WHERE patient_id = %s"
            cursor.execute(sql, (patient_id,))
            connection.commit()
        print("Patient deleted successfully.")
    finally:
        connection.close()

def delete_doctor(doctor_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM doctors WHERE doctor_id = %s"
            cursor.execute(sql, (doctor_id,))
            connection.commit()
        print("Doctor deleted successfully.")
    finally:
        connection.close()
        
def login(email, password):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT Patient_ID, Password FROM patients WHERE Email = %s", (email,))
            patient = cursor.fetchone()
            if patient and bcrypt.checkpw(password.encode(), patient[1]):
                return {"user_id": patient[0], "role": "patient"}
            
            cursor.execute("SELECT Doctor_ID, Password FROM doctors WHERE Email = %s", (email,))
            doctor = cursor.fetchone()
            if doctor and bcrypt.checkpw(password.encode(), doctor[1]):
                return {"user_id": doctor[0], "role": "doctor"}
            
            return {"msg": "Invalid email or password"}
    finally:
        connection.close()