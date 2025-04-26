"""
Students full name: Aminur Rasul
April 25, loop
"""
print("\n------Example 1 For loop as a counter ------")
#print hello from 0 to 4
for x in range(0,5):
    print(f"hello{x}")

print("\n------Example 2 For loop in a list ------")
fruits=["Apple", "orange", "graphe", "kiwis", "Phineapples"]
for eachfruitindex in range(0,5):
    print(f"fruit in index {eachfruitindex} = {fruits[eachfruitindex]})")
#Alternative way of to loop thrugh list

print("\n------Alternative way to loop thrugh list ------")
for eachfruit in fruits:
   print(eachfruit)

print("\n------Example 3: For loop in different increment ------")
#for loop to print from 2 to 30 with an increment of 3
for num in range(2,30,3):
    print(num)

print("\n------Example 4: For loop in different increment ------")
#for loop to print from 10 to 10 with an decrement of 2
for num in range(10,0,-2):
    print(num)

print("\n------Example 5: For loop through string ------")
username="peterpan123"
for eachcharacter in username:
    print(eachcharacter)

print("\n------Example 6: Nested conditional statement ------")
# for loop  to check how many negative number in the list
number=[5,-2, 0, 9,8,-1]
negativecounter=0
for eachnumber in number:
    if eachnumber <0:
        negativecounter +=1 #The same negative number = negativenumber +1
#prompt result
print(f"there are {negativecounter} negative numbers")

print("\n------Example 7: Nested conditional statement: operation ------")
# for loop to add all odd numbers
sumodd=0
for eachnumber in number:
    if eachnumber %2 == 1:
        sumodd+=eachnumber
#prompt result
print(f"The sum of all odd number is ={sumodd}")

print("\n------Example 8: Break statment in a loop ------")
# for loop to print from 0 to 10 (exclusive) and terminate the loop if it reach 5
for n in range (0,10):
    if n==5:
        print("Counter reach to 5")
        break
    else:
        print(n)

print("\n------Example 9: Continue statment in a loop ------")
# for loop to add number   from 0 to 10 (exclusive) except number 5
sumall=0
for n in range (10):
    sumall+=n
    print(f"\tsum {sumall}")

print("\n------Example 9: Continue statment in a loop ------")
# for loop to add number   from 0 to 10 (exclusive) except number 5
sumall=0
for n in range(10):
    if n==5:
        print("Skipping 5")
        continue
    sumall+= n
    print(n)
    print(f"\tsum {sumall}")

print("\n------Example 10: else  statment in a  for loop ------")
for n in range(6):
    if(n==3):
        break
    print(n)
else:
    print("loop completed")

print("\n------Example 11: While loop for counter ------")
# while loop to print from 0-5(inclusive)

n=0
while n<6:
    print(n)
    n+=1
print("\n------Example 12: While loop as check point ------")
# while loop to collect and add between -5 and 5
sumusernumber = 0
while True:
    number = int(input('Enter a number between -5 and 5: '))
    if number < -5 or number > 5:
        break
    sumusernumber += number

print(f"The total sum is = {sumusernumber}")


print("\n------Example 13: While loop as counter operator------")
# while loop to collect the even number in the list
numbers=[20, 0, -5, 1 , 8, -6, 7, -3]
index=0
len_numbers= len(numbers)
evencount=0
while index<len_numbers:
    if numbers[index]%2==0 and not (numbers[index])==0:
        evencount+=1
    index+=1
else:
    print(f"there are {evencount} even numbers")
    
