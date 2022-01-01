# Implementation of Regex to verify a users email  

# basic syntax as follows 
# UPPERCASE LETTERS  [A-Z]
# lowercase letters [a-z]
# Numbers [0-9]

import re # imported regex module 
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)" # regex to identify the pattern assigned to a variable 
user_input = input() #  take for user input 
if(re.search(pattern, user_input)): # re.search('pattern to identify', variable to parse)
    print("valid email")
else:
    print("invalid email") 