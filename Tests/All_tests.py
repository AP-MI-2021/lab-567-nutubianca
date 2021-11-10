from Tests.Test_Domain import testObiect
from Tests.testsCRUD import test_add_object, test_delete_object, test_modify_object, test_moving_objects, \
    test_add_string, test_maxPretPerLocatie, test_sorting_objects, test_sumaPreturiPerLocatie, test_undo_redo


def runAll():
    testObiect()
    test_add_object()
    test_delete_object()
    test_modify_object()
    test_moving_objects()
    test_add_string()
    test_maxPretPerLocatie()
    test_sorting_objects()
    test_sumaPreturiPerLocatie()
    test_undo_redo()