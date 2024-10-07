from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Phoenixwalnut@9094@localhost/HospitalDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

from flask_migrate import Migrate
migrate = Migrate(app, db)

class Patient(db.Model):
    __tablename__ = 'patients'
    Patient_ID = db.Column(db.Integer, primary_key=True)
    First_Name = db.Column(db.String(100))
    Last_Name = db.Column(db.String(100))
    Date_of_Birth = db.Column(db.Date)
    Gender = db.Column(db.String(10))
    Address = db.Column(db.Text)
    Username = db.Column(db.String(50), unique=True, nullable=False)
    Password = db.Column(db.String(100), nullable=False)

class Doctor(db.Model):
    __tablename__ = 'doctors'
    Doctor_ID = db.Column(db.Integer, primary_key=True)
    First_Name = db.Column(db.String(100))
    Last_Name = db.Column(db.String(100))
    Specialisation = db.Column(db.String(100))
    Username = db.Column(db.String(50), unique=True, nullable=False)
    Password = db.Column(db.String(100), nullable=False)

@app.route('/register', methods=['POST'])
@jwt_required()
def register(s):
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    if s == 'patient':
        new_patient = Patient(
            First_Name=data['first_name'],
            Last_Name=data['last_name'],
            Date_of_Birth=data['dob'],
            Gender=data['gender'],
            Address=data['address'],
            Username=data['username'],
            Password=hashed_password
        )
        db.session.add(new_patient)
        db.session.commit()
        return jsonify(message="Patient added"), 201 

    elif s == 'doctor':
        new_doctor = Doctor(
            First_Name=data['first_name'],
            Last_Name=data['last_name'],
            Specialisation=data['specialisation'],
            Username=data['username'],
            Password=hashed_password
        )
        db.session.add(new_doctor)
        db.session.commit()
        return jsonify(message="Doctor added"), 201
    
    else:
        return jsonify(message="Error"), 400
    
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    patient = Patients.query.filter_by(Username=data['username']).first()
    if patient and bcrypt.check_password_hash(patient.Password, data['password']):
        access_token = create_access_token(identity={'user_id': patient.Patient_ID, 'role': 'patient'})
        return jsonify(access_token=access_token), 200

    doctor = Doctors.query.filter_by(Username=data['username']).first()
    if doctor and bcrypt.check_password_hash(doctor.Password, data['password']):
        access_token = create_access_token(identity={'user_id': doctor.Doctor_ID, 'role': 'doctor'})
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Bad username or password"}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(msg="Welcome to the protected route!")

if __name__ == '__main__':
    app.run(debug=False)
