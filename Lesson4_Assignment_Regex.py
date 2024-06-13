# Python Regular Expressions Mastery

# Task 1 : Name Verification

import re # importing regex

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

def valid_names(names):
    for name in names:
        if re.match(r"^[A-Z][a-z]+ |\w [A-Z][a-z]+", name): # checks to see if the beginning of the string starts with upper case or lowercase followed by one or more occurences or words uppercase and lower case followed by one or more occurences are valid
            print(name) # if the names are valid print the name
        else:
            print('Invalid name') # If it is not valid print invalid name

valid_names(names)