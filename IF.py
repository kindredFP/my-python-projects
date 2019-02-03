# Define Variables

print("Enter your first name.")
firstName = input()
print("Your first name is " + firstName)
print()

print("Now please enter your last name.")
lastName = input()
print("Your last name is " + lastName)
print()

print("Now please enter your userId.")
userId = input()
userId = userId.strip()
print("Your userId  is " + userId)

print("Please enter the same userId")
enteredUserId = input()
enteredUserId = enteredUserId.strip()

# IF STATEMENT
if userId == enteredUserId:
    print("You entered the same userId")
else:
    print("The userId did not match the original one you entered")


