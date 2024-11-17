from auth import login, signup

def main():
    while True:
        print("\nWelcome to Healthcare Management System")
        print("1. Login")
        print("2. Signup")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            login()
        elif choice == "2":
            signup()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
