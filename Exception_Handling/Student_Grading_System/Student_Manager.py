from Student import Student

class DuplicateRollNumberError(Exception):pass
class InvalidMarksError(Exception):pass

class StudentManager:
    def __init__(self):
        self.students=[]
        self.roll_numbers= set()#this going to unique
        
    def is_duplicate_roll(self,roll_number):
        return roll_number in self.roll_numbers
    
    def validate_marks(self,marks):
        if marks<0 or marks>100:
            raise InvalidMarksError("Marks must be between 0 and 100")
        
    def add_student(self):
        try:
            name= input("Enter the name of the student: ")
            roll_number= int(input("Enter the Roll Number: "))
            marks = int(input("Enter the Marks: "))
            
            if self.is_duplicate_roll(roll_number):
                raise DuplicateRollNumberError("This roll number already exists.")
            
            self.validate_marks(marks)
            
            new_student = Student(name,roll_number,marks)
            new_student.calculate_grade()
            
            self.students.append(new_student)
            self.roll_numbers.add(roll_number)
            
            print(f"Student {name} added successfully!")  # Confirm addition
        except (DuplicateRollNumberError, InvalidMarksError) as e:
            print(e)  # Print the error message
            
            
    def display_all_students(self):
        if not self.students:
            print("No students available.")
        for student in self.students:
            print(student)
            
            
        
            
            