import db
from doctor_dashboard import doctor_dashboard
from patient_dashboard import patient_dashboard

def login():
    print("\n*****Login*****")
    role = input("Login as (doctor[doc]/patient[pat]): ").strip().lower()
    
    if role == "doctor" or role == "doc":
        username = input("Enter username: ").strip()
        
        doctor = db.find_record("doctors", {"username": username})
        if doctor:
            doctor_dashboard(doctor)
            return
        else:
            print("Doctor not found. Please signup.")
    elif role == "patient" or role == "pat":
        username = input("Enter username: ").strip()
        
        patient = db.find_record("patients", {"username": username})
        if patient:
            patient_dashboard(patient)
            return
        else:
            print("Patient not found. Please signup.")
    else:
        print("Invalid role. Try again.")
        login()

def signup():
    print("\n*****Signup*****")
    role = input("Login as (doctor[doc]/patient[pat]): ").strip().lower()
    

    if role == "doctor" or role == 'doc':
        username = input("Enter a unique username: ").strip()
        
        specialization = input("Enter your specialization: ").strip()
        doctor = {
            "username": username,
            "specialization": specialization,
            "patients": []
        }
        db.insert_record("doctors", doctor)
        print("Doctor signup successful.")
    elif role == "patient" or role == 'doc':
        username = input("Enter a unique username: ").strip()
        
        name = input("Enter your name: ").strip()
        age = int(input("Enter your age: "))
        gender = input("Enter your gender: ").strip()
        medical_history = input("Enter your medical history: ").strip()
        patient = {
            "username": username,
            "name": name,
            "age": age,
            "gender": gender,
            "medical_history": medical_history,
            "appointments": []
        }
        db.insert_record("patients", patient)
        print("Patient signup successful.")
    else:
        print("Invalid role. Try again.")
        signup()
