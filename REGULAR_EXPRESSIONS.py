import re

# Shorthand character class
# \d Any numeric digit from 0 to 9.
# \D Any character that is not a numeric digit from 0 to 9.
# \w Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
# \W Any character that is not a letter, numeric digit, or the underscore character.
# \s Any space, tab, or newline character. (Think of this as matching “space” characters.)
# \S Any character that is not a space, tab, or newline.

message = "This phrase contains a phone number 905-755-1234 here is another number 999-123-1111"

# raw strings
# returns first match it finds
phoneNumberRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
myMatchObject = phoneNumberRegEx.search(message)
print(myMatchObject.group())

# findAll method returns a list of strings that it finds
myMatchObject = phoneNumberRegEx.findall(message)
print(myMatchObject)

# if you want to group using parenthesis in regular expressions
phoneNumberRegEx = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
myMatchObject = phoneNumberRegEx.search(message)
print(myMatchObject.group(1))  # grabs first parenthesis section
print(myMatchObject.group(2))

# Using pipe to handle multi prefixes
message = "This phrase contains a batman, batcopter and batwing"
messageTwo = "None Existing string"
myRegularExpression = re.compile(r'bat(man|copter|wing)')
myMatchObject = myRegularExpression.search(message)
print(myMatchObject.group())

# different message
myMatchObject = myRegularExpression.search(messageTwo)
print(myMatchObject == None)

# ? means 0 or 1
message = "batwoman"
myRegularExpression = re.compile(r'bat(wo)?man')
myMatchObject = myRegularExpression.search(message)
print(myMatchObject.group())

# * means more than 0
message = "batwowowowowoman"
myRegularExpression = re.compile(r'bat(wo)*man')
myMatchObject = myRegularExpression.search(message)
print(myMatchObject.group())

# + means 1 or more
message = "batman"
myRegularExpression = re.compile(r'bat(wo)+man')
myMatchObject = myRegularExpression.search(message)
print(myMatchObject == None)

# {x}exactly number of times adding ? makes it non greedy
message = "hellohellohello test"
myRegularExpression = re.compile(r'(hello){3}')
myMatchObject = myRegularExpression.search(message)
print(myMatchObject.group())

message = "hellohello"
myRegularExpression = re.compile(r'(hello){3}')
myMatchObject = myRegularExpression.search(message)
print(myMatchObject == None)

# findAll
message = "hellohellohello test"
myRegularExpression = re.compile(r'e')
myMatchObject = myRegularExpression.findall(message)
print(myMatchObject)

#
lyrics = "12 Drummers Drumming, 11 Pipers Piping, 10 Lords a Leaping, 9 Ladies Dancing, 8 Maids a Milking, 7 Swans a Swimming, 6 Geese a Laying, 5 Golden Rings, 4 Calling Birds, 3 French Hens, 2 Turtle Doves, and a Partridge in a Pear Tree"
myRegularExpression = re.compile(r'\d+ \w+')
myMatchObject = myRegularExpression.findall(lyrics)
print(myMatchObject)

# define your own letters using []
message = "This is my test"
vowelExp = re.compile(r'[aeiouAEIOU]')
myMatchObject = vowelExp.findall(message)
print(myMatchObject)

# ^ not (consonants)
vowelExp = re.compile(r'[^aeiouAEIOU]')
myMatchObject = vowelExp.findall(message)
print(myMatchObject)
