"""
Iris Challenge - Day 3: Mastering Comprehensions

Your task is to demonstrate your mastery of Python comprehensions. 
Follow the instructions below to complete the challenge.
"""

# 1. LIST COMPREHENSION:
# Create a list named 'cube_odds' that contains the CUBE (n**3) 
# of all ODD numbers between 1 and 30.
# TODO: Write your code here

cube_odds = [s * s * s for s in list(range(1,31)) if s % 2 == 1]
print(f"Cube Odds: {cube_odds}")


# 2. DICTIONARY COMPREHENSION:
# Given the list of names below:
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

# Create a dictionary named 'name_length_map' where:
# - Key: The name (string)
# - Value: The length of the name (int)
# Only include names that have MORE than 3 characters.
# TODO: Write your code here
name_length_map = {name: len(name) for name in names if len(name) > 3}
print(f"Name lengh map : {name_length_map}")


# 3. NESTED/CONDITIONAL CHALLENGE:
# Create a list named 'categorized_numbers' for numbers from 1 to 20:
# - If the number is even, the entry should be "Even-<number>"
# - If the number is odd, the entry should be "Odd-<number>"
# TODO: Write your code here

categorized_numbers = [f"Even-{s}" if s % 2 == 0 else f"Odd-{s}" for s in list(range(1,21))]
print(f"Categorized Numbers: {categorized_numbers}")
# When finished, print all your results to verify!
