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

