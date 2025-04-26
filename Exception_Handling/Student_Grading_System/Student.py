"""
✅ 1. Student Class
Responsibility: Holds data for one student.
Attributes to define:
name: string
roll_number: int
marks: float/int
grade: string (calculated)
Tasks (Methods):
A method to calculate grade based on marks (like A/B/C/Fail)
A method to return/display student info nicely
"""

class Student:
    def __init__(self,name,roll_number,marks):
        self.roll_number=roll_number
        self.name=name
        self.marks=marks
        self.grade=None
        
    def calculate_grade(self):
        if self.marks >= 90:
            self.grade = "A"
        elif self.marks > 70:
            self.grade = "B"
        elif self.marks > 45:
            self.grade = "C"
        else:
            self.grade = "Fail"
        return self.grade

    def __str__(self):
        return f"Name: {self.name}, Roll No: {self.roll_number}, Marks: {self.marks}, Grade: {self.grade}"

    
        
        
        