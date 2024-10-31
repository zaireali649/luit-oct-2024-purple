from datetime import datetime  # Importing the datetime module to work with dates and times

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
