📚 Student Management System
A simple Student Management System built using Python, demonstrating core programming concepts:
Variables, Functions, Data Types
Object-Oriented Programming (OOP)
Exception Handling
Basic User Interaction with Menu-based System

🏗️ Project Structure
Student.py → Defines the Student class with attributes like name, roll_number, marks, and calculated grade.
StudentManager.py → Manages a list of students, with functionality to add students, validate data, and display all students.
custom_exceptions.py → Defines custom exceptions:
DuplicateRollNumberError
InvalidMarksError
main.py → Runs the interactive menu loop allowing users to:
Add a new student
Display all students
Exit the program

🧠 Concepts Covered
Classes & Objects
Encapsulation
Custom Exception Handling
Validation of Inputs (e.g., roll number uniqueness, marks between 0-100)
Interactive CLI Menus

🚀 How to Run
Clone the repository:
git clone https://github.com/vasukiraj00/Exception-Handling

cd student-management-system
Run the program:
python main.py

📋 Features
✅ Add new students
✅ Validate and prevent duplicate roll numbers
✅ Validate marks (should be between 0 and 100)
✅ Calculate and assign grades based on marks
✅ Display all student details
✅ Clean exit from the program

⚡ Sample Output
=== Student Management System ===
1. Add Student
2. Display All Students
3. Exit

Enter your choice (1/2/3): 1
Enter the name of the student: John
Enter the Roll Number: 101
Enter the Marks: 85
Student John added successfully!

=== Student Management System ===
1. Add Student
2. Display All Students
3. Exit

Enter your choice (1/2/3): 2
Student Name: John
Roll Number: 101
Marks: 85
Grade: B
🙌 Acknowledgments
Built as a mini-project for mastering Python Exception Handling and OOP fundamentals.
A stepping stone towards bigger projects! 🚀

