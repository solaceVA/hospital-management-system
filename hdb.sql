CREATE DATABASE hdb;
USE hdb;

CREATE TABLE Patients (
    Patient_ID INT PRIMARY KEY AUTO_INCREMENT,
    First_Name VARCHAR(20),
    Last_Name VARCHAR(20),
    Date_of_Birth DATE,
    Gender VARCHAR(6),
    Phone_Number VARCHAR(100),
    Email VARCHAR(100),
    Address TEXT
);

CREATE TABLE Departments (
    Dept_ID INT PRIMARY KEY AUTO_INCREMENT,
    Department_Name VARCHAR(100),
    Location VARCHAR(100)
);

CREATE TABLE Doctors (
    Doctor_ID INT PRIMARY KEY AUTO_INCREMENT,
    Dept_ID INT,
    First_Name VARCHAR(100),
    Last_Name VARCHAR(100),
    Phone_Number VARCHAR(100),
    Email VARCHAR(100),
    FOREIGN KEY (Dept_ID) REFERENCES Departments(Dept_ID) ON DELETE CASCADE
);

CREATE TABLE Appointments (
    Appointment_ID INT PRIMARY KEY AUTO_INCREMENT,
    Patient_ID INT,
    Doctor_ID INT,
    Appointment_DateTime DATETIME,
    Appointment_Status ENUM('Completed', 'Upcoming') NOT NULL DEFAULT 'Upcoming',
    FOREIGN KEY (Patient_ID) REFERENCES Patients(Patient_ID) ON DELETE CASCADE,
    FOREIGN KEY (Doctor_ID) REFERENCES Doctors(Doctor_ID) ON DELETE CASCADE
);

CREATE TABLE Medical_Record (
    Record_ID INT PRIMARY KEY AUTO_INCREMENT,
    Patient_ID INT,
    Doctor_ID INT,
    Record_Date DATE,
    Diagnosis TEXT,
    Treatment TEXT,
    FOREIGN KEY (Patient_ID) REFERENCES Patients(Patient_ID) ON DELETE CASCADE,
    FOREIGN KEY (Doctor_ID) REFERENCES Doctors(Doctor_ID) ON DELETE CASCADE
);

CREATE TABLE Medications (
    Medicine_ID INT PRIMARY KEY AUTO_INCREMENT,
    Medicine_Name VARCHAR(100),
    Dosage VARCHAR(50),
    Frequency VARCHAR(50)
);

CREATE TABLE Prescriptions (
    Prescription_ID INT PRIMARY KEY AUTO_INCREMENT,
    Record_ID INT,
    Medicine_ID INT,
    Quantity INT,
    Start_Date DATE,
    End_Date DATE,
    FOREIGN KEY (Record_ID) REFERENCES Medical_Record(Record_ID) ON DELETE CASCADE,
    FOREIGN KEY (Medicine_ID) REFERENCES Medications(Medicine_ID) ON DELETE CASCADE
);

CREATE TABLE Bills (
    Bill_ID INT PRIMARY KEY AUTO_INCREMENT,
    Patient_ID INT,
    Bill_Date DATE,
    Payment_Status ENUM('Paid', 'Partial', 'Unpaid') NOT NULL DEFAULT 'Unpaid',
    Amount DECIMAL(10, 2),
    FOREIGN KEY (Patient_ID) REFERENCES Patients(Patient_ID) ON DELETE CASCADE
);
