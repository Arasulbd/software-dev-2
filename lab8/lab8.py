"""
Students full name
April 20, Intoduction python
"""
#Single Comment. This line will not work

print("good morining,\nThis my 1st python program code")
print("\example1:String charecter------")
print("\tGood morning ! \nThis is my first python \"Phyton\" code")
print("\n------Example 2: Data Type ------")
print(f"data type of 3.56={type(3.56)}")
print(f"Data type of -120 is {type(-120)}")
print(f"Data type of \'Hello World\' is {type("Hello World")}")
print(f"Data type of symbol \'$\' is {type('$')}")
print(f"Data type of False:={type(False)}")
print(f"Data type of l \'160.5\' is {type('160.5')}")
print(1,000,300)

print("\n------Example 3: Variables ------")

#declare variable

number1 = 25.5
number2 = -12
username="Rasul"
add_numbers= number1+number2
is_raining=True
#promt result
print(f"{username},the sum of {number1} and {number2} is{add_numbers}")

print(f"is rainining today?={is_raining}")

print("\n------Example 4: Assigning varialble ------")

item1,item2,item3="apple",25, False
print(f"item1={item1}, iteam2={item2}, item3={item3}")


# diclare multiplae variable

score1=score2=score3=88

print(f"score1={score1}, score2={score2}, score3={score3}")
number1=number2=number3= 12.5
print(f"variable number 1 is: {number1}")
print(f"variable number 2 is: {number2}")
print(f"variable number 3 is: {number3}")

print("\n------Example5: input command ------")
print("Enter User name")
usernamet=input()
print(f"collected username={username} ")
luckynumber=input("Enter a lucky number:")
print(f"Enter a Lucky Number={luckynumber}")
#double the lucky number
dblucky=int(luckynumber)*2
print(f"Doubled of Lucky={dblucky}")

# cast integer or float to string
triplenumber=str(dblucky)*3
print(f"tripled the casted number ={triplenumber}")

# integer to boll value
completed_task=-20
print(f"completed_task={bool(completed_task)}")

print("\n------Example-6: Arithmetic Operators ------")

num1=25
num2=9
print(f"the sum of {num1} and {num2}is {num1+num2}")
print(f"the difference between  {num1} and {num2}is {num1-num2}")
print(f"the product of   {num1} and {num2}is {num1*num2}")
print(f"the quotient of   {num1} and {num2}is {num1/num2}")
print(f"the modulus remainder of   {num1} and {num2}is {num1%num2}")
print(f"the interger of quotient of {num1} and {num2}is {num1//num2}")
print(f"the result of base {num2} to power of  {num2**3}")


print("\n------Example-7: Finding the hypotesuna ------")

x=float(input("Enter Side 1: "))
y=float(input("Enter Side 2: "))
# calculate the hypotesuna
hyp=(x**2 +y**2)**0.5

print(f"the hypotenuse of {x} and {y} is {hyp:0.1f}")


print("\n------Example-8: Assignment operator ------")
n=20
print(f"number={n}")
n +=3
print(f"number+3={n}")
n-=4

print(f"updated -number={n}")
n*=2
print(f"updated * number={n}")
n/=3
print(f"updated / number={n}")

n//=2
print(f"updated // number={n}")
n**=2
print(f"updated ** ظnumber={n}")
n%=5
print(f"updated % ظnumber={n}")

print("\n------Example-9: Comparison operator ------")

n1=10
n2=3
n3=7

compare1=n1==n2
compare2=n1==(n2+n3)
print(f" is n1 equal n2?     {compare1}")
print(f" is n1 equal n2+n2?     {compare2}")
compare3=n1>n2
compare4=n2<=n3
print(f"is n1 greater then n2     {compare3}")
print(f"is n2 less then  or equal to n3     {compare4}")

print("\n------Example-10: Index ------")

username1="peterabc123"
print(f"the fifth charecheter ={username1[4]}")

print(f"the fifth charecter={username1[5]}")

print("\n------Example-11: string slice ------")

print(f"slice from begeiningof to 4th charecter ={username1[:4]}")
print(f"slice from begeiningof to 7th charecter ={username1[6:]}")
print(f"slice from 3rd to to 8th charecter ={username1[2:8]}")
# sliche from 4the 6 the charecter with negative index
print(f"slice from 3rd to to 8th charecter ={username1[-8:-5]}")

print("\n------Example-12: total charecter len method ------")

print(f"the user name has ={len(username1)} charecters")



      