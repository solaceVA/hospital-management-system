import streamlit as st
import pandas as pd
from db import *

def main():
    st.title("Hospital Management System")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Doctors", "Patients", "Appointments", "Bills", "Medications"])
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
                df = pd.DataFrame(doctors, columns=["Doctor ID", "Name", "Phone Number", "Email", "Dept ID", "Department Name"])
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

    with tab4:
        st.header("Bills")
        option = st.selectbox("Select an option", ["Create Bill", "Update Bill Amount", "Update Bill Status", "Get Bill", "Get All Bills", "Get Total Amount"])
        if option == "Create Bill":
            create_patient_id = st.number_input("Patient ID", min_value=0, key="create_patient_id")
            bill_date = st.date_input("Bill Date")
            payment_status = st.selectbox("Payment Status", ["Unpaid","Partial", "Paid"])
            amount = st.number_input("Amount", min_value=0.0, key="create_amount")
            if st.button("Create Bill"):
                data = {
                    'patient_id': create_patient_id,
                    'bill_date': bill_date,
                    'payment_status': payment_status,
                    'amount': amount
                }
                create_bill(data)
                st.success("Bill created successfully.")
                create_patient_id = 0
                bill_date = None
                payment_status = "Unpaid"
                amount = 0.0
        elif option == "Update Bill Amount":
            update_bill_id = st.number_input("Bill ID", min_value=0, key="update_bill_id")
            update_amount = st.number_input("New Amount", min_value=0.0, key="update_amount")
            if st.button("Update Bill Amount"):
                update_amount(update_bill_id, update_amount)
                st.success("Bill amount updated successfully.")
                update_bill_id = 0
                update_amount = 0.0
        elif option == "Update Bill Status":
            update_status_bill_id = st.number_input("Bill ID", min_value=0, key="update_status_bill_id")
            status = st.selectbox("New Payment Status", ["Paid", "Unpaid"])
            if st.button("Update Bill Status"):
                update_status(update_status_bill_id, status)
                st.success("Bill status updated successfully.")
                update_status_bill_id = 0
                status = "Unpaid"
        elif option == "Get Bill":
            get_bill_id = st.number_input("Bill ID", min_value=0, key="get_bill_id")
            if st.button("Get Bill"):
                bill = get_bill(get_bill_id)
                if bill:
                    st.write(bill)
        elif option == "Get All Bills":
            if st.button("Get All Bills"):
                bills = get_all_bills()
                if bills:
                    df = pd.DataFrame(bills, columns=["Bill ID", "Patient ID", "Bill Date", "Payment Status", "Amount"])
                    st.dataframe(df)
        elif option == "Get Total Amount":
            total_patient_id = st.number_input("Patient_ID", min_value=0, key="total_patient_id")
            if st.button("Get Total Amount"):
                total = get_totals(total_patient_id)
                st.write(f"Total amount: {total}")
    
    with tab5:
        st.header("Medications")
        meds = get_medicines()
        if meds:
            df = pd.DataFrame(meds, columns=["Medicine ID", "Name", "Dosage", "Frequency", "Price"])
            st.dataframe(df)
        st.subheader("Add a new medicine")
        name = st.text_input("Medicine Name")
        dosage = st.text_input("Dosage")
        frequency = st.text_input("Frequency")
        price = st.number_input("Price", min_value=0.0)
        if st.button("Add Medicine"):
            data = {
                'name': name,
                'dosage': dosage,
                'frequency': frequency,
                'price': price
            }
            add_medicine(data)
            st.success("Medicine added successfully.")
            name = ""
            dosage = ""
            frequency = ""
            price = 0.0
        st.subheader("Update medicine price")
        med_id = st.number_input("Medicine ID", min_value=0)
        new_price = st.number_input("New Price", min_value=0.0)
        if st.button("Update Price"):
            update_price(med_id, new_price)
            st.success("Medicine price updated successfully.")
            med_id = 0
            new_price = 0.0
        st.subheader("Delete a medicine")
        med_id = st.number_input("MEDICINE ID", min_value=0)
        if st.button("Delete Medicine"):
            delete_medicine(med_id)
            st.success("Medicine deleted successfully.")
            med_id = 0
        st.subheader("Update medicine dosage")
        med_id = st.number_input("Medicine id", min_value=0)
        new_dosage = st.text_input("New Dosage")
        if st.button("Update Dosage"):
            update_dosage(med_id, new_dosage)
            st.success("Medicine dosage updated successfully.")
            med_id = 0
            new_dosage = ""
        st.subheader("Update medicine frequency")
        med_id = st.number_input("medicine ID", min_value=0)
        new_frequency = st.text_input("New Frequency")
        if st.button("Update Frequency"):
            update_frequency(med_id, new_frequency)
            st.success("Medicine frequency updated successfully.")
            med_id = 0
            new_frequency = ""
    with tab6:
        st.header("Prescriptions")
        functionality = st.selectbox("Select a functionality", ["Create Prescription", "Get Prescription", "Update Quantity", "Update End Date"])
        if functionality == "Create Prescription":
            st.subheader("Create a new prescription")
            record_id = st.number_input("Medical Record ID", min_value=0)
            medicine_id = st.number_input("medicine id", min_value=0)
            quantity = st.number_input("Quantity", min_value=0)
            start_date = st.date_input("Start Date")
            end_date = st.date_input("End Date")
            if st.button("Create Prescription"):
                data = {
                    'record_id': record_id,
                    'medicine_id': medicine_id,
                    'quantity': quantity,
                    'start_date': start_date,
                    'end_date': end_date
                }
                create_prescription(data)
                st.success("Prescription created successfully.")
                record_id = 0
                medicine_id = 0
                quantity = 0
                start_date = None
                end_date = None

        elif functionality == "Get Prescription":
            st.subheader("Get a prescription")
            record_id = st.number_input("Medical Record ID", min_value=0)
            medicine_id = st.number_input("MEDICINE Id", min_value=0)
            if st.button("Get Prescription"):
                get_prescription(record_id, medicine_id)

        elif functionality == "Update Quantity":
            st.subheader("Update medicine quantity")
            record_id = st.number_input("Medical Record Id", min_value=0)
            medicine_id = st.number_input("Medicine Id", min_value=0)
            quantity = st.number_input("New Quantity", min_value=0)
            if st.button("Update Quantity"):
                update_quantity(record_id, medicine_id, quantity)
                st.success("Medicine quantity updated successfully.")
                record_id = 0
                medicine_id = 0
                quantity = 0

        elif functionality == "Update End Date":
            st.subheader("Update end date")
            record_id = st.number_input("Medical Record id", min_value=0)
            medicine_id = st.number_input("MEDICINe id", min_value=0)
            end_date = st.date_input("New End Date")
            if st.button("Update End Date"):
                update_end_date(record_id, medicine_id, end_date)
                st.success("End date updated successfully.")
                record_id = 0
                medicine_id = 0
                end_date = None
    with tab7:
        st.header("Medical Records")
        records = get_all_records()
        if records:
            df = pd.DataFrame(records, columns=["Record ID", "Patient ID", "Doctor ID", "Record Date", "Diagnosis", "Treatment"])
            st.dataframe(df)
        else:
            st.write("No medical records found.")
        st.subheader("Create a new medical record")
        patient_id = st.number_input("Patient_ID", min_value=0)
        doctor_id = st.number_input("Doctor_ID", min_value=0)
        date = st.date_input("Record Date")
        diagnosis = st.text_area("Diagnosis")
        treatment = st.text_area("Treatment")
        if st.button("Create Record"):
            data = {
                'patient_id': patient_id,
                'doctor_id': doctor_id,
                'date': date,
                'diagnosis': diagnosis,
                'treatment': treatment
            }
            create_record(data)
            st.success("Record created successfully.")
            patient_id = 0
            doctor_id = 0
            date = None
            diagnosis = ""
            treatment = ""
        st.subheader("Update diagnosis")
        record_id = st.number_input("Record ID", min_value=0)
        diagnosis = st.text_area("New Diagnosis")
        if st.button("Update Diagnosis"):
            update_diagnosis(record_id, diagnosis)
            st.success("Diagnosis updated successfully.")
            record_id = 0
            diagnosis = ""
        st.subheader("Update treatment")
        record_id = st.number_input("Record_ID", min_value=0)
        treatment = st.text_area("New Treatment")
        if st.button("Update Treatment"):
            update_treatment(record_id, treatment)
            st.success("Treatment updated successfully.")
            record_id = 0
            treatment = ""
main()
