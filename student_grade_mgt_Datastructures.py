# Project Question: Student Grade Management System

# Problem Statement

# Write a Python program to manage student records for a class.
# Each student has a name, marks in three fixed subjects, and an average grade.

# Your program should:
# Store student data using lists, tuples, and dictionaries.
# Allow adding new students.
# Display all students with their marks and average.
# Show the topper (highest average) and lowest scorer (lowest average).

# -------------------------------
# Student Grade Management System
# -------------------------------

# Step 1: As Subjects are fixed we use a TUPLE
subjects = ("Math", "Science", "English")

# Step 2: Use a DICTIONARY to store student data
# Each key = student name and value = LIST of marks(which is a list[])
students = {
    "Aisha": [85, 78, 92],
    "Asma": [90, 88, 75],
    "Rahul": [90, 88, 75],
    "Sneha": [76, 80, 89],
    "Manha": [76, 80, 89]
}

# Step 3: Function to calculate average
def calculate_average(marks):
    total_marks=sum(marks)
    No_subjects=len(marks)
    avg=total_marks/No_subjects
    return avg


# Step :4 Add new student record
def add_student():
    name = input("\nEnter new student name: ")
    new_marks = []
    for each in subjects:
        mark = int(input(f"Enter marks for {each}: "))
        new_marks.append(mark)
    students[name] = new_marks
    print(f"Student named {name} added successfully!")

# step 5: Function to assign grade
def assign_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

# Step 6: students report and find topper and lowest scorer
def student_report():
    averages = {}  # Step 1: Create dictionary for averages

    # Calculate averages for all students
    for name, marks in students.items():
        avg = calculate_average(marks)
        averages[name] = avg

    # Initialize topper and lowest (outside loop!)
    topper_name = None
    topper_avg = 0
    lowest_name = None
    lowest_avg = 100

    # Find topper and lowest
    for name, avg in averages.items():
        if avg > topper_avg:
            topper_avg = avg
            topper_name = name
        if avg < lowest_avg:
            lowest_avg = avg
            lowest_name = name

    for name, avg in averages.items():
        grade = assign_grade(avg)
        print(f"{name}\t{avg:.2f}\t{grade}")

    # Print results (once)
    print(f"Topper: {topper_name} → {topper_avg:.2f}")
    print(f"Lowest Scorer: {lowest_name} → {lowest_avg:.2f}")



# Step 7: Main menu
while True:
    print("\n Student Grade Management: ")
    print("1. Display All Students records")
    print("2. Add New Student")
    print("3. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        student_report()
    elif choice == "2":
        add_student()
    elif choice == "3":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
