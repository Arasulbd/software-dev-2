"""
Student's full name: Aminur Rasul
April 27, exercise for additional point
"""
from lab11_exercise import*
import math
# creating instanche for student
student1=Student("ABCD",19)
student2=Student("XYZ", 24)
student3=Student("MNO", 22)
# adding the grade with each student
student1.add_grade("Math", 90)
student1.add_grade("english", 80)
student1.add_grade("science", 66)

student2.add_grade("Math", 70)
student2.add_grade("english", 76)
student2.add_grade("science", 60)

student3.add_grade("Math", 70)
student3.add_grade("english", 76)
student3.add_grade("science", 60)

# getting average grade for student 1
print(f"{student1.name} average grade : {student1.get_average_grade()}")
print(f"{student2.name} average grade : {student2.get_average_grade()}")
print(f"{student3.name} average grade : {student3.get_average_grade()}")