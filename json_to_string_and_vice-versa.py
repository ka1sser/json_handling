import json

people_string = """
{
    "people": [
        {
            "name": "Itadori Yuji",
            "anime": "Jujutsu Kaisen",
            "has_won": true
        },
        {
            "name": "Edward Elric",
            "anime": "Fullmetal Alchemist Brotherhood",
            "has_won": true
        }
    ]
}
"""

# Convert string to json
print(f"Type of people_string: {type(people_string)}")
data = json.loads(people_string)  # Loading a string (load-S for string)
print(f"Type of data: {type(data)}")

# Accessing an element and deleting an element
for person in data["people"]:
    del person["has_won"]

# Convert json to string
print(f"Type of data: {type(data)}")
new_data = json.dumps(
    data, indent=2, sort_keys=True
)  # Dumping a string (dump-S for string)
print(f"Type of new_data: {type(new_data)}")
