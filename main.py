# fork the repl.it and create a new git hub repo entitled 
#Comparison operators
# Logical operators
# Decision making
# loops(for loops, while loops, range, enumerator)
# min/max practice
# Random in python
# List comprehension


# review practice
# Append the value of current to the end of the list seconds Please use the list.append() method to do that.


seconds = [1.23, 1.45, 1.02]
current = 1.11

# Remove item 1.45 from seconds.
seconds = [1.23, 1.45, 1.02, 1.11]


# Remove items 1.45, 1.02, and 1.11 from seconds.
seconds = [1.23, 1.45, 1.02, 1.11]


################################comparison operators#########################
#remember....
# > greater
# < less
# >= greater or equal
# <= less or equal
# == equal
# != different or not equal to




# Comparison Operators Practice  1:
# Create two variables (num1 and num2) with the following values: 36 and 17. Check if num1 is greater than or equal to num2 and store the result of that comparison in a variable called my_bool



# Comparison Operators Practice  2:
# Create two variables (num1 and num2):
# Inside num1, store the result of the square root of 25
# Inside num2, store the number 5.
# Check if num1 is equal to num2 and store the result of that comparison in a variable called my_bool.


# Comparison Operators Practice #3:
# Create two variables (num1 and num2):

# Inside num1, store the result of 64 x 3

# Inside num2, store the result of 24 x 8

# Check if num1 is different from num2 and store the result of that comparison in a variable called my_bool.







##############################logical operators##################################################


# Logical Operators Practice #1
# Create three variables (num1, num2, and num3):

# Inside num1, store the value 36

# Inside num2, stores the result of the operation 72/2

# Inside num3, store the value 48

# Check if num1 is greater than num2, and less than num3. Store the result of that comparison in a variable called my_bool.




# Logical Operators Practice #2
# Create three variables (num1, num2, and num3):

# Inside num1, store the value 36

# Inside num2, stores the result of the operation 72/2

# Inside num3, store the value 48

# Check if num1 is greater than num2, or less than num3. Store the result of that comparison in a variable called my_bool.



# Logical Operators Practice #3
# Check if the words:

# word1 = "success", and

# word2 = "technology"

# are not found in the sentence below, and store the result (a boolean) in a variable called my_bool:

# "When something is important enough, you do it even if the odds are against you" - Elon Musk





########################################decision making in python#####################################

if 5 == 2:
  print("it is correct")
else:
  print("it is not correct")


  pet = "dog"
  if pet == "cat":
    print("you have a cat")
  elif pet == "dog":
    print("you have a dog")
  else:
    print("I don't know what animal you have")

age = 16
schoolGrade = 9
if age < 18:
  print("you are a minor")
  if schoolGrade >= 7:
    print("passed")
  else:
    print("failed")
else:
  print("you are an adult")

name = "Cristian"
relName = "Diego"
age = 16
if age < 20:
  print("i am young")
elif age < 30:
    print("i am vicenarian")
elif age < 40:
  print("i am tricenarian")
elif age < 50:
  print("i am quadragenarian")
else:
  print("i am old")


# Decision Making Practice #1
# Using the variables num1 and num2, which are fed with user input (just like in the provided code), create a flow control structure that compares the values of the variables, and returns a result according to the case:

# "num1 is greater than num2"

# "num2 is greater than num1"

# "num1 and num2 are equal"

# You must display the value of the user input instead of num1 and num2.
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")

# f"{num1} is greater than {num2}"
# "num2 is greater than num1"
# "num1 and num2 are equal"
# if num1 > num2:
#   print(str(num1) + " is greater than " + str(num2))
# elif num2 > num1:
#   print(str(num2) + " is greater than " + str(num1))
# else:
#   print(str(num1) + " and " + str(num2) + " are equal." )

# Decision Making Practice #2
# The laws of a certain country establish that an adult can drive if they are of legal age (18 years or older), and have a driver's license.

# Create a conditional structure to check if a 16-year-old without a license can drive, and display the corresponding result on the screen:

# "You can drive"

# "You can't drive yet. You must be 18 years old and have a license"

# "You can't drive. You need to have a license"

# Use the code base already provided to set up the appropriate flow control structure and check those conditions.
# age = int(input("Enter your age: "))
# license = input("Do you have your license?: ")
# if age < 18:
#   print("You can't drive yet. You must be 18 years old and have a license")
# elif age >= 18 and license == "No":
#   print("You can't drive. You need to have a license")
# elif age >= 18 and license == "Yes":
#   print("You can drive")

# # "You can drive"

# # "You can't drive yet. You must be 18 years old and have a license"

# # "You can't drive. You need to have a license"

# # Decision Making Practice #3
# # To access a certain job, the candidate must be able to program in Python and speak French.

# # Create a conditional structure to evaluate a candidate given these conditions, and display the corresponding message on the screen:

# # "You meet the requirements to apply"

# # "To apply, you need to know how to program in Python and speak French"

# # "To apply, you need to speak French"

# # "To apply, you need to know how to program in Python"

# # Use the code already provided to set up the appropriate flow control structure and check those conditions. Evaluate a candidate who knows French, but does not know how to program in Python.
# speak_french = False
# knows_python = False

# if speak_french == True and knows_python == True:
#   print("You meet the requirements to apply")
# elif speak_french == False and knows_python == True:
#   print("To apply, you need to speak French")
# elif speak_french == True and knows_python == False:
#   print("To apply, you need to know how to program in Python")
# else:
#   print("To apply, you need to know how to program in Python and speak French")


# # Decision Making Practice #4
# # ask the user for their age
# # if the user's  is between 18 - 21 , print they can vote, other wise print better luck next time.
# age = int(input("Age?: "))
# if age >= 18 and age <= 21:
#   print("you can vote")
# else:
#   print("better luck next time")
  
###################################loops intro######################################
# queue videos
#what is iteration?
#what are for loops?
my_list = ['a', 'b', 'c', 'd']
for letter in my_list:
  letter_number = my_list.index(letter) + 1
  print(f"letter {letter_number}: {letter}")
# For Loops Practice #1
# Using For loops, greet all members of a class, printing "Hello" + their name.

# For example: "Hello Norville"

students = ["Norville", "Fred", "Velma", "Daphne"]
for item in students:
  print("Hello, " + item)


# For Loops Practice #2
# Given the following list of numbers, calculate the sum of all the numbers using For loops and store the result of the sum in a variable called sum_numbers:

list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
# sum_numbers = 





# For Loops Practice #3
# Given the following list of numbers, perform the sum of all even and odd* numbers separately in the variables sum_even and sum_odd respectively:

list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

# *Recall from previous days: the modulus (or remainder) of a number divided by 2 is zero when said value is even, and 1 when it is odd

# num % 2 == 0 (even values)

# num % 2 == 1 (odd values)

list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

# sum_even = 

# sum_odd = 




########################################loops############################################################
# while Loops
# The while statement in Python is one of most general ways to perform iteration. A while statement will repeatedly execute a single statement or group of statements as long as the condition is true. The reason it is called a 'loop' is because the code statements are looped through over and over again until the condition is no longer met.

# The general format of a while loop is:

# while condition:
#     code statements
# else:
#     final code statements

# so a while loop is basically a way for python to loop through code several times until a condtion is met
# Let’s look at a few simple while loops in action.
#queue video about loops
# i = 1
# while i < 10:
#   print(i)
#   i = i + 1
#   # or i += 1

# print("done with loop")


# we can use a while loop to continually ask the user to guess a word until they guess it correctly
# secret_word ="giraffe"
# guess= ""

# while guess != secret_word:
#   guess = input("enter a guess: ")

# print("you win")


# While Loops Practice #1
# Create a While Loop that prints the numbers 10 to 0 on the screen, one at a time.

number = 10



# While Loops Practice #2
# Create a While Loop that subtracts one by one the numbers from 50 to 0 (both numbers included) with the following additional conditions:

# If the number is divisible by 5, show that number on the screen (remember that here you can use the modulus operation dividing by 5 and checking the remainder!)

# If the number is not divisible by 5, continue executing the loop without showing the value on the screen (don't forget to continue subtracting so that the program doesn't run infinitely).

number = 50



# Loop Interruption Statements Practice
# Create a For loop through the following list of numbers, printing each of its elements to the screen, and interrupt the flow when you find a negative value:

# list_numbers = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

# You must not change the order of the list.

list_numbers = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]




##############################dictionaries and loops##############################################
#We've been learning about sequences in Python but now we're going to switch gears and learn about mappings in Python. If you're familiar with other languages you can think of these Dictionaries as hash tables.

# This section will serve as a brief introduction to dictionaries and consist of:

# 1.) Constructing a Dictionary
# 2.) Accessing objects from a dictionary
# 3.) Nesting Dictionaries
# 4.) Basic Dictionary Methods

# So what are mappings? Mappings are a collection of objects that are stored by a key, unlike a sequence that stored objects by their relative position. This is an important distinction, since mappings won't retain order since they have objects defined by a key.

# A Python dictionary consists of a key and then an associated value. That value can be almost any Python object.


#sample dictionary
monthConversions = {
    "JAN" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun": "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct"  : "October"

}
# print(monthConversions["Sep"])
# #add more months
# monthConversions['Nov'] ="November"
# monthConversions['Dec'] = "December"
# print(monthConversions)
#print(monthConversions.keys())
# so structure of a dictionary
 #is the title of the dictionary = {"key": "value"}

# challenge 1
#how do we get data from our dictionary?
# test for understanding
#create a dictionary filled with your favorite actors and movies.
#call the dictionary favActors_Movies
# call the dictionary twice finding at least two movies









##############################ranges#####################################################

# Range Practice #1
# Create a list consisting of all the numbers from 2500 to 2585 (inclusive). Store this list in the variable my_list.



# Range Practice #2
# Using the range() function, create in a single line of code a list consisting of all numbers that are multiples of 3 from 3 to 300 (inclusive). Store this list in the variable my_list.



# Range Practice #3
# Use the range() function and a loop to add the squares of all the numbers from 1 to 15 (inclusive). Store the result in a variable called sum_squares.



# For this purpose:

# Create a range of values that you can iterate through in a loop

# For each of these values, find its squared value (power of 2). You may need to create intermediate variables (optionally).

# Sum all the squared values obtained. Accumulate the sum in the variable sum_squares.



##############################enumerators in python #####################################################


# Enumerator Practice #1
# Print sentences like the following on the screen:

# '{name} is found at index {index}'

# Where name must be each of the names in the list below, and the index, must be obtained via enumerate().

# list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]

# You can use the given print() line as an example and change its variable names, but the returned phrases must be the same!

# Tip: use loops!

# list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]

# print(f'{nombre} se encuentra en el índice {indice}')



# Enumerator Practice #2
# Create a list formed by the tuples (index, element), obtained through enumerating the indices of each character of the "Python" string.

# Call the returned list with the variable name indices_list.

# "Python"


# Enumerator Practice #3
# Print to the screen only the indices of those names in the list below, that start with M:

# list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]

# You can solve it in different ways, but it will help you keeping mind some (if not all) the following elements:

# loops

# if conditionals

# the enumerate() method

# string methods and indexing

# list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]








######################################### zip in python############################################



# Zip Practice #1
# Print to the screen phrases like the following example:

# "The capital of Germany is Berlin"

# Use the zip function, loops, and the following lists of countries and capitals to solve it quickly and efficiently.

# capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
# countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]



# Zip Practice #2
# Create a zip object made up of lists, of a set of brands and products that you prefer, inside the my_zip variable.
# brands =
# products =


# Zip Practice #3
# Create a zip object with the translations of the numbers from 1 to 5 in Spanish, Portuguese and English (in that same order), and then convert the generated object into a list called numbers:

# one / um / one

# two / two / two

# three / three / three

# four / four / four

# five / five / five

# The result should follow the structure:

# [('one', 'um', 'one'), ('two', 'dois', 'two'), ... ]

# 1: uno / um / one
# 2: dos / dois / two
# 3: tres / três / three
# 4: cuatro / quatro / four
# 5: cinco / cinco / five




#################################################min/max######################################

# Min & Max Practice #1
# Get the maximum value among the values in the following list, and store it in a variable named maximum_value:

# number_list = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]




# Min & Max Practice #2
# Calculate the difference between the maximum and minimum value in the following list of numbers, and store it in a variable called number_range:

# number_list = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]


# Min & Max Practice #3
# Using max(), min(), and dictionary methods, get the minimum value from the following dictionary:

# dictionary_ages = {"Tony":55, "Paulie":42, "Meadow":78, "Vito":44, "Ralph":24, "Sarah":35, "Evan":19, "Jean":2 ,"Ned":49}

# Store this value in a variable called minimum_age.

# Also, get the name that comes last in alphabetical order, and store it in a variable called last_name.




################################################random in python#################################################
# Random Practice #1
# Implement the randint() function from the random library that allows you to obtain an integer from 1 to 10, and store that value in a variable called random_number.


# Random Practice #2
# Implement the random() function from the random library to obtain a real number between 0 and 1, and store that value in a variable called random_number.


# Random Practice #3
# Use the random library's choice() method to get a random item from the list of names below, and store the chosen name in a variable called raffle.

# names = ["Samantha", "Carrie", "Chris", "Charlotte", "Richard"]




################################################List comprehension###############################################
# List Comprehensions Practice #1
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# Create a square_values list consisting of the numbers in the values list, squared.

# values = [1, 2, 3, 4, 5, 6, 9.5]




# List Comprehensions Practice #2
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# Create an even_values list consisting of the numbers in the values list that (you guessed it!) are even.

# values = [1, 2, 3, 4, 5, 6, 9.5]




# List Comprehensions Practice #3
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# For the following list of temperatures in degrees Fahrenheit, express these same values in a new list of temperature values in degrees Celsius. The conversion between type of units is as follows:

# °C = (°F - 32) * (5/9)

# or expressed in another way:

# (degrees_fahrenheit-32)*(5/9)

# The list of temperatures is as follows:

# temperature_fahrenheit = [32, 212, 275]

# Store this new list in a variable called degrees_celsius
  
# Decision Making Practice #1
# Using the variables num1 and num2, which are fed with user input (just like in the provided code), create a flow control structure that compares the values of the variables, and returns a result according to the case:

# "num1 is greater than num2"

# "num2 is greater than num1"

# "num1 and num2 are equal"

# You must display the value of the user input instead of num1 and num2.
# num1 = input("Enter a number:")
# num2 = input("Enter another number:")

# f"{num1} is greater than {num2}"
# "num2 is greater than num1"
# "num1 and num2 are equal"


# Decision Making Practice #2
# The laws of a certain country establish that an adult can drive if they are of legal age (18 years or older), and have a driver's license.

# Create a conditional structure to check if a 16-year-old without a license can drive, and display the corresponding result on the screen:

# "You can drive"

# "You can't drive yet. You must be 18 years old and have a license"

# "You can't drive. You need to have a license"

# Use the code base already provided to set up the appropriate flow control structure and check those conditions.
age = 16
has_license = False

"You can drive"

"You can't drive yet. You must be 18 years old and have a license"

"You can't drive. You need to have a license"

# Decision Making Practice #3
# To access a certain job, the candidate must be able to program in Python and speak French.

# Create a conditional structure to evaluate a candidate given these conditions, and display the corresponding message on the screen:

# "You meet the requirements to apply"

# "To apply, you need to know how to program in Python and speak French"

# "To apply, you need to speak French"

# "To apply, you need to know how to program in Python"

# Use the code already provided to set up the appropriate flow control structure and check those conditions. Evaluate a candidate who knows French, but does not know how to program in Python.


speak_french = True
knows_python = False

"You meet the requirements to apply"

"To apply, you need to know how to program in Python and speak French"

"To apply, you need to speak French"

"To apply, you need to know how to program in Python"


# Decision Making Practice #4
# Enter your name

# Enter your relatives name
# Enter your age

# If age is less than 20 print i am young

# If age is less than 30 then print iam vicenarian

# If age is less than 40 then print i am a tricenarian

# If age is less than 50 then print I am quadragenarian


# Decision Making Practice #1
# ask the user for their age
# if the user's  is between 18 - 21 , print they can vote, other wise print better luck next time.

###################################loops intro######################################
# queue videos
#what is iteration?
#what are for loops?


# For Loops Practice #1
# Using For loops, greet all members of a class, printing "Hello" + their name.

# For example: "Hello Norville"

students = ["Norville", "Fred", "Velma", "Daphne"]




# For Loops Practice #2
# Given the following list of numbers, calculate the sum of all the numbers using For loops and store the result of the sum in a variable called sum_numbers:

list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
# sum_numbers = 





# For Loops Practice #3
# Given the following list of numbers, perform the sum of all even and odd* numbers separately in the variables sum_even and sum_odd respectively:

list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

# *Recall from previous days: the modulus (or remainder) of a number divided by 2 is zero when said value is even, and 1 when it is odd

# num % 2 == 0 (even values)

# num % 2 == 1 (odd values)

list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

# sum_even = 

# sum_odd = 




########################################loops############################################################
# while Loops
# The while statement in Python is one of most general ways to perform iteration. A while statement will repeatedly execute a single statement or group of statements as long as the condition is true. The reason it is called a 'loop' is because the code statements are looped through over and over again until the condition is no longer met.

# The general format of a while loop is:

# while condition:
#     code statements
# else:
#     final code statements

# so a while loop is basically a way for python to loop through code several times until a condtion is met
# Let’s look at a few simple while loops in action.
#queue video about loops
# i = 1
# while i < 10:
#   print(i)
#   i = i + 1
#   # or i += 1

# print("done with loop")


# we can use a while loop to continually ask the user to guess a word until they guess it correctly
# secret_word ="giraffe"
# guess= ""

# while guess != secret_word:
#   guess = input("enter a guess: ")

# print("you win")


# While Loops Practice #1
# Create a While Loop that prints the numbers 10 to 0 on the screen, one at a time.

number = 10



# While Loops Practice #2
# Create a While Loop that subtracts one by one the numbers from 50 to 0 (both numbers included) with the following additional conditions:

# If the number is divisible by 5, show that number on the screen (remember that here you can use the modulus operation dividing by 5 and checking the remainder!)

# If the number is not divisible by 5, continue executing the loop without showing the value on the screen (don't forget to continue subtracting so that the program doesn't run infinitely).

number = 50



# Loop Interruption Statements Practice
# Create a For loop through the following list of numbers, printing each of its elements to the screen, and interrupt the flow when you find a negative value:

# list_numbers = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

# You must not change the order of the list.

list_numbers = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]




##############################dictionaries and loops##############################################
#We've been learning about sequences in Python but now we're going to switch gears and learn about mappings in Python. If you're familiar with other languages you can think of these Dictionaries as hash tables.

# This section will serve as a brief introduction to dictionaries and consist of:

# 1.) Constructing a Dictionary
# 2.) Accessing objects from a dictionary
# 3.) Nesting Dictionaries
# 4.) Basic Dictionary Methods

# So what are mappings? Mappings are a collection of objects that are stored by a key, unlike a sequence that stored objects by their relative position. This is an important distinction, since mappings won't retain order since they have objects defined by a key.

# A Python dictionary consists of a key and then an associated value. That value can be almost any Python object.


#sample dictionary
monthConversions = {
    "JAN" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun": "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct"  : "October"

}
# print(monthConversions["Sep"])
# #add more months
# monthConversions['Nov'] ="November"
# monthConversions['Dec'] = "December"
# print(monthConversions)
#print(monthConversions.keys())
# so structure of a dictionary
 #is the title of the dictionary = {"key": "value"}

# challenge 1
#how do we get data from our dictionary?
# test for understanding
#create a dictionary filled with your favorite actors and movies.
#call the dictionary favActors_Movies
# call the dictionary twice finding at least two movies









##############################ranges#####################################################

# Range Practice #1
# Create a list consisting of all the numbers from 2500 to 2585 (inclusive). Store this list in the variable my_list.



# Range Practice #2
# Using the range() function, create in a single line of code a list consisting of all numbers that are multiples of 3 from 3 to 300 (inclusive). Store this list in the variable my_list.



# Range Practice #3
# Use the range() function and a loop to add the squares of all the numbers from 1 to 15 (inclusive). Store the result in a variable called sum_squares.



# For this purpose:

# Create a range of values that you can iterate through in a loop

# For each of these values, find its squared value (power of 2). You may need to create intermediate variables (optionally).

# Sum all the squared values obtained. Accumulate the sum in the variable sum_squares.



##############################enumerators in python #####################################################


# Enumerator Practice #1
# Print sentences like the following on the screen:

# '{name} is found at index {index}'

# Where name must be each of the names in the list below, and the index, must be obtained via enumerate().

# list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]

# You can use the given print() line as an example and change its variable names, but the returned phrases must be the same!

# Tip: use loops!

# list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]

# print(f'{nombre} se encuentra en el índice {indice}')



# Enumerator Practice #2
# Create a list formed by the tuples (index, element), obtained through enumerating the indices of each character of the "Python" string.

# Call the returned list with the variable name indices_list.

# "Python"


# Enumerator Practice #3
# Print to the screen only the indices of those names in the list below, that start with M:

# list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]

# You can solve it in different ways, but it will help you keeping mind some (if not all) the following elements:

# loops

# if conditionals

# the enumerate() method

# string methods and indexing

# list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]








######################################### zip in python############################################



# Zip Practice #1
# Print to the screen phrases like the following example:

# "The capital of Germany is Berlin"

# Use the zip function, loops, and the following lists of countries and capitals to solve it quickly and efficiently.

# capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
# countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]



# Zip Practice #2
# Create a zip object made up of lists, of a set of brands and products that you prefer, inside the my_zip variable.
# brands =
# products =


# Zip Practice #3
# Create a zip object with the translations of the numbers from 1 to 5 in Spanish, Portuguese and English (in that same order), and then convert the generated object into a list called numbers:

# one / um / one

# two / two / two

# three / three / three

# four / four / four

# five / five / five

# The result should follow the structure:

# [('one', 'um', 'one'), ('two', 'dois', 'two'), ... ]

# 1: uno / um / one
# 2: dos / dois / two
# 3: tres / três / three
# 4: cuatro / quatro / four
# 5: cinco / cinco / five




#################################################min/max######################################

# Min & Max Practice #1
# Get the maximum value among the values in the following list, and store it in a variable named maximum_value:

# number_list = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]




# Min & Max Practice #2
# Calculate the difference between the maximum and minimum value in the following list of numbers, and store it in a variable called number_range:

# number_list = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]


# Min & Max Practice #3
# Using max(), min(), and dictionary methods, get the minimum value from the following dictionary:

# dictionary_ages = {"Tony":55, "Paulie":42, "Meadow":78, "Vito":44, "Ralph":24, "Sarah":35, "Evan":19, "Jean":2 ,"Ned":49}

# Store this value in a variable called minimum_age.

# Also, get the name that comes last in alphabetical order, and store it in a variable called last_name.




################################################random in python#################################################
# Random Practice #1
# Implement the randint() function from the random library that allows you to obtain an integer from 1 to 10, and store that value in a variable called random_number.


# Random Practice #2
# Implement the random() function from the random library to obtain a real number between 0 and 1, and store that value in a variable called random_number.


# Random Practice #3
# Use the random library's choice() method to get a random item from the list of names below, and store the chosen name in a variable called raffle.

# names = ["Samantha", "Carrie", "Chris", "Charlotte", "Richard"]




################################################List comprehension###############################################
# List Comprehensions Practice #1
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# Create a square_values list consisting of the numbers in the values list, squared.

# values = [1, 2, 3, 4, 5, 6, 9.5]




# List Comprehensions Practice #2
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# Create an even_values list consisting of the numbers in the values list that (you guessed it!) are even.

# values = [1, 2, 3, 4, 5, 6, 9.5]




# List Comprehensions Practice #3
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# For the following list of temperatures in degrees Fahrenheit, express these same values in a new list of temperature values in degrees Celsius. The conversion between type of units is as follows:

# °C = (°F - 32) * (5/9)

# or expressed in another way:

# (degrees_fahrenheit-32)*(5/9)

# The list of temperatures is as follows:

# temperature_fahrenheit = [32, 212, 275]

# Store this new list in a variable called degrees_celsius



