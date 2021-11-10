from Domain.inventar import creeaza_obiect, getID, getLocatie, getNume, getDescriere, getPret


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
    if len(locatie) != 4:
        print("Eroare: locatie necorespunzatoare!")
        return lista
    if "0" in id or "-" in id:
        print("Eroare: ID-ul nu poate fi negativ sau egal cu 0!")
        return lista
    try:
        pret_int = int(pret)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista
    if float(pret) <= 0:
        raise ValueError("Pretul trebuie sa fie mai mare ca 0!")
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
    if get_by_ID(id, lista) is None:
        raise ValueError("Nu exista un obiect cu id-ul dat!")
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
    if get_by_ID(id, lista) is None:
        raise ValueError("Nu exista un obiect cu id-ul dat!")
    if len(locatie) != 4:
        print("Eroare: locatie necorespunzatoare!")
        return lista
    lista_noua = []
    for obiect in lista:
        if getID(obiect) == id:
            obiect_nou = creeaza_obiect(id, nume, descriere, pret, locatie)
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua


def moving_objects(locatie_1, locatie_2, lista):
    """
    -muta toate obiectele dintr-o locatie in alta
    :param locatie_1: string cu numele primei locatii
    :param locatie_2: string cu numele locatiei dorite pentru obiecte
    :param lista: lista de obiecte
    :return: lista_noua: lista initiala, dar cu obiectul dorit modificat
    """
    lista_noua = []
    for obiect in lista:
        if getLocatie(obiect) == locatie_1:
            obiect_nou = creeaza_obiect(getID(obiect), getNume(obiect), getDescriere(obiect), getPret(obiect),
                                        locatie_2)
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua


def add_string(pret, string, lista):
    """
    -concateneaza un sir la toate descrierile obiectelor cu
    pretul mai mare decat o valoare data
    :param pret: pretul dat de utilizator(de tip float)
    :param string: string de sirul dorit pentru adaugare
    :param lista: lista de obiecte
    :return: lista_noua: lista initiala, dar cu obiectele dorite modificate
    """
    lista_noua = []
    for obiect in lista:
        if getPret(obiect) > pret:
            descriere_noua = getDescriere(obiect) + " " + string
            obiect_nou = creeaza_obiect(getID(obiect), getNume(obiect), descriere_noua, getPret(obiect),
                                        getLocatie(obiect))
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua


def delete_string(pret, string, lista):
    """
    -sterge un sufix dat de la toate descrierile obiectelor cu
    pretul mai mare decat o valoare data
    :param pret: pretul dat de utilizator(de tip float)
    :param string: string de sirul dorit pentru adaugare
    :param lista: lista de obiecte
    :return: lista_noua: lista initiala, dar cu obiectele dorite modificate
    """
    lista_noua = []
    for obiect in lista:
        if getPret(obiect) > pret and string in getDescriere(obiect):
            descriere_veche = getDescriere(obiect)
            descriere_noua = descriere_veche[:-len(string)]
            obiect_nou = creeaza_obiect(getID(obiect), getNume(obiect), descriere_noua, getPret(obiect),
                                        getLocatie(obiect))
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua


def sorting_objects(lista):
    """
    -ordoneaza obiectele crescator dupa pretul de achizitie
    :param lista: lista de obiecte
    :return: lista data ordonata dupa pretul de achizitie
    """
    return sorted(lista, key=lambda obiect: getPret(obiect))


def maxPretPerLocatie(lista):
    '''
    -determina cel mai mare pret pentru fiecare locatie
    :param lista: lista de obiecte
    :return: un dictionar rezultat
    '''
    rezultat = {}
    for obiect in lista:
        locatie = getLocatie(obiect)
        pret = getPret(obiect)
        if locatie in rezultat:
            if pret > rezultat[locatie]:
                rezultat[locatie] = pret
        else:
            rezultat[locatie] = pret
    return rezultat


def sumaPreturiPerLocatie(lista):
    '''
    -determina suma preturilor pentru fiecare locatie
    :param lista: lista de obiecte
    :return: un dictionar rezultat
    '''
    rezultat = {}
    for obiect in lista:
        locatie = getLocatie(obiect)
        pret = getPret(obiect)
        if locatie in rezultat:
            rezultat[locatie] = rezultat[locatie] + pret
        else:
            rezultat[locatie] = pret
    return rezultat

