

from simpleFunctions import euclid, isbn

'''euclid'''

'''
pre/postcondition:
    Specification：function purpose
    Precondition：input requirement
    Postcondition: output requirment

validity:
    Normal
    Boundary-valid
    Boundary-invalid
    Equivalence Partition
'''


def test_euclid_normal():
    assert euclid( 30, 12 ) == 6 
    
def test_euclid_coprime():
    assert euclid(5, 7) == 1 

def test_euclid_boundary_valid():
    assert euclid(1, 97) == 1
    
def test_euclid_boundary_invalid():
    assert euclid(0, 97) is None
    
def test_euclid_invalid_a():
    assert euclid(-21, 7) is None

def test_euclid_invalid_b():
    assert euclid(21, -7) is None

def test_euclid_invalid_both():
    assert euclid(-21, -7) is None

test_euclid_normal()
test_euclid_coprime()
test_euclid_boundary_valid()
test_euclid_boundary_invalid()
test_euclid_invalid_a()
test_euclid_invalid_b()
test_euclid_invalid_both()



'''ISBN'''


'''
pre/postcondition:
    Specification：function purpose
    Precondition：input requirement
    Postcondition: output requirment
'''



def test_isbn_normal_valid(): #valid checksum
    assert isbn([0, 3, 0, 6, 4, 0, 6, 1, 5, 2]) is True

def test_isbn_normal_invalid(): #invalid checksum
    assert isbn([0, 3, 0, 6, 4, 0, 6, 1, 5, 3]) is False


def test_isbn_boundary_9(): #9 digits
    assert isbn([0, 3, 0, 6, 4, 0, 6, 1, 5]) is False

def test_isbn_boundary_10(): #10 digits
    assert isbn([0, 3, 0, 6, 4, 0, 6, 1, 5, 2]) is True

def test_isbn_boundary_11(): #11 digits
    assert isbn([0, 3, 0, 6, 4, 0, 6, 1, 5, 2, 9]) is False

test_isbn_normal_valid()
test_isbn_normal_invalid()
test_isbn_boundary_9()
test_isbn_boundary_10()
test_isbn_boundary_11()