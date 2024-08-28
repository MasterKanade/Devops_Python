course = "python programming"
course2 = "Python Programming"
course3 = "   Python Programming   "

# Print the string in uppercase
print(course.upper())
# Print the string in lowercase
print(course2.lower())
# Print the string in title case where every starting character of the word would be capitalized
print(course.title())
# Remove the beginning and end spaces and print the string
print(course3.strip())
# Remove only the right side spaces or trim the spaces
print(course3.rstrip())
# Remove only the left side spaces or tring the spaces
print(course3.lstrip())
# find the index position of the given string
print(course.find("pro"))
# replace the string by character or by using word
print(course.replace("p", "j"))
# To check whether the given string is present in the original string
print("pro" in course)
# To check whether the given string is not present in the original string
print("swift" not in course)
# if string is not present then it will return the -1 in find method case
# it will return -1 because text is not present in course.
print(course.find("text"))
