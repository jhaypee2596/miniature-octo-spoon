# Hello World
print ("Hello World!")

# Example, do not modify!
print(5 / 8)

# Print the sum of 7 and 10
print(7 + 10)

# Division
print(5 / 8)

# Addition
print(7 + 10)

# Addition, subtraction
print(5 + 5)
print(5 - 5)

# Multiplication, division, modulo, and exponentiation
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)

# How much is your $100 worth after 7 years?
print(100 * 1.1 ** 7)

# Create a variable savings
savings = 100

# Print out savings
print(savings)

# Create a variable savings
savings = 100

# Create a variable growth_multiplier
growth_multiplier = 1.1

# Calculate result
result = savings * growth_multiplier ** 7

# Print out result
print(result)

# Create a variable desc
desc = "compound interest"

# Create a variable profitable
profitable = True

savings = 100
growth_multiplier = 1.1
desc = "compound interest"

# Assign product of savings and growth_multiplier to year1
year1 = savings * growth_multiplier

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc

# Print out doubledesc
print(doubledesc)

# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)

# Test List
myListA = [1, 3, 4, 2]
myListB = [[1, 2, 3], [4, 5, 7]]
myListC = [1 + 2, "a" * 5, 3]

print(myListA)
print(myListB)
print(myListC)
print(type(myListC))

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = [areas[3] + areas[-3]]

# Print the variable eat_sleep_area
print(eat_sleep_area)

# Slicing and dicing : my_list[start:end] : The start index will be included, while the end index is not.

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[-4:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[-4:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs = [areas[:6]]

# Alternative slicing to create upstairs
upstairs = [areas[-4:]]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

# Subsetting lists of lists

# Print out house
print(house)
print(house[-1][1])

# List Manipulation

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print areas before maninipulation
print("Before: ")
print(areas)

# Correct the bathroom area
areas[-1] = 10.5

# Change "living room" to "chill zone"
areas[4] = "chill zone"

# Print areas after manipulation
print("AFter: ")
print(areas)

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

# Print areas
print(areas)
print(areas_1)
print(areas_2)

# Delete list elements
areas_test = areas_2[:]
print(areas_test)
#del(areas_test[10]); del(areas_test[11]) # OPTION A
#del(areas_test[10:11]); # OPTION B
del(areas_test[-4:-2]) # OPTION C.
#del(areas_test[-3]); del(areas_test[-4]) # OPTION D

# Print areas
print(areas_test)

# Inner workings of lists

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
#areas_copy = areas
#areas_copy = list(areas) # Explicit Copy of Areas 
areas_copy = areas[:] # Explicit Copy of Areas 

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)