from Domain.inventar import getID, getNume, getDescriere, getPret, getLocatie
from Logic.CRUD import add_object, get_by_ID, delete_object, modify_object, moving_objects, add_string


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
    lista = add_object("2", "pixuri",  "albastre", 50, "nr11", lista)
    lista = delete_object("1", lista)
    assert len(lista) == 1
    assert get_by_ID("1", lista) is None
    assert get_by_ID("2", lista) is not None

    lista = delete_object("2", lista)
    assert len(lista) == 0
    assert get_by_ID("2", lista) is None


def test_modify_object():
    lista = []
    lista = add_object("1", "hartie", "A4", 20, "etaj", lista)
    lista = add_object("2", "pixuri", "albastre", 50, "nr11", lista)
    lista = modify_object("1","capsator", "mic", 60, "nr22", lista)
    assert getID(lista[0]) == "1"
    assert getNume(lista[0]) == "capsator"
    assert getDescriere(lista[0]) == "mic"
    assert getPret(lista[0]) == 60
    assert getLocatie(lista[0]) == "nr22"



def test_moving_objects():
    lista = []
    lista = add_object("1", "hartie", "A4", 20, "nr11", lista)
    lista = add_object("2", "pixuri", "albastre", 50, "nr11", lista)
    lista = add_object("3", "capsator", "mic", 60, "nr22", lista)
    lista = moving_objects("nr11", "nr44", lista)
    assert getLocatie(lista[0]) == "nr44"
    assert getLocatie(lista[1]) == "nr44"
    assert getLocatie(lista[2]) == "nr22"


def test_add_string():
    lista = []
    lista = add_object("1", "hartie", "A4", 20, "nr11", lista)
    lista = add_object("2", "pixuri", "albastre", 50, "nr11", lista)
    lista = add_string(20, "scump", lista)
    assert getDescriere(lista[0]) == "A4"
    assert getDescriere(lista[1]) == "albastre scump"