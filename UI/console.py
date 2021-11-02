from Domain.inventar import creeaza_obiect, toString
from Logic.CRUD import delete_object, modify_object, add_object, moving_objects, add_string


def print_menu():
    print("1. Adauga obiect")
    print("2. Sterge obiect")
    print("3. Modifica un obiect")
    print("4. Mutarea tuturor obiectelor dintr-o locatie in alta")
    print("5. Concatenarea unui string citit la toate descrierile "
          "obiectelor cu pretul mai mare decat o valoare citita")
    print("a. Afisare obiecte")
    print("x. Iesire")


def ui_adaugare(lista):
    id = input("Dati id-ul: ")
    nume = input("Dati nume: ")
    descriere = input("Dati descriere: ")
    pret = float(input("Dati pretul achizitiei: "))
    locatie = input("Dati locatia: ")
    return add_object(id, nume, descriere, pret, locatie, lista)

def ui_deleting(lista):
    id = input("Dati id-ul obiectului de sters: ")
    return delete_object(id, lista)


def ui_modify(lista):
    id = input("Dati id-ul obiectului de modificat: ")
    nume = input("Dati noul nume: ")
    descriere = input("Dati noua descriere: ")
    pret = float(input("Dati noul pret de achizitie: "))
    locatie = input("Dati noua locatie: ")
    return modify_object(id, nume, descriere, pret, locatie, lista)


def show_all(lista):
    for obiect in lista:
        print(toString(obiect))


def ui_moving(lista):
    locatie_1 = input("Dati locatia din care va avea loc mutarea:")
    locatie_2 = input("Dati locatia in care va avea loc mutarea:")
    return moving_objects(locatie_1, locatie_2, lista)


def ui_string(lista):
    pret = float(input("Dati pretul: "))
    string_adaugare = input("Dati string-ul dorit: ")
    return add_string(pret, string_adaugare, lista)


def runMenu(lista):
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = ui_adaugare(lista)
        elif optiune == "2":
            lista = ui_deleting(lista)
        elif optiune == "3":
            lista = ui_modify(lista)
        elif optiune == "4":
            lista = ui_moving(lista)
        elif optiune == "5":
            lista = ui_string(lista)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            print("Meniul se va inchide. Multumim!")
            break
        else:
            print("Optiune invalida. Reincercati!")