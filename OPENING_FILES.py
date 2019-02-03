import os

fileName = "sample.txt"
writableFileName = "writable.txt"

# Access file in resourceFiles subfolder
os.chdir(os.getcwd() + "//resourceFiles")
# Open the file
myFileObject = open(fileName)

# single string
contentOfFile = myFileObject.read()
print(contentOfFile)

# Close the file
myFileObject.close()

# after you read the file to use readLines() you need to reopen the file
# Open the file
myFileObject = open(fileName)

# stores it as a list of strings
contentOfFile = myFileObject.readlines()
print(contentOfFile)

# Close the file
myFileObject.close()

# Open a file to be write enabled (w) or append (a)
myFileObject = open(writableFileName, "w")
myFileObject.write("Here is my new content that I'm writing\n")
myFileObject.write("I can add additional content ")
myFileObject.close()

# now try to print the file that you just wrote on
myFileObject = open(writableFileName)
contentOfFile = myFileObject.readlines()
print(contentOfFile)
myFileObject.close()
