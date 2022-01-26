# Task 1
# Write a Python function to find the Max of three numbers.

def max_number(list):
    return max(list)


print(max_number([5, 7, 1])) # Enter here the three numbers



# Task 2
# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def sum(list):
    result = 0
    for number in list:
        result += number
    return result


print(sum([11, 99, 637, 443])) # Enter here the numbers you want to sum



# Task 3
# Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

def multiply(list):
    result = 1
    for number in list:
        result *= number
    return result


print(multiply([3, 6, 9, 6]))



# Task 4
# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def reverse():
    text = input("Enter text: ")
    return text [::-1]


print(reverse())



# Task 5
# Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.

def factorial(x):
    result = 1
    while x > 0:
        result *= x
        x -= 1
    return result
    

print(factorial(0))



# Task 6
# Write a Python function to check whether a number falls in a given range.

def func_range(number, num_range1, num_range2):
    if number in range(num_range1, num_range2 + 1):
        return bool(True)
    else:
        return bool(False)


print(func_range(24, 3, 24))



# Task 7
# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.    
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def upper_lower():
    text = input("Enter text: ")
    count_upper = 0
    count_lower = 0
    for i in text:
        if i.isupper():
            count_upper += 1
        elif i.islower():
            count_lower += 1
    print(f"No. of Upper case characters : {count_upper}")
    print(f"No. of Lower case Characters : {count_lower}")


upper_lower()



# Task 8 
# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def list_transform(first_list):
    unique_list = []
    for number in first_list:
        if number not in unique_list:
            unique_list.append(number)
    return unique_list


print(list_transform([1, 2, 3, 3, 3, 4, 5, 6]))



# Task 9
# Write a Python function that takes a number as a parameter and check the number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

def prime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True


print(prime(2))



# Task 10
# Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

def even(list):
    even_numbers = []
    for number in list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


print(even([1, 2, 3, 4, 5, 6, 7, 8, 9]))



# Task 11 
# Write a Python function to check whether a number is perfect or not. 
# Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. 
# Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 
# The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.

def perfect_number(x):
    sum = 0
    for i in range(1, x):
        if x % i == 0:
            sum += i
    return sum == x


print(perfect_number(28))


# Task 12
# Write a Python function that checks whether a passed string is palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

def palindrom():
    text = input("Enter text: ")
    n = text.replace(" ", "")
    if n == n[::-1]:
        print("It is palindrom!")
    else:
        print("It is not a palindrom!")


palindrom()



# Task 13
# Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

def pangram():
    text = input("Enter text: ")
    new_text = text.replace(" ", "")
    new_text = new_text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in new_text:
            return "The text is not pangram!"
        else:
            return "The text is a pangram!"


print(pangram())



# Task 14
# Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).

def squared():
    list = [i for i in range(1, 31)]
    squared_list = []
    for number in list:
        number *= number
        squared_list.append(number)
    return squared_list


print(squared())