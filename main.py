#1 Swaplist
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

#4