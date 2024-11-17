# Healthcare Management System

A terminal-based Healthcare Management System designed to simplify and streamline patient-doctor interactions. Built with Python and MongoDB, this project allows doctors and patients to manage appointments, patient records, and doctor-patient relationships efficiently.

## Features

#### General

- Secure login and signup for doctors and patients.
- Role-based functionalities for doctors and patients.

#### Doctors

- Add patient details to their managed list.
- View all patients under their care, including patient details and appointment history.

#### Patients

- View their personal details and medical history.
- Book appointments with available doctors.

#### Database

- Uses MongoDB for persistent storage.
- Stores:
    - Patient data: Personal details, medical history, appointments.
    - Doctor data: Specializations, managed patient lists.

## File Structure

``` bash []
healthcare_management/
├── db.py                  # Handles database operations (MongoDB)
├── main.py                # Entry point of the application
├── auth.py                # Login and signup functionality
├── doctor_dashboard.py    # Doctor-related operations
├── patient_dashboard.py   # Patient-related operations
└── README.md              # Project documentation

```

## Technologies Used

- Programming Language: `Python`
- Database: `MongoDB`
- Modules:
    - `pymongo`: For interacting with `MongoDB`.

## Setup Instructions

1. **Clone the Repository:**

    ``` bash
    git clone https://github.com/shubhash-singh/L_and_T-Healthcare_Management_System.git
    cd L_and_T-Healthcare_Management_System
    ```

2. **Install Dependencies:** Ensure you have Python installed. Install the required module:

    ``` bash[]
    pip install pymongo
    ```

3. ***Start MongoDB:** Start the MongoDB service on your system:

    ``` bash []
    mongod
    ```

4. **Run the Application:** Execute the main script:

``` bash []
    python main.py
```

## Usage

1. Login or Signup:
    - Choose whether to log in or sign up.
    - Specify whether you are a doctor or a patient.

2. Doctor Functionalities:
    - Add patients to your list.
    - View the details of all managed patients.

3. Patient Functionalities:
    - View your personal details and appointment history.
    - Book appointments with available doctors.

## Example Usage

#### Doctor Login Flow:

1. Login as a doctor.
2. Add patient details using their username.
3. View the list of patients under your care.

#### Patient Login Flow:

1. Login as a patient.
2. View your details.
3. Book an appointment with an available doctor.

## Contributing

1. Fork this repository.
2. Create a feature branch: git checkout -b feature-name.
3. Commit your changes: git commit -m 'Add some feature'.
4. Push to the branch: git push origin feature-name.
5. Open a pull request.

## Contact

- Developer: Shubhash Singh
- Email: <subhashsingh2059@gmail.com>
- GitHub: shubhash-singh
- Linkdin: <https://www.linkedin.com/in/shubhash-singh-124254215/>
- Phone: +91 93815 60406
- Leetcode: <https://leetcode.com/u/Shubhash_Singh/>
