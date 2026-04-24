"""
Desafio do Dia (Laboratório de 5 min)
No seu repositório, crie um arquivo chamado day_2_structures.py e tente resolver este problema:

Você tem uma lista com nomes duplicados: usuarios = ["Gabriel", "Manu", "Gabriel", "Rogerio"].

Converta para um set para limpar os nomes.

Adicione um novo nome.

Imprima o resultado final.

Conseguiu visualizar a diferença de "verborragia" em relação ao Java? Se quiser, já pode subir esse código para o seu repo! Amanhã o papo é sobre Comprehensions (o equivalente turbinado das Streams do Java).
"""

# Starting list with duplicates
usuarios = ["Gabriel", "Manu", "Gabriel", "Rogerio"]

# 1. Convert to set to remove duplicates (The Pythonic way to clean duplicates)
usuarios_unicos = set(usuarios)

# 2. Add a new name (Sets use .add() instead of .append())
usuarios_unicos.add("Iris")

# 3. Print the final result
print("Final unique users:", usuarios_unicos)
