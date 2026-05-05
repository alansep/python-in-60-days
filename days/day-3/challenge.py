numbers = list(range(1,21))

filtered_numbers = [s * s for s in numbers if s % 3 == 0]

filtered_dict = {s: "Par" if s%2==0 else "Impar" for s in filtered_numbers}

print(filtered_numbers)
print(filtered_dict)