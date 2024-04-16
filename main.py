users: list=[

    {"name": "Julia","surname":"Gotowiec","posts":1500,},
    {"name": "Hub","surname":"Sybilski","posts":123456,},
    {"name": "Adrian","surname":"Dobrzan","posts":2137,}

]
print("informacje o Twoich znajomych: ")
for user in users:
    print(f'\tTwoj znajomy {user["name"]} {user["surname"]} opublikowal {user["posts"]}.')