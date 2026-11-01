# 2026 Fall 95896
# Student: Hank Lin
# Andrew ID: hanklin

'''Question 1: Write for loops to do each of the following.
a. Print the integers from 50 to 100, inclusive
b. Print the integers from 100 to 50, inclusive, on one line (recall that print can use this form:
print(thing ,end=' ' ) to print all the entries on one line).
c. Print the even integers from 50 to 100, inclusive, on one line
d. Print the integers that are divisible by 7 *or* divisible by 8, from 50 to 100 inclusive
e. Print the sum of the integers from 50 to 100, inclusive
'''

# a.
for q1a in range(50, 101):
    print(q1a)

#b 
for q1b in range(100,49,-1):
    print(q1b, end = ' ')

#c
print([q1c for q1c in range(50,101,2)])

#d
for q1d in range(50,101):
    if q1d % 7 == 0 or q1d % 8 == 0:
        print(q1d, end=" ")



#e
sumE = 0
for q1e in range(50, 101):
    sumE += q1e
print(sumE)

#%%
'''
Question 2: Prompt the user to enter the temperature in degrees Fahrenheit and whether it is raining (yes or no).
Based on the respective condition, display one of the following messages:
• “Stay inside” if the temperature is below 32 and it is raining
• “Bring a coat” if the temperature is below 50
• “Wear a sweater” if the temperature is below 60
• “Nice weather” otherwise

'''

temp_2 = int(input("Enter temperature: "))
rain_2 = input("Is it raining? (yes or no): ").lower() == "yes"


if temp_2 < 32 and rain_2:
    print("Stay inside")

elif temp_2 < 50:
    print("Bring a coat")

elif temp_2 < 60:
    print("Wear a sweater")
    
else:
    print("Nice weather")



#%%
'''
Question 3: Create a variable called num and set it equal to 1. Write code that displays the corresponding day
given the number using a match/case statement. Use the following mapping: 1 to Monday, 2 to Tuesday, ..., 7 to
Sunday. If the integer is not between 1 and 7, display "Error". Test your code with several values to make sure
that the match/ case statement works correctly
'''

num = 1


match num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Error")
    


#%%
'''
Question 4: Prompt the user to enter a string containing letters, digits, and other characters. Write code that
displays only the digits in the string, in the order they appear.
'''

myString = input("Enter String: ")
ans4 = []

for ch in myString:
    if ch.isdigit():
        ans4.append(ch)


print("".join(ans4))



'''
Question 5: Prompt the user to enter a positive integer. Use a while loop to display the digits of the integer in
reverse order. Do not convert the integer to a string.
'''


int5 = int(input("Enter a Positive Interger: "))

while int5 > 0:
    dig5 = int5 % 10
    print(dig5, end="")
    
    int5 = int5 // 10




#%%
'''
Question 6: This problem explores some of the math library not discussed in lecture.
a. In the interpreter, run the command 'import math'. Then type dir(math) to see a list of the math
library's functions.
b. Prompt the user for an angle in degrees. Use math.radians( ) to convert it to radians; store it in a
variable called 'theta' and display it. Note the required library prefix before the function name.
c. Compute the sum of the squares of the sine and cosine of theta and display the answer (it should be 1).
Then write an if statement that displays 'Equal' if it really is equal to 1, otherwise display 'Not equal'.
Were they equal? How could they possible be unequal?
d. For each trig identity below, assign the left-hand side to a variable called left and the right-hand side
to a variable called right. Display left, right, and the result of left == right. Use print(
‘%.16f’ % (left) ) and something similar for right, so that you can see 16 decimal places. 
'''

#a 
import math

# print(dir(math))

#b
angle = float(input("Provide an angle in degrees: "))

theta = math.radians(angle)

print(angle, theta)

#c

q6c = math.sin(theta) ** 2 + math.cos(theta) ** 2

print(repr(q6c))

if q6c == 1:
    print('Equal')
else:
    print('Not equal')
    
'''    
#c test for other angles:

for angle in [10, 20, 30, 45, 60, 70, 80]:
    theta = math.radians(angle)
    result = math.sin(theta) ** 2 + math.cos(theta) ** 2
    print(angle, repr(result), result == 1)
    

angle, sum of sin**2 & cos**2, equal to 1
10 0.9999999999999999 False
20 1.0 True
30 1.0 True
45 1.0000000000000002 False
60 1.0 True
70 0.9999999999999999 False
80 0.9999999999999999 False
'''

#d
# (i)

left = math.tan(theta)
right = math.sin(theta) / math.cos(theta)

print('%.16f' % left)
print('%.16f' % right)
print(left == right)

diff = abs(left - right)
print('%.16f' % diff)



if diff <= 0.001:
    print("Tolerance 0.001: Equal")
else:
    print("Tolerance 0.001: Not equal")

if diff <= 0.00001:
    print("Tolerance 0.00001: Equal")
else:
    print("Tolerance 0.00001: Not equal")

if diff <= 0.000000001:
    print("Tolerance 0.000000001: Equal")
else:
    print("Tolerance 0.000000001: Not equal")



# (ii)

left = math.cos(theta)
right = math.sin(math.pi/2 - theta)

print('%.16f' % left)
print('%.16f' % right)
print(left == right)

diff = abs(left - right)
print('%.16f' % diff)



if diff <= 0.001:
    print("Tolerance 0.001: Equal")
else:
    print("Tolerance 0.001: Not equal")

if diff <= 0.00001:
    print("Tolerance 0.00001: Equal")
else:
    print("Tolerance 0.00001: Not equal")

if diff <= 0.000000001:
    print("Tolerance 0.000000001: Equal")
else:
    print("Tolerance 0.000000001: Not equal")



# (iii)

left = math.cos(theta * 2)
right = math.cos(theta) ** 2 - math.sin(theta) ** 2

print('%.16f' % left)
print('%.16f' % right)
print(left == right)

diff = abs(left - right)
print('%.16f' % diff)



if diff <= 0.001:
    print("Tolerance 0.001: Equal")
else:
    print("Tolerance 0.001: Not equal")

if diff <= 0.00001:
    print("Tolerance 0.00001: Equal")
else:
    print("Tolerance 0.00001: Not equal")

if diff <= 0.000000001:
    print("Tolerance 0.000000001: Equal")
else:
    print("Tolerance 0.000000001: Not equal")



# (iv)

left = math.sin(theta/ 2)

right_root = math.sqrt((1 - math.cos(theta)) / 2)

if left >= 0:
    right = right_root
else:
    right = - right_root

print('%.16f' % left)
print('%.16f' % right)
print( left == right)

diff = abs(left - right)
print('%.16f' % diff)



if diff <= 0.001:
    print("Tolerance 0.001: Equal")
else:
    print("Tolerance 0.001: Not equal")

if diff <= 0.00001:
    print("Tolerance 0.00001: Equal")
else:
    print("Tolerance 0.00001: Not equal")

if diff <= 0.000000001:
    print("Tolerance 0.000000001: Equal")
else:
    print("Tolerance 0.000000001: Not equal")




    
    