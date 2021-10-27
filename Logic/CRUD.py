from Domain.inventar import creeaza_obiect, getID


def add_object(id, nume, descriere, pret, locatie, lista):
    """"
    -adauga un obiect in inventar printr-o lista
    :param id: string cu id-ul obiectului
    :param nume: string cu numele obiectului
    :param descriere: string cu descrierea obiectului
    :param pret: int cu pretul achizitiei obiectului
    :param locatie: string cu locatia obiectului
    :param lista: lista de obiecte
    :return: o lista cu obiectele initiale, fiimd adaugat un obiect nou
    """
    obiect = creeaza_obiect(id, nume, descriere, pret, locatie)
    return lista + [obiect]

def get_by_ID(id, lista):
    """
    -va da elementul din lista pentru un id dat
    :param id: id-ul dat de utilizator
    :param lista: lista de obiecte
    :return: obiectul cu id-ul dat sau None, daca nu exista
    """
    for obiect in lista:
        if getID(obiect) == id:
            return obiect
    return None


def delete_object(id, lista):
    """
    -stergerea unui obiect din lista dupa id
    :param id: string cu id-ul obiectului
    :param lista: lista de obiecte
    :return: lista fara obiectul cu id-ul dat de utilizator
    """
    return [obiect for obiect in lista if getID(obiect) != id]


def modify_object(id, nume, descriere, pret, locatie, lista):
    """
    -modifica atributele dorite ale unui obiect dupa id
    :param id: string cu id-ul obiectului
    :param nume: string cu numele obiectului
    :param descriere: string cu descrierea obiectului
    :param pret: int cu pretul achizitiei obiectului
    :param locatie: string cu locatia obiectului
    :param lista: lista de obiecte
    :return: lista_noua: lista initiala, dar cu obiectul dorit modificat
    """
    lista_noua = []
    for obiect in lista:
        if getID(obiect) == id:
            obiect_nou = creeaza_obiect(id, nume, descriere, pret, locatie)
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua