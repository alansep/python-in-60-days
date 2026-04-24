duplicated_names_list = ["Gabriel", "Manu", "Gabriel", "Rogerio"]

# names_set = {duplicated_names_list[0], duplicated_names_list[1], duplicated_names_list[2], duplicated_names_list[3]}
# Gemini's tip 
names_set = set(duplicated_names_list)
names_set.add("Tiger")

print(names_set)