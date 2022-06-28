def printRange(my_range):
    print("please enter value between 1 to " + str(my_range))


mylist = []


# This function take input for given range and store it in list
def getInputInRange(my_range):
    for i in range(0, my_range):
        new_val = int(input("enter val " + str(i + 1) + ":- "))
        mylist.append(new_val)

    return True


#  This function check is input type is int
def isIntValue(val):
    True  # type(int(val)) == int


while True:
    firstRange = input("enter val :- ")
    firstRange = int(firstRange)
    if firstRange in range(1, 21):
        if getInputInRange(firstRange):
            print("List:- \n")
            print(mylist)
            break
    else:
        printRange(20)
