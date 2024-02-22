#Swaplist
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
print(swapList(newone))

#test
n = int(input("enter:"))
if n >= 100:
    print(True)
else:
    print(False)

#if-else branch
if the_weather_is_good:
    go_for_a_walk()
    have_fun()
else:
    go_to_a_theater()
    enjoy_the_movie()
have_lunch()

#nested if-else statements
if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()

#elif statement
if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()

#largest among three numbers 2 diff methods
#1
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

print("The larger number is:", larger_number)

#2
# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number is the largest one. We will verify this soon.
largest_number = number1

if number2 > largest_number:
    largest_number = number2

if number3 > largest_number:
    largest_number = number3

print("The largest number is:", largest_number)

