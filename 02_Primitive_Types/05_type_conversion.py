# we usually accept values from the user by using input() method
# The input method accepts the user value generally in the string type

user_input = input("Enter the number: \t")
print(type(user_input))  # It will print <class 'str'>

# However, when you want to continue with this number it won't be converted
# it will form the error if we add it with string like
# addition = user_input + 1 will produce error for "1" + 1 as compliers get confused.
# to convert the string into numbers we use either int or float in built methods

addition = int(user_input) + 1
print(f"Addition of two number is: {addition}")

# we've following in-built type conversion functions
# int(x) float(x) bool(x) str(x)

# Python has the truthy and falsy value concept
# where following values are considered as falsy values
# " " - empty string; 0 and None are Falsy values in python

print(bool(0))  # it will print False
print(bool(1))  # it will print True
# it will print False, even though space will also be considered as True
print(bool(""))
print(bool(-1))  # it will print True
print(bool(5))  # it will print True
print(bool(None))  # it will print False
print(bool("False"))  # it will print True
