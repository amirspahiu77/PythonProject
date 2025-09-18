contact_info = {
    "Kroni": "555-1234",
    "Rroni": "123456-99"
}

print(contact_info)

kroni_phone = contact_info["Kroni"]
print(kroni_phone)

#update values
contact_info["Rroni"] = "1234-567"
print(contact_info)

#add a new contact
contact_info["Alina"] = "555-5555"
print(contact_info)

#delete an existing contact
del contact_info["Kroni"]
print(contact_info)

#keys() method
keys = contact_info.keys()
print(keys)

#values() method
values = contact_info.values()
print(values)

#items() method
items = contact_info.items()
print(items)
