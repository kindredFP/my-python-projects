# you can put single quotes inside double quoted strings
print("They're going over there")
# you can also escape it
print("They\'re going over there")

# Other escape characters
# \"     double quote
# \t     tabs
# \n     new line
# \\    slash

# upper/lower methods
name = "Francis"
print(name.upper())
print(name.lower())

# 3 double quotes is handy
# """ anything inside here is part of a string """
print("""Anyting inside can have spaces
// slashes and anything
""")

# Using index on a list
mySentence = "here is my sentence"
print(mySentence[0])
print(mySentence[3])
print(mySentence[8])

# handy string methods to determine if string contains alphanumeric etc values.
spam = 'hasnumbers1'
print(spam.isalnum())
print(spam.isnumeric())
print(spam.isalpha())

# handy %s replacement
name = "francis"
age = "40"
address = "attenborough"
print("Hello my name is %s and my age is %s and I live near %s" % (name, age, address))
