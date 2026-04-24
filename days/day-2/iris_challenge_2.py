"""
🌟 IRIS CHALLENGE - DAY 2 (RETAKE)
Focus: Refinement, Unpacking, and Pythonic Mapping.

Scenario:
You have a raw access log (list of tuples). You need to clean it, map it, and verify security.

1. Clean duplicates: Remove exact (id, system) duplicates using a Set.
2. Mapping: Create a Dict where key=user_id and value=list of unique systems.
   -> Goal: Avoid 'fake lists'. Use direct list manipulation or even 'defaultdict'.
3. Unpacking: Try to use 'for user_id, system in ...' instead of indexing (tuple[0]).
4. Security Check: Use the immutable tuple SISTEMAS_CRITICOS = ("Financeiro", "RH") 
   to identify which users had dangerous access.

---
RAW DATA:
"""

log_acessos = [
    (101, "Financeiro"),
    (102, "RH"),
    (101, "Financeiro"), 
    (103, "TI"),
    (102, "RH"),         
    (101, "Suporte")     
]

SISTEMAS_CRITICOS = ("Financeiro", "RH")

# YOUR CODE STARTS HERE:

# 1 - removing duplicates
log_acessos_without_duplicates = set(log_acessos)
print(f"1 - Without duplicates = {log_acessos_without_duplicates}")


# 2 - user dictionary
user_dictionary = {}

for key, value in log_acessos_without_duplicates:
   if key in user_dictionary:
      user_dictionary[key].append(value)
   else: 
      user_dictionary[key] = [value]

print(f"\nuser_dictionary = {user_dictionary}")

# 4 - critical systems

for key, value in log_acessos_without_duplicates:
   if value in SISTEMAS_CRITICOS:
      print(f"user {key} has accessed a critical system: {value}")


