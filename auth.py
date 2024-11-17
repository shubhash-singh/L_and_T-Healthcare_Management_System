from db import insert_record, find_record
from doctor_dashboard import doctor_dashboard
from patient_dashboard import patient_dashboard

def login():
    print("\nLogin")
    role = input("Login as (doctor[doc]/patient[pat]): ").strip().lower()
    
    if role == "doctor" or role == "doc":
        username = input("Enter username: ").strip()
        
        doctor = find_record("doctors", {"username": username})
        if doctor:
            doctor_dashboard(doctor)
        else:
            print("Doctor not found. Please signup.")
    elif role == "patient" or role == "pat":
        username = input("Enter username: ").strip()
        
        patient = find_record("patients", {"username": username})
        if patient:
            patient_dashboard(patient)
        else:
            print("Patient not found. Please signup.")
    else:
        print("Invalid role. Try again.")

def signup():
    print("\nSignup")
    role = input("Signup as (doctor/patient): ").strip().lower()
    username = input("Enter a unique username: ").strip()

    if role == "doctor":
        specialization = input("Enter your specialization: ").strip()
        doctor = {
            "username": username,
            "specialization": specialization,
            "patients": []
        }
        insert_record("doctors", doctor)
        print("Doctor signup successful.")
    elif role == "patient":
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
        insert_record("patients", patient)
        print("Patient signup successful.")
    else:
        print("Invalid role. Try again.")
