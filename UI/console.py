from Domain.inventar import creeaza_obiect, toString, getNume, getDescriere, getPret, getLocatie
from Logic.CRUD import delete_object, modify_object, add_object, moving_objects, add_string, get_by_ID, sorting_objects, \
    maxPretPerLocatie, sumaPreturiPerLocatie, delete_string


def print_menu():
    print("1. Adauga obiect")
    print("2. Sterge obiect")
    print("3. Modifica un obiect")
    print("4. Mutarea tuturor obiectelor dintr-o locatie in alta")
    print("5. Concatenarea unui string citit la toate descrierile "
          "obiectelor cu pretul mai mare decat o valoare citita")
    print("6. Determinarea celui mai mare pret pentru fiecare locatie")
    print("7. Ordonarea obiectelor crescator dupa pretul achizitiei")
    print("8. Afisarea sumelor preturilor pentru fiecare locatie")
    print("9. Undo")
    print("a. Afisare obiecte")
    print("x. Iesire")


def ui_adaugare(lista, undo_operations):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati nume: ")
        descriere = input("Dati descriere: ")
        pret = float(input("Dati pretul achizitiei: "))
        locatie = input("Dati locatia(4 caractere): ")
        rezultat = add_object(id, nume, descriere, pret, locatie, lista)
        undo_operations.append([
            lambda: delete_object(id,rezultat),
            lambda: add_object(id,nume,descriere,pret,locatie,lista)
        ])
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def ui_deleting(lista, undo_operations):
    try:
        id = input("Dati id-ul obiectului de sters: ")
        if get_by_ID(id, lista) is None:
            raise ValueError("Nu exista un obiect cu id-ul dat!")
        rezultat = delete_object(id,lista)
        deleted_object = get_by_ID(id, lista)
        undo_operations.append([
            lambda: add_object(
                id,
                getNume(deleted_object),
                getDescriere(deleted_object),
                getPret(deleted_object),
                getLocatie(deleted_object),
                rezultat),
            lambda: deleted_object(id,lista)
        ])
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_modify(lista, undo_operations):
    try:
        id = input("Dati id-ul obiectului de modificat: ")
        if get_by_ID(id, lista) is None:
            raise ValueError("Nu exista un obiect cu id-ul dat!")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret = float(input("Dati noul pret de achizitie: "))
        locatie = input("Dati noua locatie: ")
        rezultat = modify_object(id, nume, descriere, pret, locatie, lista)
        old_object = get_by_ID(id, lista)
        undo_operations.append([
            lambda: modify_object(
                id,
                getNume(old_object),
                getDescriere(old_object),
                getPret(old_object),
                getLocatie(old_object),
            ),
            lambda: modify_object(id,nume,descriere,pret,locatie,lista)
        ])
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def show_all(lista):
    for obiect in lista:
        print(toString(obiect))


def ui_moving(lista, undo_operations):
    locatie_1 = input("Dati locatia din care va avea loc mutarea:")
    locatie_2 = input("Dati locatia in care va avea loc mutarea:")
    rezultat = moving_objects(locatie_1, locatie_2, lista)
    undo_operations.append([
        lambda: moving_objects(locatie_2, locatie_1, lista),
        lambda: moving_objects(locatie_1, locatie_2, lista)
    ])
    return rezultat


def ui_string(lista, undo_operations):
    try:
        pret = float(input("Dati pretul: "))
        string_adaugare = input("Dati string-ul dorit: ")
        rezultat = add_string(pret, string_adaugare, lista)
        undo_operations.append([
            lambda: delete_string(pret,string_adaugare,lista),
            lambda: add_string(pret, string_adaugare, lista)
        ])

        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_sorting_objects(lista):
    show_all(sorting_objects(lista))


def ui_highest_price(lista):
    rezultat = maxPretPerLocatie(lista)
    for locatie in rezultat:
        print("Locatia {} are pretul maxim de achizitie {}".format(locatie, rezultat[locatie]))


def ui_sums_prices(lista):
    rezultat = sumaPreturiPerLocatie(lista)
    for locatie in rezultat:
        print("Locatia {} are suma preturilor de achizitie {}".format(locatie, rezultat[locatie]))


def runMenu(lista):
    undo_operations = []
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = ui_adaugare(lista, undo_operations)
        elif optiune == "2":
            lista = ui_deleting(lista, undo_operations)
        elif optiune == "3":
            lista = ui_modify(lista, undo_operations)
        elif optiune == "4":
            lista = ui_moving(lista, undo_operations)
        elif optiune == "5":
            lista = ui_string(lista, undo_operations)
        elif optiune == "6":
            ui_highest_price(lista)
        elif optiune == "7":
            ui_sorting_objects(lista)
        elif optiune == "8":
            ui_sums_prices(lista)
        elif optiune == "9":
            if len(undo_operations) > 0:
                operations = undo_operations.pop()
                lista = operations[0]()
            else:
                print("Nu se poate face undo!")
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            print("Meniul se va inchide. Multumim!")
            break
        else:
            print("Optiune invalida. Reincercati!")