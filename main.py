#1 Swaplist first element and last element
def swapList(newone):
    size=len(newone)

    temp=newone[0]
    # 1 3 4 5 6 (5-1=4)
    newone[0]=newone[size-1]
    newone[size-1]=temp
    print("Here is the ouput after swapping")
    print("please check below")
    return newone
newone=[1,3,4,5,6]
print(swapList(newone))                             \\ouput : Here is the ouput after swapping
                                                              please check below
                                                              [6, 3, 4, 5, 1]

#2 largest among three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
largest_number = max(number1, number2, number3)
print("The largest number is:", largest_number)

#3 Spathiphyllum plant sampletest
name=input("enter flower name:")
if name=="Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif name=="spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not",name+"!")

#4 Swapping three elements in a List
def swapPositions(lst, pos1, pos2,pos3):
    lst[pos1], lst[pos2],lst[pos3] = lst[pos3], lst[pos1] , lst[pos2]
    return lst
List = [26,36,75,42,94,253]
pos0, pos3 ,pos4 = 0, 3 ,4
print(swapPositions(List, pos0, pos3, pos4))   \\ouput : [94, 36, 75, 26, 42, 253]

#5 Length of string using diff methods
new_list=[1,2,3,5,6,7,8,5]
#using len
yupp=len(new_list)
#using sum
aprox=sum(1 for i in new_list)
#using counter
counter=0
for i in new_list:
    counter=counter+1
print("the length of the list is", yupp)            \\ouput: the length of the list is 8
print("the length of the list is " + str(aprox))    \\ouput: the length of the list is 8
print("the length of the list is " + str(counter))  \\output:the length of the list is 8

#6 Checking the variable is in list or not
test_list = [1, 6, 3, 5, 3, 4]
check = int(input("Enter the element to check: "))
if check in test_list:
    print("Element Exists")
else:
    print("Not Exists")                             \\output :Enter the element to check: 2
                                                              Not Exists
#7 Matrices
import numpy as np
a=np.matrix([[2,5],[3,2]])
b=np.matrix([[7,6],[4,5]])
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))

#8 Calendar
import calendar
year=int(input("enter year: "))
month=int(input("enter month: "))
print(calendar.month(year,month))

#9 Positie, Negative and Zero
a = float(input("Enter a value: "))
if a > 0:
    print("Number is Positive")
elif a < 0:
    print("Number is Negative")
else:
    print("Number is zero")

#10 Even or odd
hipe=float(input("enter a value : "))
if(hipe%2!=0):
    print("Odd number")
else:
    print("Even number")

#11 Leap Year or Not
Year=int(input("Enter: "))
if(((Year%4==0) and (Year%100!=0)) or (Year%400==0)):
    print("Leap Year")
else:
    print("Not a Leap Year")

#12 Obtain all leap year in between range
begin_year=int(input("Enter begin year: "))
end_year=int(input("Enter end year: "))
for year in range(begin_year,end_year+1):
    if((year%4==0) and (year%100!=0) or (year%400==0)):
        print(year)

#13 prime number or not
num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

#14 obtain prime number between range
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
print(f"Prime numbers in the interval [{start}, {end}]:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num)

#15 factorial of a number
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print(" Factorial does not exists")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

#16 Multiplication table
number = int(input ("Enter the number: "))
count = 1
print ("The Multiplication Table of: ", number)    #while loop for iterating the multiplication 10 times
while count <= 10:
    number = number * 1
    print (number, 'x', count, '=', number * count)
    count += 1

#17 fibonacci series
n = int(input ("Enter the number: "))
a = 0
b = 1
for i in range(0,n):
    print(a, end = " ")
    c = a+b
    a = b
    b = c

# 18 Sum of natural numbers
num = int(input("Enter a positive integer: "))
sum_natural = sum(range(1, num + 1))
print(f"The sum of natural numbers up to {num} is {sum_natural}")

# 19 Check if a number is Armstrong
num = int(input("Enter a number to check if it's an Armstrong number: "))
num_str = str(num)
num_digits = len(num_str)
armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
is_armstrong = armstrong_sum == num
print(f"{num} is {'an' if is_armstrong else 'not an'} Armstrong number")

# 20 Reverse a string
string_input = input("Enter a string: ")
reversed_string = string_input[::-1]
print(f"The reversed string is: {reversed_string}")

# 21 Check if a string is a palindrome
string_input = input("Enter a string to check if it's a palindrome: ")
is_palindrome = string_input == string_input[::-1]
print(f"The string {'is' if is_palindrome else 'is not'} a palindrome")

# 22 Calculate the average of numbers in a list
numbers = [float(x) for x in input("Enter numbers separated by space: ").split()]
average = sum(numbers) / len(numbers)
print(f"The average of the numbers is: {average}")

# 23 Convert temperature from Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")

# 24 Find the largest element in a list
numbers = [float(x) for x in input("Enter numbers separated by space: ").split()]
largest_number = max(numbers)
print(f"The largest number in the list is: {largest_number}")

# 25 Check if a year is a leap year using a function
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Enter a year to check if it's a leap year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 26 Find the common elements between two lists
list1 = [int(x) for x in input("Enter numbers for list 1 separated by space: ").split()]
list2 = [int(x) for x in input("Enter numbers for list 2 separated by space: ").split()]
common_elements = set(list1) & set(list2)
print(f"The common elements between the two lists are: {list(common_elements)}")

# 27 Calculate the area of a triangle
base = float(input("Enter the base length of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area_triangle = 0.5 * base * height
print(f"The area of the triangle is: {area_triangle}")

# 28 Check if a number is a perfect square
import math

num = int(input("Enter a number to check if it's a perfect square: "))
sqrt_num = math.isqrt(num)
is_perfect_square = sqrt_num**2 == num
print(f"{num} is {'a' if is_perfect_square else 'not a'} perfect square")

# 29 Count the occurrences of a specific element in a list
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
element_to_count = int(input("Enter the element to count: "))
occurrences = numbers.count(element_to_count)
print(f"The element {element_to_count} occurs {occurrences} times in the list")

# 30 Reverse a list
original_list = [int(x) for x in input("Enter numbers separated by space: ").split()]
reversed_list = original_list[::-1]
print(f"The reversed list is: {reversed_list}")
