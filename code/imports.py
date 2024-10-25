from datetime import datetime  # Importing the datetime module to work with dates and times
import math  # Importing math for advanced mathematical functions

# Original variables
var = "These are words."  # Defining a string variable
print(type(var))  # Printing the type of var, which will be <class 'str'>

var2 = "386"  # Another string variable that looks like a number
print(type(var2))  # Printing the type of var2, which is also a string <class 'str'>

var3 = int(var2)  # Converting the string '386' to an integer
print(type(var3))  # Printing the type of var3, which will now be <class 'int'>

var4 = input("Enter a number: ")  # Taking user input, which will always return a string
print(var4)  # Printing the value entered by the user
print(type(var4))  # Printing the type of var4, which will be <class 'str'>

var5 = float(var4)  # Converting the user input (string) to a float
print(var5 + 1)  # Adding 1 to the float value and printing the result

var6 = datetime.now()  # Getting the current date and time
print(var6)  # Printing the current date and time
print(type(var6))  # Printing the type of var6, which will be <class 'datetime.datetime'>

# New cool stuff

# Mixed data types example
var1 = "42"  # String that looks like a number
var2 = 10.5  # Float
var3 = 3  # Integer

# Convert var1 to an integer, add it to var2 and var3, then show type of result
result = int(var1) + var2 + var3
print(f"Result of adding different types: {result}")
print(f"Type of result: {type(result)}")  # Type will be float since var2 is float

# String formatting and concatenation
name = "Python"
greeting = f"Hello, {name}!"  # f-string for formatting
print(greeting)

# String slicing
message = "Data Science is fun!"
print(f"Sliced message: {message[0:4]}")  # Output: Data
print(f"Reversed message: {message[::-1]}")  # Output: !nuf si ecneicS ataD

# Math operations
print(f"Square root of 16: {math.sqrt(16)}")  # Output: 4.0
print(f"2 raised to the power 5: {math.pow(2, 5)}")  # Output: 32.0

# Boolean logic operations
a = True
b = False
print(f"a AND b: {a and b}")  # Output: False
print(f"a OR b: {a or b}")  # Output: True
print(f"NOT a: {not a}")  # Output: False

# Type casting and rounding
float_num = 8.75
print(f"Integer part of {float_num}: {int(float_num)}")  # Output: 8
print(f"Rounded value of {float_num}: {round(float_num)}")  # Output: 9

# Working with lists
my_list = [1, 2, 3.5, "Python", True]  # Mixed data types in a list
print(f"Original list: {my_list}")
print(f"List length: {len(my_list)}")
print(f"Second item in list: {my_list[1]}")  # Indexing
print(f"Last item in list: {my_list[-1]}")  # Negative indexing
