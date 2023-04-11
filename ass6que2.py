import json

# Create dictionary of Indian states and their capitals
indian_states = {
    "Andhra Pradesh": "Amaravati",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Gujarat": "Gandhinagar",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Tamil Nadu": "Chennai"
}

# Write dictionary to a JSON file
with open("indian_states.json", "w") as f:
    json.dump(indian_states, f)

