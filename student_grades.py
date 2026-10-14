
def student_grades_manager():
    students = {
        "Amit": "A",
        "Priya": "B",
        "Rahul": "C"
    }

    while True:
        print("\n===== Student Grades Manager =====")
        print("1. Add a new student")
        print("2. Update an existing student's grade")
        print("3. Display all student grades")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            name = input("Enter student name: ").strip()
            grade = input("Enter student grade (A/B/C/D/F): ").strip().upper()

            if not name:
                print("Student name cannot be empty.")
            elif grade not in ["A", "B", "C", "D", "F"]:
                print("Invalid grade! Please enter A, B, C, D, or F.")
            elif name in students:
                print("Student already exists. Use the update option.")
            else:
                students[name] = grade
                print(f"Student {name} added successfully.")

        elif choice == "2":
            name = input("Enter student name to update: ").strip()

            if name in students:
                grade = input("Enter the new grade (A/B/C/D/F): ").strip().upper()

                if grade in ["A", "B", "C", "D", "F"]:
                    students[name] = grade
                    print(f"Grade updated successfully for {name}.")
                else:
                    print("Invalid grade! Please enter A, B, C, D, or F.")
            else:
                print(f"Student {name} not found.")

        elif choice == "3":
            if students:
                print("\n----- All Student Grades -----")
                for name, grade in students.items():
                    print(f"{name}: {grade}")
            else:
                print("No student records found.")

        elif choice == "4":
            print("Exiting Student Grades Manager. Goodbye!")
            break

        else:
            print("Invalid choice! Please select an option from 1 to 4.")


if __name__ == "__main__":
    student_grades_manager()
