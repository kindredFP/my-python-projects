
print('-----------------------------------------------------')
print('Please enter an integer')

while True:
    userEnteredNumber = input()

    try:
        if int(userEnteredNumber) > 0:
            print('you entered the value greater than 0')
            break;
        else:
            print('you entered a value less than 0')
            break
    except ValueError:
        print('You didnt enter an integer like I asked')
        print("try again")
print("End of while loop")

print('-----------------------------------------------------')
print("Here is another code snippet that prints my integer list and calls the index function")
myList = [1, 2, 3, 4, 5, 6, 7]
print("the value of my list is " + str(myList))

valueOfIndex = myList.index(3)  # this will return to me the index location of 3
print("passing index method call returns " + str(valueOfIndex))
print("now try calling index and passing a value not existing")
try:
    print(myList.index(8))  # note 8 does not exist so this will fail

except ValueError:
    print("Value Error was caught because 8 does not exit")

print("now will try and append the missing value 8 in list")
myList.append(8)  # add the number 8 to the list
print("Current value of my list is " + str(myList))

print("Just appended 8 now the value of calling index is " + str(myList.index(8)))
