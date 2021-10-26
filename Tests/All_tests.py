from Tests.Test_Domain import testObiect
from Tests.testsCRUD import test_add_object, test_delete_object, test_modify_object


def runAll():
    testObiect()
    test_add_object()
    test_delete_object()
    test_modify_object()