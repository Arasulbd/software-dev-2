"""
NAME=Aminur Rasul
MAy4 Phython class
"""
#1. reveiew of class
class Person:
    def __init__(self, name , age):
       self.username = name
       self.user_age = age*2

    def __str__(self):
        return f"username={self.username}\nUser age={self.user_age} "
    
    #method
    def intro(self):
        return f"hello I am {self.username}"
    
 #print("\n------ Example 1:  ------")
#create object of the classs
user1=Person("Peter", 23)
print(user1.intro())

# Example 2
class Chair:
    # accessable propoerties
    chair_color="brown"
    #inttionlisg the class properties
    def __init__(self, height, width, length):
        self.chairheight = height
        self.__width = width  # private variable
        self.chairlength = length * 2

    def pass_length(self):
        return self.chairlength

    def chair_volume(self):
        return self.chairlength * self.chairheight * self.__width

    def get_color(self):
        return self.chair_color

    def chair_description(self):
        return f"The total volume of the chair is {self.chair_volume()}. The chair color is {self.get_color()}."

    def setprice(self, price):
        self._chairprice = price


# Create an object
userchair1 = Chair(2, 5, 9)

# Output details
print(f"The chair length is = {userchair1.chairlength}")
print(f"The chair width is = {userchair1._Chair__width}")  # Accessing private attribute
print(f"The chair length is = {userchair1.pass_length()}")
print(f"The chair volume is = {userchair1.chair_volume()}")
print(userchair1.chair_description())

# Set and access private price attribute
userchair1.setprice(25)
print(f"The price of the chair is $ {userchair1._chairprice}")