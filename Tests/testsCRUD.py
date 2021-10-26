from Domain.inventar import getID, getNume, getDescriere, getPret, getLocatie
from Logic.CRUD import add_object, get_by_ID, delete_object, modify_object


def test_add_object():
    lista = []
    lista = add_object("1", "hartie",  "A4", 20, "etaj", lista)
    assert get_by_ID("1",lista) == lista[0]
    assert len(lista) == 1
    assert getID(lista[0]) == "1"
    assert getNume(lista[0]) == "hartie"
    assert getDescriere(lista[0]) == "A4"
    assert getPret(lista[0]) == 20
    assert getLocatie(lista[0]) == "etaj"


def test_delete_object():
    lista = []
    lista = add_object("1", "hartie",  "A4", 20, "etaj", lista)
    lista = add_object("2", "pixuri",  "albastre", 50, "nr1", lista)
    lista = delete_object("1", lista)
    assert len(lista) == 1
    assert get_by_ID("1", lista) is None
    assert get_by_ID("2", lista) is not None

    lista = delete_object("3", lista)
    assert len(lista) == 1
    assert get_by_ID("2", lista) is not None


def test_modify_object():
    lista = []
    lista = add_object("1", "hartie", "A4", 20, "etaj", lista)
    lista = add_object("2", "pixuri", "albastre", 50, "nr1", lista)
    lista = modify_object("1","capsator", "mic", 60, "nr2", lista)
    assert getID(lista[0]) == "1"
    assert getNume(lista[0]) == "capsator"
    assert getDescriere(lista[0]) == "mic"
    assert getPret(lista[0]) == 60
    assert getLocatie(lista[0]) == "nr2"
    