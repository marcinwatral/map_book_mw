def read_friends(users: list)->None:
    print("informacje o Twoich znajomych: ")
    for user in users:
        print(f'\tTwoj znajomy {user["name"]} {user["surname"]} opublikowal {user["posts"]} postow.')

def add_user(lista: list) -> None:
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    liczba_postow = int(input("Podaj liczbę postów uzytkownika: "))
    new_user = {"name": imie, "surname": nazwisko, "posts": liczba_postow, }
    lista.append(new_user)