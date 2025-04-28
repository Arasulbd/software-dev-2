"""
Student's full name: Aminur Rasul
April 27,  Exercise- extra point
"""
import math
# create clss for student and _init_ method argument for name, age and grades 
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# for empty distionery for grades
        self.grades = {}  
# method to add grade 
    def add_grade(self, subject, grade):
        self.grades[subject] = grade
# method to get return average grade for all the students
    def get_average_grade(self):
        total = sum(self.grades.values())
        average = total / len(self.grades)
        return average
        

