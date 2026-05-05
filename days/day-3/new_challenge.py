# Day 3 Challenge: List and Dictionary Comprehensions

# 1. Create a list of numbers from 1 to 50
numbers = list(range(1, 51))

# 2. Use list comprehension to create a list of squares of even numbers
even_squares = [n**2 for n in numbers if n % 2 == 0]
print("Squares of even numbers:", even_squares)

# 3. Use dictionary comprehension to create a map where:
# Key is the number, Value is its square
# Only include numbers divisible by 5
divisible_by_5_map = {n: n**2 for n in numbers if n % 5 == 0}
print("Numbers divisible by 5 and their squares:", divisible_by_5_map)
