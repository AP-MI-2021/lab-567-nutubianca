from Domain.inventar import creeaza_obiect, toString
from Logic.CRUD import delete_object, modify_object, add_object, moving_objects, add_string, get_by_ID


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
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati nume: ")
        descriere = input("Dati descriere: ")
        pret = float(input("Dati pretul achizitiei: "))
        locatie = input("Dati locatia(4 caractere): ")
        if len(locatie) != 4:
            print("Eroare: locatie necorespunzatoare!")
            return lista
        return add_object(id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def ui_deleting(lista):
    try:
        id = input("Dati id-ul obiectului de sters: ")
        if get_by_ID(id, lista) is None:
            raise ValueError("Nu exista un obiect cu id-ul dat!")
        return delete_object(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_modify(lista):
    try:
        id = input("Dati id-ul obiectului de modificat: ")
        if get_by_ID(id, lista) is None:
            raise ValueError("Nu exista un obiect cu id-ul dat!")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret = float(input("Dati noul pret de achizitie: "))
        locatie = input("Dati noua locatie: ")
        if len(locatie) != 4:
            print("Eroare: locatie necorespunzatoare!")
            return lista
        return modify_object(id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def show_all(lista):
    for obiect in lista:
        print(toString(obiect))


def ui_moving(lista):
    locatie_1 = input("Dati locatia din care va avea loc mutarea:")
    locatie_2 = input("Dati locatia in care va avea loc mutarea:")
    return moving_objects(locatie_1, locatie_2, lista)


def ui_string(lista):
    try:
        pret = float(input("Dati pretul: "))
        string_adaugare = input("Dati string-ul dorit: ")
        return add_string(pret, string_adaugare, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


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