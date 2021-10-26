from Domain.inventar import creeaza_obiect, getID, getNume, getDescriere, getPret, getLocatie


def testObiect():
    obiect = creeaza_obiect("1", "hartie",  "A4", 20, "etaj")
    assert getID(obiect) == "1"
    assert getNume(obiect) == "hartie"
    assert getDescriere(obiect) == "A4"
    assert getPret(obiect) == 20
    assert getLocatie(obiect) == "etaj"