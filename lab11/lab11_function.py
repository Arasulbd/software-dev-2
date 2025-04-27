
"""
Student's full name: Aminur Rasul
April 27, Functions
"""

import math

# Example 3: Function that does not return a value
def greeting():
    print("Welcome to functions!")

# Example 4: Function with parameter
def printusername(username):
    print(f"Welcome to function {username}")

# Example 5: Function with default parameters
def user_country(username="(no name)", country="USA"):
    print(f"{username} is living in country {country}")

# Example 6: Function that returns a value
def product(n1, n2):
    return n1 * n2

# Example 7: Function to check if number is multiple of 3
def multiple3(n):
    if n % 3 == 0 and n != 0:
        return True
    else:
        return False

# Example 8: Composition functions
def collectnum():
    n = float(input("Enter a number between 1 and 9: "))
    while not (1 <= n <= 9):
        n = float(input("Re-enter a number between 1 and 9: "))
    return n

def sumnumbers(totalnumbers):
    total_sum = 0
    for _ in range(totalnumbers):
        total_sum += collectnum()
    return total_sum

def printresult(totalsum):
    print(f"The total sum is {totalsum}")

# Example 9: Area of a circle
def areacircle(radius):
    area = math.pow(radius, 2) * math.pi
    return round(area, 2)

def areaprint(area, radius=0):
    print(f"The area of circle with radius {radius} is {area}")

#function  of return of the ratio of two numbers
def ratio_hour(hour):
    try:
        dayhour = 24
        r = hour / dayhour  # Calculate ratio
    except ZeroDivisionError:
        print("Zero Expectation")
        print("number can't be divided by zero")
        return 0
    except ValueError:
        print("Value Expectation")
        print("number was not provided or invalid")
        return 0
    except Exception:
        print("General Expectation")
        print(f"There was an error in the division")
        return 0
    else:
        print("diviion is fine")

        return r  # If no error occurred, return the ratio
    finally:
        print("Process completed")

# Example 11
# definanig a class name "my class"
class Myclass:
    # property attribute
    id=12345
    #method
    def msg(self):
        return "Welcome to the python class"


# Example 12 
class complexnumber():
     # instantiate of the class
    def __init__(self, realnumber, imgnumber):
        self.r=realnumber
        self.i=imgnumber
   
# Example 13 
class car:
    #instantiate of the class
    def __init__(self, make, model,year):
        self.carmake=make
        self.carmodel=model
        self.caryear= year
    # set property odometer
    odometer_reading=0
    # method to return descriptive of the car
    def get_car_description(self):
        return f"{self.carmake} with model{self.carmodel} was made on {self.caryear}"
    # Method to read odo meter
    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it"
    # update the odometer
    def update_odometer(self,milage):
        if milage> self.odometer_reading:
            self.odometer_reading=milage
        else:
            print('odometer can \'T roll back')

# add to miles to odometer
def increment_odometer(self, miles):
    if miles>0: 
        self.odometer_reading+=miles
    else:
        print("cant find negative miles")