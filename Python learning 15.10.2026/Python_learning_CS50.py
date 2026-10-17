"""
print("Hello world")
print("It's my first step in learning Python")
print("Now I'm making some changes in the code from Gitlab page")

# Comments in Python are written with the # symbol.
# Pseudocode is a way to plan your code before writing it in a programming language.

# you can you 3x" " to write multi-line comments in Python, but remember that this is
# not a standard way to write comments in Python, and it is not recommended to use it
# for multi-line comments.

###### Strings % Variables ######

# Input() function is used to take input from the user.
print("What is your name?")
input()
print("Hello Tomek")

# Return values from input() function can be stored in a variable.
name = input("What is your name?")
print("Hello " + name) 

# input function always returns a string.
# string is a data type that represents text; "str" in Python.

name = input("What is your name?")
print("Hello" ,name , sep="...")

# parameters in functions are values that you can pass to a function to customize its behavior.
# giving values in print function in a way first value is printed, then second, and so on.
# named parameters in functions are values that you can pass to a function by specifying the name of the parameter and its value.
# named parameters in print function are sep, end, file, flush.

print(f"Hello, {name}!") #newer feature in Python 3.6 and above, f-strings allow you to embed expressions inside string literals, using curly braces {}.

# end for today - 51:00 - https://www.youtube.com/watch?v=nLRL_NcnK-4&t=413s

#strings data type has a lot functionalities build-in


# but spaces doesnt look nice, so we can use:
name = input("What is your name?")
name = name.strip() #strip() method removes any leading and trailing whitespace from the string.
print(f"Hello, {name}!")

# lets make a capital letter at the front:
name = input("What is your name?")
name = name.strip()
name = name.capitalize() #capitalize() method returns a copy of the string with its first character capitalized and the rest lowercased.
print(f"Hello, {name}!")

# What about surname?
name = input("What is your name?")
name = name.strip()
name =name.title() #title() method returns a copy of the string with the first character of each word capitalized and the rest lowercased.
print(f"Hello, {name}!")

# but we can combine it together:
name = input("What is your name?")
name = name.strip().title()
print(f"Hello, {name}!")

#also we can do this this way, so there only 2 lines of code:
name = input("What is your name?").strip().title()
print(f"Hello, {name}!")
"""
#so separate name from surname
name = input("What is your name?").strip().title()
first_name, last_name = name.split(" ") 
#split() method splits a string into a list of substrings based on a specified delimiter (in this case, a space).
print(f"Hello {first_name} {last_name}")


