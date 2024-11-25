import json

with open('scripts/Lab005/contacts.json') as file:
    contacts = json.load(file)

print(contacts)    