appointments = []


def book_appointment(patient_name, practitioner_name, appointment_time):
    # Validation improvements
    if not patient_name or not isinstance(patient_name, str) or patient_name.strip() == "":
        raise ValueError("Patient name cannot be empty.")

    if not practitioner_name or not isinstance(practitioner_name, str) or practitioner_name.strip() == "":
        raise ValueError("Practitioner name is invalid.")

    if not appointment_time or not isinstance(appointment_time, str) or appointment_time.strip() == "":
        raise ValueError("Appointment time is invalid.")

    # Preventing same practitioner and time slot conflict
    for appt in appointments:
        if appt['practitioner'].lower() == practitioner_name.strip().lower() and appt[
            'time'].lower() == appointment_time.strip().lower():
            raise ValueError(f"Conflict: Practitioner {practitioner_name} is already booked at {appointment_time}.")

    appointment = {
        "patient": patient_name.strip(),
        "practitioner": practitioner_name.strip(),
        "time": appointment_time.strip()
    }
    appointments.append(appointment)
    print(
        f"\n[Success] Successfully booked appointment for {patient_name.strip()} with {practitioner_name.strip()} at {appointment_time.strip()}.")


def display_appointments():
    if not appointments:
        print("\n--- No appointments recorded yet. ---")
        return
    print("\n--- Current Appointments List ---")
    for index, appointment in enumerate(appointments, start=1):
        print(
            f"{index}. Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")


if __name__ == "__main__":
    print("Welcome to SmartCare: The Clinical Appointment Booking System!\n")

    while True:
        print("\nMenu:")
        print("1. Book a New Appointment")
        print("2. View All Appointments")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == '1':
            p_name = input("Enter patient name: ")
            doc_name = input("Enter practitioner name: ")
            time_slot = input("Enter appointment time (e.g., 2024-07-20 10:00 AM): ")

            try:
                book_appointment(p_name, doc_name, time_slot)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            display_appointments()

        elif choice == '3':
            print("\nThank you for using SmartCare System. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")