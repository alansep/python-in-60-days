# Day 3: Mastering Comprehensions

Today's focus was on understanding how to transform and filter data in a more "Pythonic" way, which is the equivalent of Streams and Filters in the Java world.

## 🧠 Key Learnings

### 1. List Comprehension
Used to create new lists based on existing iterables. It's more concise than a traditional `for` loop.
- **Syntax:** `[expression for item in iterable if condition]`
- **Java Equivalent:** `list.stream().filter(x -> ...).map(x -> ...).collect(Collectors.toList())`

### 2. Dictionary Comprehension
Allows for the quick creation of dictionaries.
- **Syntax:** `{key_expression: value_expression for item in iterable if condition}`
- **Usage:** Perfect for mapping IDs to objects or transforming lists into lookup maps.

### 3. Conditional Logic in Comprehensions
We explored how to use `if/else` inside the expression part (ternary operator):
- **Syntax:** `[value_if_true if condition else value_if_false for item in iterable]`

## 🛠 Exercises Completed
- **exe-1.py:** Filtered and transformed a list of languages.
- **exe-2.py:** Converted a list of tuples into a user lookup dictionary.
- **iris-challenge.py:** A personalized challenge covering nested logic and dictionary mapping.
- **challenge.py:** Original challenge using squares and parity mapping.
