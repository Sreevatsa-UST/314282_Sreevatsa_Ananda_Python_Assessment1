# Part 1 — Python fundamentals
# 1. First largest number
# Given [12, 5, 8, 20, 15], find the first largest number 

numbers = [12, 5, 8, 20, 15]

print("1. First largest number")

largestNumber = numbers[0]
for num in numbers:
    if num > largestNumber:
        largestNumber = num
        print("The first largest number is:", largestNumber)
        
print("********************************************************")

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 2. Character frequency 
# Given the string 'programming', count the frequency of every character using a dictionary.

string = 'programming'
charater = {}

for char in string:
    if char in charater:
        charater[char] += 1
    else:
        charater[char] = 1

print("2. Character frequency")
print("Character frequency:", charater)
print("********************************************************")

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 3. Student marks analysis · 
# Store three students and their marks in a dictionary. Print each student's result as Pass (marks >= 40) or Fail.

students = { 'Jack': 78, 'Sam': 25, 'Hian': 62 }

print("3. Student marks analysis")

for student, marks in students.items():
    if marks >= 40:
        print(f"{student} has passed with {marks} marks")
    else:
        print(f"{student} has failed with {marks} marks")

print("********************************************************")

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
