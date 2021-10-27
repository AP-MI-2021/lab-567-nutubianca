def creeaza_obiect(id, nume, descriere, pret, locatie):
    '''
    creeaza un obiect din inventar
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :return:
    '''
    return [id, nume, descriere, pret, locatie]


def getID(obiect):
    '''
    preia id-ul unui obiect din inventar
    :param obiect: touple ce retine un obiect
    :return: id-ul obiectului
    '''
    return obiect[0]


def getNume(obiect):
    '''
    preia numele unui obiect din inventar
    :param obiect: touple ce retine un obiect
    :return: numele obiectului
    '''
    return obiect[1]


def getDescriere(obiect):
    '''
    preia descrierea unui obiect din inventar
    :param obiect: touple ce retine un obiect
    :return: descrierea obiectului
    '''
    return obiect[2]


def getPret(obiect):
    '''
    preia pretul achizitiei unui obiect din inventar
    :param obiect: touple ce retine un obiect
    :return: pretule achizitiei obiectului
    '''
    return obiect[3]


def getLocatie(obiect):
    '''
    preia locatia unui obiect din inventar
    :param obiect: touple ce retine un obiect
    :return: locatia obiectului
    '''
    return obiect[4]


def toString(obiect):
    return "ID: {}, Nume: {}, Descriere: {}, Pretul achizitiei: {}, Locatie: {}".format(
        getID(obiect),
        getNume(obiect),
        getDescriere(obiect),
        getPret(obiect),
        getLocatie(obiect)
    )