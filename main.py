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

#4 Swapping three elements in a List
def swapPositions(lst, pos1, pos2,pos3):
    lst[pos1], lst[pos2],lst[pos3] = lst[pos3], lst[pos1] , lst[pos2]
    return lst
List = [26,36,75,42,94,253]
pos0, pos3 ,pos4 = 0, 3 ,4
print(swapPositions(List, pos0, pos3, pos4))   \\ouput : [94, 36, 75, 26, 42, 253]

#length of string using diff methods
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
