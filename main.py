from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Phoenixwalnut@9094@localhost/hdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

class Patient(db.Model):
    __tablename__ = 'patients'
    Patient_ID = db.Column(db.Integer, primary_key=True)
    First_Name = db.Column(db.String(20))
    Last_Name = db.Column(db.String(20))
    Date_of_Birth = db.Column(db.Date)
    Gender = db.Column(db.String(6))
    Phone_Number = db.Column(db.String(100))
    Email = db.Column(db.String(100))
    Address = db.Column(db.Text)

class Department(db.Model):
    __tablename__ = 'departments'
    Dept_ID = db.Column(db.Integer, primary_key=True)
    Department_Name = db.Column(db.String(100))
    Location = db.Column(db.String(100))

class Doctor(db.Model):
    __tablename__ = 'doctors'
    Doctor_ID = db.Column(db.Integer, primary_key=True)
    Dept_ID = db.Column(db.Integer, db.ForeignKey('departments.Dept_ID', ondelete='CASCADE'))
    First_Name = db.Column(db.String(100))
    Last_Name = db.Column(db.String(100))
    Phone_Number = db.Column(db.String(100))
    Email = db.Column(db.String(100))
    department = db.relationship('Department', backref='doctors')

@app.route('/register/patients', methods=['POST'])
def register_patient():
    data = request.get_json()
    new_patient = Patient(
        First_Name=data['first_name'],
        Last_Name=data['last_name'],
        Date_of_Birth=data['dob'],
        Gender=data['gender'],
        Address=data['address'],
        Phone_Number=data['phone_number'],
        Email=data['email']
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify(message="Patient added"), 201 

@app.route('/register/doctors', methods=['POST'])
def register_doctor():
    data = request.get_json()
    new_doctor = Doctor(
        First_Name=data['first_name'],
        Last_Name=data['last_name'],
        Phone_Number=data['phone_number'],
        Email=data['email'],
        Dept_ID=data['dept_id']
    )
    db.session.add(new_doctor)
    db.session.commit()
    return jsonify(message="Doctor added"), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    patient = Patient.query.filter_by(Email=data['email']).first()
    if patient:
        access_token = create_access_token(identity={'user_id': patient.Patient_ID, 'role': 'patient'})
        return jsonify(access_token=access_token), 200

    doctor = Doctor.query.filter_by(Email=data['email']).first()
    if doctor:
        access_token = create_access_token(identity={'user_id': doctor.Doctor_ID, 'role': 'doctor'})
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Bad email"}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(msg="Welcome to the protected route!")

if __name__ == '__main__':
    app.run(debug=False)
