"""
Student's full name: Aminur Rasul
April 25, Loop
"""
from lab11_function import *  # Import all functions from file : lab22_function
import math

print("\n------ Example 1: Python Dictionary ------")
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car)

# to accesss the item in disctionery we use []
print(f"The year of the car is = {car['year']}")
# update value of the car
car["year"] = 1980

print(f"The year of the car updated to {car['year']}")
print(f"The year of the car updated to = {car['year']}")
# add car value pair
car["color"] = "red"
print(car)

print("\nLoop through each key in the dictionary:")
for k in car:
    print(k)

print("\nLoop through each value in the dictionary:")
for k in car:
    print(car[k])

print("\nLoop through each key and value in the dictionary:")
for k in car:
    print(f"{k} has value {car[k]}")

print("\n------ Example 2: Dictionary Application ------")
#given the number of following list , creat a disctionery that will count the number of time that a words appear in the string
#creat a disctionary to orgnize the words as the key and the number of occurency of the word in the value of the key
phrase = "to be or not to be"
print(f"Original phrase = {phrase}")

phrase_split = phrase.split()
print(f"Split phrase = {phrase_split}")

# creat the disctionary

word_count_dict = {}
for word in phrase_split:
    # loop toeach word in the list
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1
        # print the result

print("Resulting dictionary:")
for w in word_count_dict:
    print(f"'{w}' = {word_count_dict[w]}")

print("\n------ Example 3: Function that does not return a value ------")
greeting()

print("\n------ Example 4: Function ------")
printusername("peterpan")

print("\n------ Example 5: Function with default parameters ------")
user_country("martha", "chile")
user_country("Anna")
user_country("", "country")

print("\n------ Example 6: Function that returns a value ------")
num1 = 2
num2 = -6
prod1 = product(num1, num2)
print(f"The product of {num1} and {num2} is = {prod1}")

print("\n------ Example 7: Boolean value ------")
checknum1 = multiple3(num1)
checknum2 = multiple3(num2)
print(f"Is {num1} multiple of 3? {checknum1}")
print(f"Is {num2} multiple of 3? {checknum2}")

print("\n------ Example 8: Composition function ------")
# number = collectnum()
# print(number)

sumall = sumnumbers(3)
print(f"The sum of numbers from 0 to 3 = {sumall}")

print("\n------ Example 9: Built-in math function ------")
r = 2
a = areacircle(r)
areaprint(a, r)

print("\n------ Example 10: Try except------")
r1=ratio_hour(0)
r1=ratio_hour(3)
r1=ratio_hour("peter")

print("\n------ Example 11: Class------")
# create instant of the class
user1=Myclass()
print(f"an intence of the class={user1}")
# class the class property
user1id=user1.id
print(F"user 1 id ={user1id} ")
# call the class method
user1msg=user1.msg
print(f"user 1 messege={user1msg}")

print("\n------ Example 12: Instantiation Class------")
# creat an instant number 
paircomplexnumber=complexnumber(2,3) 
# call the instance object r of the class
real=paircomplexnumber.r
print(f"The real part is {real}")

print("\n------ Example 13: Instan of the  Class------")

# instant of the class
car1=Car("Tesla","S",2023)
# call property, odometer_reading
car_reading = car1.odometer_reading
print(f"car miles reading={car_reading} ")
#car call description
print(car1.get_car_description())
# call odometer
print(car1.read_odometer())
# update to odometer to milage to 10
car1.update_odometer(10)
print(car1.read_odometer())
car1.update_odometer(5)
print(car1.read_odometer())

# update to odometer to milage to 20
car1.increment_odometer(20)
print(car1.read_odometer())
car1.increment_odometer (-5)
print(car1.read_odometer())
car1.increment_odometer(8)
print(car1.read_odometer())