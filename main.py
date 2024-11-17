from db import insert_record, find_record, update_record, delete_record

def main_menu():
    while True:
        print("\nHealthcare Management System")
        print("1. Manage Patient Records")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manage_patients()
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def manage_patients():
    print("\n1. Add Patient")
    print("2. View Patient")
    print("3. Update Patient")
    print("4. Delete Patient")
    print("5. Back to Main Menu")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        view_patient()
    elif choice == "3":
        update_patient()
    elif choice == "4":
        delete_patient()
    elif choice == "5":
        return
    else:
        print("Invalid choice. Please try again.")

def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender: ")
    medical_history = input("Enter patient medical history: ")

    patient = {
        "name": name,
        "age": age,
        "gender": gender,
        "medical_history": medical_history,
    }

    insert_record("patients", patient)

def view_patient():
    name = input("Enter patient name to search: ")
    patient = find_record("patients", {"name": name})

    if patient:
        print("\nPatient Details:")
        print(f"Name: {patient['name']}")
        print(f"Age: {patient['age']}")
        print(f"Gender: {patient['gender']}")
        print(f"Medical History: {patient['medical_history']}")
    else:
        print("Patient not found.")

def update_patient():
    name = input("Enter patient name to update: ")
    field = input("Enter the field to update (name, age, gender, medical_history): ")
    new_value = input(f"Enter the new value for {field}: ")

    if field == "age":
        new_value = int(new_value)

    update_record("patients", {"name": name}, {field: new_value})

def delete_patient():
    name = input("Enter patient name to delete: ")
    delete_record("patients", {"name": name})

if __name__ == "__main__":
    main_menu()
