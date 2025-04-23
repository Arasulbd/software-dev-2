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

print("\n------Example-13: String method ------")

username = " peterpan123  "
print(f"the username ={username}. End of username")
username=username.strip
print(f"the username after method strip ={username}. End of username")

print("\n------Example-14: String method ------")

username = username.lower()
print(f"The username after method lower = {username}. End of username")
username = username.upper()
print(f"The username after method upper = {username}. End of username")

print("\n------Example-15: replace method ------")

username = username.replace('p', '%')
print(f"the username after method replace ={username}. End of username")


print("\n------Example-16: Split method ------")

msg="introdunction to phython programiming today we are learning string methid"
print(f"messege={msg}")
msg=msg.split()
print(f"messge after method ={msg}")


print("\n------Example-17: find method ------")
index_p = msg.find('p')
print(f"index of letter p is={index_p}")
sec_index_p = msg.find('p',index_p+1)
print(f"Next index letter of P is ={sec_index_p}")

#find a non exixting letter
index_y = msg.find('y')
print(f"the index letter of y is ={index_y}")

print("\n------Example-18:in not in statement  ------")

answer_we = "we " in msg 
print(f"is the word 'we in the msg sting? = {answer_we}")
answer_today = "Today" not in msg
print(f"is the word 'Today ' not  in the msg sting? = {answer_today}")

print("\n------Example-19:list indexing  ------")
colors=["orange", "megenta", "olive"]
numbers=["2", "12", "30"]
fixedlist=[False,20 , "peter"]

emptylist=[]

print(f"cplors list={colors}")


print("\n------Example-20:+ * operator on list------")

new_color=colors[0]+colors[-1]
print(f"the new color is + {new_color}")
# contenicate with 2nd and 3rd color
#new_word=colors[1]+numbers[2] data type error


print("\n------Example-21:remove item from  list------")

colors.pop(-1)
print(f"colors after pops ={colors}")

print("\n------Example-21:Add item to the list------")
# add item to the end of list color
colors.append("pink")
print("colors after append ={colors}")
#add a new list to a list
#colors.append(["blue", ["green"]])
#print(f"colors aftert apprnd {colors}")
#colors.append("red","purple")
#print(f"colors aftert apprnd {colors}")

print("\n------Example-22:Add item to the list------")

print(f"Mixed list ={colors}")
colors.sort()
print(f"colors list shorted ={colors}")

bool_list=[True, False, True]
bool_list.sort()
print(f"bool list shorted= {bool_list}")

print("\n------Example-24:count method------")
count_true=bool_list.count(True)
print(f"thre is {count_true} True values")
count_red=colors.count("red")
print(f"thre is {count_red} red colors")

print("\n------Example-25:Length of list------")
length_colors=len(colors)
print(f"there is /are {length_colors} colors")

print("\n------Example-26:index of a item in the list------")
# index of color olive
index_olive=colors.index("olive")
print(f" the index of color of olive is {index_olive}")

