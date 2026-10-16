# Part 2 — Functions
# Question 6: Function with return value
# Write a function calculate_bill(price, quantity) that returns the total bill amount. If the bill exceeds ₹2,000, apply a 10% discount.
# Example: calculate_bill(500, 5) should return 2250.0.

def calculateBill(price, quantity):
    
    print("1. Function with return value")
    
    totalBill = price * quantity
    if totalBill > 2000:
        totalBill *= 0.9  # Apply 10% discount
        print(f"A 10% discount has been applied on Price: {price} and Quantity: {quantity}. Total bill after discount is: {totalBill}")
        # return totalBill
    else:
        print(f"No discount applied. on Price: {price} and Quantity: {quantity}. Total bill is: {totalBill}")
    
    return totalBill
    
print(calculateBill(100, 5))
print("********************************************************")

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Question 7: Lambda function
# Given the list:
# numbers = [12, 5, 18, 7, 24, 9, 30]
# Use lambda function to obtain all numbers multiplied by 3.

numbers = [12, 5, 18, 7, 24, 9, 30]
multiple = lambda x: x * 3

multipliedNumbers = [multiple(num) for num in numbers]

print("2. Lambda function")
print("Numbers multiplied by 3:", multipliedNumbers)
print("********************************************************")

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Question 8: Recursion
# Write a recursive function to calculate the factorial of a number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("8. Recursion")    

result = factorial(7)

print(f"Factorial of 7 is : {result}")
print("********************************************************")

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Question 9: String processing
# Write a function that accepts a string and returns the number of vowels, consonants, digits, and spaces.

def characterCount(inputString):
    
    vowelCount = 0
    consonantCount = 0
    digitCount = 0
    spaceCount = 0

    vowels = "aeiouAEIOU"
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"

    for char in inputString:
        if char == " ":
            spaceCount += 1
        elif char in vowels:
            vowelCount += 1
        elif char in letters:
            consonantCount += 1
        elif char in digits:
            digitCount += 1
    return vowelCount, consonantCount, digitCount, spaceCount


print("9. String processing")
inputString = input("Enter a string: ")
vowels, consonants, digits, spaces = characterCount(inputString)

print(f"Vowels Count: {vowels}")
print(f"Consonants Count: {consonants}")
print(f"Digits Count: {digits}")
print(f"Spaces Count: {spaces}")
print("********************************************************")

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
