# Define Variables
exitPassword = "francis"
password = ""
counter = 0

print("What do you think is the password to exit the loop.")

# LOOPS
while password != exitPassword:
    password = input()
    if password == exitPassword:
        print("You got the right password")
        break;

    print("Nope it is not \""+ password + "\"")
    print("Try Again!")
    counter = counter + 1

print("********************")
print("Your invalid attempts on guessing the password is " + str(counter) + " times")

