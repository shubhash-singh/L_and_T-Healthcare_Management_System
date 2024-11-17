from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import pymongo

# MongoDB setup
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["healthcare_management"]

# Screens for different sections

class MainMenuScreen(Screen):
    pass

class AddPatientScreen(Screen):
    def add_patient(self):
        patient = {
            "name": self.ids.patient_name.text,
            "age": int(self.ids.patient_age.text),
            "gender": self.ids.patient_gender.text,
            "medical_history": self.ids.medical_history.text,
            "allergies": self.ids.allergies.text,
            "medications": self.ids.medications.text,
        }
        db.patients.insert_one(patient)
        self.ids.message_label.text = "Patient added successfully."

class ViewPatientsScreen(Screen):
    def on_pre_enter(self):
        self.ids.patient_list.text = ""
        patients = db.patients.find()
        for patient in patients:
            self.ids.patient_list.text += f"{patient['name']} - {patient['age']} years\n"

class AddAppointmentScreen(Screen):
    def add_appointment(self):
        appointment = {
            "patient_name": self.ids.appointment_patient_name.text,
            "doctor": self.ids.doctor_name.text,
            "date": self.ids.appointment_date.text,
            "time": self.ids.appointment_time.text
        }
        db.appointments.insert_one(appointment)
        self.ids.appointment_message_label.text = "Appointment scheduled successfully."

class ViewAppointmentsScreen(Screen):
    def on_pre_enter(self):
        self.ids.appointment_list.text = ""
        appointments = db.appointments.find()
        for appointment in appointments:
            self.ids.appointment_list.text += f"{appointment['patient_name']} with {appointment['doctor']} on {appointment['date']} at {appointment['time']}\n"

class AddBillingScreen(Screen):
    def add_billing(self):
        billing = {
            "patient_name": self.ids.billing_patient_name.text,
            "amount": float(self.ids.billing_amount.text),
            "insurance_claimed": self.ids.insurance_claimed.text,
            "paid": self.ids.paid_status.text
        }
        db.billing.insert_one(billing)
        self.ids.billing_message_label.text = "Billing record added successfully."

class ViewBillingScreen(Screen):
    def on_pre_enter(self):
        self.ids.billing_list.text = ""
        billing_records = db.billing.find()
        for record in billing_records:
            self.ids.billing_list.text += f"{record['patient_name']} - Amount: {record['amount']} Paid: {record['paid']}\n"

class AnalyticsScreen(Screen):
    def display_analytics(self):
        total_patients = db.patients.count_documents({})
        total_appointments = db.appointments.count_documents({})
        total_billing = db.billing.count_documents({})
        self.ids.analytics_label.text = (f"Total Patients: {total_patients}\n"
                                         f"Total Appointments: {total_appointments}\n"
                                         f"Total Billing Records: {total_billing}")

# Main app class

class HealthcareApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name="menu"))
        sm.add_widget(AddPatientScreen(name="add_patient"))
        sm.add_widget(ViewPatientsScreen(name="view_patients"))
        sm.add_widget(AddAppointmentScreen(name="add_appointment"))
        sm.add_widget(ViewAppointmentsScreen(name="view_appointments"))
        sm.add_widget(AddBillingScreen(name="add_billing"))
        sm.add_widget(ViewBillingScreen(name="view_billing"))
        sm.add_widget(AnalyticsScreen(name="analytics"))
        return sm

if __name__ == "__main__":
    HealthcareApp().run()
