"""
Students full name
April 24, conditional statement
"""
print("\n------Example 1 and 2: If statement ------")

age=20
agecode=123
if age>=21:
    print("You are audult")
    agecode=200
else:
    print('You are under 21')
    agecode=100

print(f"After the if statment , agecode= {agecode}")

print("\n------Example 3: Multi statement ------")
age=200
if 0<=age<21:
    print('you are minior!')
elif 21<= age <65:
    print('you are audult!')
elif 65<= age <130:
    print('you are senior citizen!')
else:
    print("Unable to read the age")

    print("\n------Example 4: and operator ------")

    temperature=80
    humidity=100
    if 70<=temperature<=90 and humidity<80:
        print('the weather is pleasent')
    else:
        print('the weather is not idale')

    print("\n------Example 5: OR operator ------")
    day="Monday"
    is_holyday=True
    if day=="Saturday" or day=="Sunday" or is_holyday:
        print("you can relax a day")
    else:
        print("it is a work day")

print("\n------Example 6: Nested statement ------")
number=int(input("Enter a number"))
if (number>=0):
    if number==0:
        print("the number is zero")
    print(f"{number} is positive")
else:
    print(f"{number} is negative")

print("\n------Example 7: Nested statement ------")


#username validation
username=input("Enter a username:")
len_username=len(username)
username=username.strip()
if len_username>=3:
    index_whitespace=username.find(" ")
    if index_whitespace == -1:
        print(f"{username} is valid")
    else:
        print(f"{username} is not valid")
else:
    print(f"{username} is invalid. username must have 3 character ")

    print("\n------Example 8: match case statement ------")
respnse_code=401
match respnse_code:
    case 400:
        print(f"Code={respnse_code} server cannot understand")
    case 401|403:
        print(f"{respnse_code}. Refused to send back")
    case 404:
        print(f"{respnse_code} response code not found")
    case _:
        print(f"INVALID CODE")

print("\n------Exercise ------")

grade_1=float(input ("Enter the grade1:"))
grade_2=float(input("Enter the grade 2:"))
#calculate the average
average=(grade_1+grade_2)/2
if 90<= average <=100:
       print(f"your average GPA is {average}, Your grade is A") 
elif 70<= average <=89.99:
       print(f"your average GPA is {average}, Your grade is B") 
elif 60<= average<=69.99:
        print(f"your average GPA is {average}, Your grade is C") 
elif 50<= average<=59.99:
       print(f"your average GPA is {average}, Your grade is D")  
else:
        GPA="Undefined "

