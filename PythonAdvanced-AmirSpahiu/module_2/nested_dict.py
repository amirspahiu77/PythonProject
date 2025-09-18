contact_information = {
    #Alice
    "Alice": {
        "phone_number": "555-1234",
        "email": "alice@gmail.com",
        "address": "1234 st",
        "birthday": "20/11/2000"
    },
    #Bob
    "Bob": {
        "phone_number": "555-1234",
        "email": "bob@gmail.com",
        "address": "1234 st",
        "birthday": "20/11/2000"

    },
    #Eve
    "Eve": {
        "phone_number": "555-1234",
        "email": "eve@gmail.com",
        "address": "1234 st",
        "birthday": "20/11/2000"
    }
}

print(contact_information)

bob_information = contact_information["Bob"]
print(bob_information)