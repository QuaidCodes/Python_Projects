# JSON manipulation - JSON is commonly used with data APIs'. 

import json

# Sample JSON
sampleJSON = '{"first_name": "John", "last_name": "Doe", "age": 20}'

# Parse to dict
user = json.loads(sampleJSON) # convet the json to a dict

print(user)
print(user["first_name"]) # dict indexing

car = {
    'make': 'Ford',
    'model': 'Mustang',
    'year': 2023
}

carJSON = json.dumps(car) # Converts the dict into json format

print(carJSON)
