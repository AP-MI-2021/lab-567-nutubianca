def creeaza_obiect(id, nume, descriere, pret_achizitie, locatie):
    '''
    creeaza un obiect din inventar
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :return:
    '''
    return {
        "id": id,
        "nume": nume,
        "descriere": descriere,
        "pret": pret_achizitie,
        "locatie": locatie
    }


def getID(obiect):
    '''
    preia id-ul unui obiect din inventar
    :param obiect: dictionar ce retine un obiect
    :return: id-ul obiectului
    '''
    return obiect["id"]


def getNume(obiect):
    '''
    preia numele unui obiect din inventar
    :param obiect: dictionar ce retine un obiect
    :return: numele obiectului
    '''
    return obiect["nume"]


def getDescriere(obiect):
    '''
    preia descrierea unui obiect din inventar
    :param obiect: dictionar ce retine un obiect
    :return: descrierea obiectului
    '''
    return obiect["descriere"]


def getPret(obiect):
    '''
    preia pretul achizitiei unui obiect din inventar
    :param obiect: dictionar ce retine un obiect
    :return: pretule achizitiei obiectului
    '''
    return obiect["pret"]


def getLocatie(obiect):
    '''
    preia locatia unui obiect din inventar
    :param obiect: dictionar ce retine un obiect
    :return: locatia obiectului
    '''
    return obiect["locatie"]


def toString(obiect):
    return "ID: {}, Nume: {}, Descriere: {}, Pretul achizitiei: {}, Locatie: {}".format(
        getID(obiect),
        getNume(obiect),
        getDescriere(obiect),
        getPret(obiect),
        getLocatie(obiect)
    )