from Domain.inventar import toString
from Logic.CRUD import add_object, modify_object, delete_object


def show_all(lista):
    for obiect in lista:
        print(toString(obiect))

def printMenu():
    print("add,id,nume,descriere,pret,locatie")
    print("delete,id")
    print("modify,id,nume,descriere,pret,locatie")
    print("show all commands")
    print("show list")
    print("help")
    print("stop")

def Help():
    print("-ajutor-")
    print("Puteti accesa aplicatia prin a da comenzi astfel:")
    print("->comenzile vor fi separate de ';'")
    print("->datele necesare din interiorul comenzilor vor fi separate prin ','")
    print("Programul va rula pana la comanda 'stop'")

def Menu(lista):
    printMenu()
    while True:
        stop = 0
        optiuni = input("Dati optiunile: ")
        lista_optiuni = optiuni.split(";")
        for date in lista_optiuni:
            lista_date = date.split(",")
            if lista_date[0] == "show all commands":
                printMenu()
            elif lista_date[0] == "help":
                Help()
            elif lista_date[0] == "add":
                try:
                    lista = add_object(lista_date[1],lista_date[2],lista_date[3],lista_date[4],lista_date[5],lista)
                except IndexError as ie:
                    print("Eroare: {}".format(ie))
            elif lista_date[0] == "modify":
                try:
                    lista = modify_object(lista_date[1], lista_date[2], lista_date[3], lista_date[4], lista_date[5], lista)
                except IndexError as ie:
                    print("Eroare: {}".format(ie))
            elif lista_date[0] == "delete":
                try:
                    lista = delete_object(lista_date[1], lista)
                except IndexError as ie:
                    print("Eroare: {}".format(ie))
            elif lista_date[0] == "show list":
                show_all(lista)
            elif lista_date[0] == "stop":
                print("Meniul se va inchide. Multumim!")
                stop = 1
                break
            else:
                print("Optiune inexistenta.")
        if stop == 1:
            break