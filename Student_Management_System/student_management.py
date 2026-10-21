import json
import os

FILE_NAME = "students.json"


def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError) as error:
        print("Could not read student data:", error)
        return []


def save_students(students):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
        return True
    except OSError as error:
        print("Could not save student data:", error)
        return False


def add_student(students):
    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if any(s["id"] == student_id for s in students):
        print("Student ID already exists.")
        return

    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        marks = float(input("Enter marks (0-100): "))
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Please enter valid numeric marks.")
        return

    students.append({
        "id": student_id,
        "name": name,
        "marks": marks
    })

    if save_students(students):
        print("Student added successfully!")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n{:<12} {:<22} {:>8}".format("ID", "Name", "Marks"))
    print("-" * 44)

    for student in students:
        print("{:<12} {:<22} {:>8.2f}".format(
            student["id"], student["name"], student["marks"]
        ))


def search_student(students):
    student_id = input("Enter student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


def update_student(students):
    student_id = input("Enter student ID to update: ").strip()

    for student in students:
        if student["id"] == student_id:
            name = input("Enter new name (press Enter to keep current): ").strip()

            if name:
                student["name"] = name

            new_marks = input(
                "Enter new marks (press Enter to keep current): "
            ).strip()

            if new_marks:
                try:
                    marks = float(new_marks)
                    if not 0 <= marks <= 100:
                        print("Marks must be between 0 and 100.")
                        return
                    student["marks"] = marks
                except ValueError:
                    print("Invalid marks.")
                    return

            if save_students(students):
                print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student(students):
    student_id = input("Enter student ID to delete: ").strip()

    for student in students:
        if student["id"] == student_id:
            students.remove(student)

            if save_students(students):
                print("Student deleted successfully!")
            return

    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Thank you for using Student Management System!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
