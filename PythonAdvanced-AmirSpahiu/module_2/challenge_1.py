jane = {
    'name': 'Jane',
    'phone': '333-2211',
    'email': 'jane@email.com'
}

john = {
    'name': 'John',
    'phone': '111-2233',
    'email': 'john@email.com'
}

contacts = {
    'Jane': jane,
    'John': john
}

print("Jane's contact:", contacts['Jane'])

contacts['Jane']['phone'] = '555-000-1111'

print("Jane's updated contact:", contacts['Jane'])