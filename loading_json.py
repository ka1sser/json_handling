import json

# Converting json file into a Python object
with open("pokemon.json", "r") as f:
    data = json.load(f)  # Loading json file

# Accessing and deleting an element
for pokemon in data["pokemons"]:
    del pokemon["stats"]

# Converting Python object to json file
with open("new_pokemon.json", "w") as f:
    json.dump(data, f, indent=2)  # Dumping to new file
