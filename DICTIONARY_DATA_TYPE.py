# define a dictionary list
myDictionary = {'firstName': 'francis', 'lastName': "pala", 'age': 40}

print()
print("The keys of my Dictionary")
print(myDictionary.keys())

print()
print("The values of my Dictionary")
print(myDictionary.values())

print("")
print("The keys and values of my Dictionary")
print(myDictionary.items())
print("Or using for loop")
# List the key and value pairs of dictionary
for k, v in myDictionary.items():
    print('Key: ' + k + ' Value: ' + str(v))

print("")
print("Access specific value passing the key")
print("The Value of passing Key firstName is = " + myDictionary.get('firstName', 'elementDoesntExist'))
print("Pass a key that doesnt exist = " + myDictionary.get('nonExistentKey', 'The key returned doesnt exist'))

# setDefault is a function to use to define an init value if the key doenst exist yet, if a value exist nothing happens
print("My old dictionary value = " + str(myDictionary.items()))
# Add a value if it doesnt exist
myDictionary.setdefault("univ", "U of T")
print("My new dictionary value = " + str(myDictionary.items()))

print("*********")
# Add 2 dictionaryLists
list1 = {'name': 'Francis', 'age': 40}
list2 = {'name': 'Aiden', 'age': 4}

# after defining the two lists append it to another list
list1.update(list2)
print("dictionary values got overwritten by the same keys" + str(list1))
# try adding a list with new keys
list3 = {"other": 1, "gender": "M"}
list1.update(list3)
print("Updated value of list1 which contains list3" + str(list1))
