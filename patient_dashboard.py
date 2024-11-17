from db import find_all_records, update_record

def patient_dashboard(patient):
    while True:
        print(f"\nPatient Dashboard - {patient['username']}")
        print("1. View My Details")
        print("2. Book Appointment")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_my_details(patient)
        elif choice == "2":
            book_appointment(patient)
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def view_my_details(patient):
    print("\nMy Details:")
    print(f"Name: {patient['name']}")
    print(f"Age: {patient['age']}")
    print(f"Gender: {patient['gender']}")
    print(f"Medical History: {patient['medical_history']}")
    print(f"Appointments: {patient['appointments']}")

def book_appointment(patient):
    doctors = find_all_records("doctors")
    if not doctors:
        print("No doctors available.")
        return

    print("Available Doctors:")
    for i, doctor in enumerate(doctors, start=1):
        print(f"{i}. {doctor['username']} (Specialization: {doctor['specialization']})")

    choice = int(input("Select a doctor by number: ")) - 1
    if choice < 0 or choice >= len(doctors):
        print("Invalid choice.")
        return

    selected_doctor = doctors[choice]
    appointment = {
        "doctor_username": selected_doctor["username"],
        "doctor_specialization": selected_doctor["specialization"]
    }
    patient["appointments"].append(appointment)
    update_record("patients", {"username": patient["username"]}, {"appointments": patient["appointments"]})
    print("Appointment booked successfully.")
