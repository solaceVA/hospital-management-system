import streamlit as st
import pandas as pd
from db import *

def main():
    st.title("Hospital Management System")
    tab1, tab2, tab3 = st.tabs(["Doctors", "Patients", "Appointments"])
    with tab1:
        st.header("Doctors")
        option = st.selectbox("Select an option", ["Register Doctor", "Delete Doctor", "Doctors List"])
        if option == "Register Doctor":
            first_name = st.text_input("Doctor First Name")
            last_name = st.text_input("Doctor Last Name")
            phone_number = st.text_input("Doctor Phone Number")
            email = st.text_input("Doctor Email")
            dept_id = st.number_input("Department ID", min_value=1)
            password = st.text_input("Doctor Password", type="password")
            if st.button("Register as Doctor"):
                data = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'phone_number': phone_number,
                    'email': email,
                    'dept_id': dept_id,
                    'password': password
                }
                register_doctor(data)
                st.success("Doctor registered successfully.")
                first_name = ""
                last_name = ""
                phone_number = ""
                email = ""
                dept_id = 1
                password = ""
        elif option == "Delete Doctor":
            doctor_id = st.number_input("Doctor ID", min_value=0)
            if st.button("Delete Doctor"):
                delete_doctor(doctor_id)
                st.success("Doctor deleted successfully.")
                doctor_id = 0
        elif option == "Doctors List":
            doctors = get_all_doctors() 
            if st.button("Get Doctors"):
                df = pd.DataFrame(doctors, columns=["Doctor ID", "First Name", "Last Name", "Phone Number", "Email", "Dept ID"])
                st.dataframe(df)

    with tab2:
        st.header("Patients")
        option = st.selectbox("Select an option", ["Register Patient", "Delete Patient", "Patients List"])
        if option == "Register Patient":
            first_name = st.text_input("First Name")
            last_name = st.text_input("Last Name")
            dob = st.date_input("Date of Birth")
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            phone_number = st.text_input("Phone Number")
            email = st.text_input("Email")
            address = st.text_input("Address")
            password = st.text_input("Password", type="password")
            if st.button("Register"):
                data = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'dob': dob,
                    'gender': gender,
                    'phone_number': phone_number,
                    'email': email,
                    'address': address,
                    'password': password
                }
                register_patient(data)
                st.success("Patient registered successfully.")
                first_name = ""
                last_name = ""
                dob = ""
                gender = ""
                phone_number = ""
                email = ""
                address = ""
                password = ""
        elif option == "Delete Patient":
            patient_id = st.number_input("Patient ID", min_value=0)
            if st.button("Delete"):
                delete_patient(patient_id)
                st.success("Patient deleted successfully.")
        elif option == "Patients List":
            patients = get_all_patients()
            if st.button("Get Patients"):
                df = pd.DataFrame(patients, columns=["Patient ID", "First Name", "Last Name","Date_Of_Birth", "Gender", "Phone Number", "Email", "Address"])
                st.dataframe(df)

    with tab3:
        st.header("Appointments")
        option = st.selectbox("Select an option", ["Create Appointment", "Update Appointment Date", "Update Appointment Time", "Update Appointment Status", "Delete Appointment", "Appointments List"])
        if option == "Create Appointment":
            patient_id = st.number_input("Patient ID", min_value=0)
            doctor_id = st.number_input("Doctor ID", min_value=0)
            date = st.date_input("Appointment Date")
            time = st.time_input("Appointment Time" )
            if st.button("Create Appointment"):
                data = {
                    'patient_id': patient_id,
                    'doctor_id': doctor_id,
                    'date': date,
                    'time': time
                }
                create_apt(data)
                st.success("Appointment created successfully.")
                patient_id = 0
                doctor_id = 0
                date = None
                time = None
        elif option == "Update Appointment Date":
            apt_id = st.number_input("Appointment ID", min_value=0)
            date = st.date_input("New Appointment Date")
            if st.button("Update Appointment Date"):
                update_aptdate(date, apt_id)
                st.success("Appointment updated successfully.")
                apt_id = 0
                date = None
        elif option == "Update Appointment Time":
            apt_id = st.number_input("Appointment ID", min_value=0)
            time = st.time_input("New Appointment Time")
            if st.button("Update Appointment Time"):
                update_apttime(time, apt_id)
                st.success("Appointment updated successfully.")
                apt_id = 0
                time = None
        elif option == "Update Appointment Status":
            apt_id = st.number_input("Appointment ID", min_value=0)
            status = st.selectbox("New Appointment Status", ["Pending", "Completed"])
            if st.button("Update Appointment Status"):
                update_aptstatus(status, apt_id)
                st.success("Appointment status updated successfully.")
                apt_id = 0
                status = "Pending"
        elif option == "Delete Appointment":
            apt_id = st.number_input("Appointment ID", min_value=0)
            if st.button("Delete Appointment"):
                delete_apt(apt_id)
                st.success("Appointment deleted successfully.")
                apt_id = 0
        elif option == "Appointments List":
            appointments = get_all_apts()
            if st.button("Get Appointments"):
                df = pd.DataFrame(appointments, columns=["Appointment ID", "Patient ID", "Doctor ID", "Date", "Time", "Status"])
                df["Time"] = df["Time"].apply(lambda x: (x + pd.Timestamp('1970-01-01')).time() if isinstance(x, pd.Timedelta) else x.strftime("%H:%M"))
                st.dataframe(df)

main()
