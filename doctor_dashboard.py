from db import find_record, update_record

def doctor_dashboard(doctor):
    while True:
        print(f"\nDoctor Dashboard - {doctor['username']}")
        print("1. Add Patient Details")
        print("2. View All Patients")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_patient_details(doctor)
        elif choice == "2":
            view_all_patients(doctor)
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def add_patient_details(doctor):
    patient_username = input("Enter patient's username: ").strip()
    patient = find_record("patients", {"username": patient_username})

    if not patient:
        print("Patient not found.")
        return

    if patient_username not in doctor["patients"]:
        doctor["patients"].append(patient_username)
        update_record("doctors", {"username": doctor["username"]}, {"patients": doctor["patients"]})
    print("Patient successfully added to doctor's list.")

def view_all_patients(doctor):
    print("\nList of Patients:")
    for patient_username in doctor.get("patients", []):
        patient = find_record("patients", {"username": patient_username})
        if patient:
            print(f"- Name: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}, Appointments: {patient['appointments']}")
        else:
            print(f"- Username: {patient_username} (Details not found)")
