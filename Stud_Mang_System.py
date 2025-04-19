# Student Management System (Alternative Functional Style)

students = []

def create_student(student_id, name, age, shift):
    return {
        "id": student_id,
        "name": name,
        "age": age,
        "shift": shift
    }

def get_student_index_by_id(student_id):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            return index
    return None

def student_exists(student_id):
    return any(student["id"] == student_id for student in students)

def add_student_flow():
    student_id = input("Enter student ID: ")
    if student_exists(student_id):
        print("Student ID already exists!")
        return
    
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    if not age.isdigit():
        print("Invalid age! Age must be a number.")
        return
    
    shift = input("Enter student shift and Time ")
    new_student = create_student(student_id, name, int(age), shift)
    students.append(new_student)
    print(f"Student {name} added successfully!")

def view_students_flow():
    if not students:
        print("No students found.")
        return

    print("\nStudent List:")
    print("ID\tName\t\tAge\tShift")
    print("-" * 40)
    for student in students:
        print(f"{student['id']}\t{student['name']:<15}\t{student['age']}\t{student['shift']}")

def update_student_flow():
    student_id = input("Enter student ID to update: ")
    index = get_student_index_by_id(student_id)
    
    if index is None:
        print(f"Student with ID {student_id} not found.")
        return

    student = students[index]
    print(f"Updating student: {student['name']}")

    name = input("Enter new name (or press Enter to keep unchanged): ")
    age = input("Enter new age (or press Enter to keep unchanged): ")
    shift = input("Enter new shift (or press Enter to keep unchanged): ")

    if name:
        student["name"] = name
    if age and age.isdigit():
        student["age"] = int(age)
    if shift:
        student["shift"] = shift

    print("Student updated successfully!")

def delete_student_flow():
    student_id = input("Enter student ID to delete: ")
    index = get_student_index_by_id(student_id)
    
    if index is None:
        print(f"Student with ID {student_id} not found.")
        return

    deleted_student = students.pop(index)
    print(f"Student {deleted_student['name']} deleted successfully!")

def main_menu():
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View list of Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student_flow()
        elif choice == "2":
            view_students_flow()
        elif choice == "3":
            update_student_flow()
        elif choice == "4":
            delete_student_flow()
        elif choice == "5":
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
