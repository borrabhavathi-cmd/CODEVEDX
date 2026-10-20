import csv
import os

def process_students(filename):
    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            students = []

            for row in reader:
                try:
                    name = row["name"].strip()
                    marks = float(row["marks"])

                    if name and 0 <= marks <= 100:
                        students.append({
                            "name": name,
                            "marks": marks
                        })
                    else:
                        print("Invalid data skipped:", row)

                except (ValueError, KeyError):
                    print("Invalid row skipped:", row)

        if not students:
            print("No valid student records found.")
            return

        # Sort students by marks (highest first)
        students.sort(key=lambda student: student["marks"], reverse=True)

        average = sum(s["marks"] for s in students) / len(students)

        print("\n=== STUDENT MARKS REPORT ===")
        for student in students:
            print(f'{student["name"]}: {student["marks"]}')

        print(f"\nAverage Marks: {average:.2f}")

        print("\nStudents scoring 75 or above:")
        for student in students:
            if student["marks"] >= 75:
                print(student["name"], "-", student["marks"])

        # Save processed results
        with open("processed_students.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "marks"])
            writer.writeheader()
            writer.writerows(students)

        print("\nResults saved to processed_students.csv")

    except FileNotFoundError:
        print("Error: CSV file not found.")
    except PermissionError:
        print("Error: Permission denied. Check file access.")
    except (OSError, csv.Error) as error:
        print("File processing error:", error)


if __name__ == "__main__":
    process_students("students.csv")
