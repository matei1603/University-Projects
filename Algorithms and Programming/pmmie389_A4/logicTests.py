import logic
import MyVector
import VectorRepository
import numpy as np

#logic tests
def testIsIntGreaterThanZero():
    assert logic.isIntGreaterThanZero(5) == True

    try:
        logic.isIntGreaterThanZero(0)
    except ValueError:
        assert True

    try:
        logic.isIntGreaterThanZero('x')
    except ValueError:
        assert True

def testIsInt():
    assert logic.isInt(5) == True

    try:
        logic.isInt('x')
    except ValueError:
        assert True

    try:
        logic.isInt(5.2)
    except ValueError:
        assert True

def testIsNumber():
    assert logic.isNumber(16) == True
    assert logic.isNumber(3.0) == True

    try:
        logic.isNumber('x')
    except ValueError:
        assert True


def runAllLogicTests():
    testIsIntGreaterThanZero()
    testIsInt()
    testIsNumber()

#tests2

def testAddScalar():
    v = MyVector(5,'r',1,[5,6,7])
    v.addScalar(2)
    a = np.array([7,8,9])
    comparison = v.getValues() == a
    assert comparison.all() == True
    v.addScalar(0)
    a = np.array([4,4,5])
    comparison = v.getValues() == a
    assert comparison.all() == False

    try:
        v.addScalar('x')
    except ValueError:
        assert True

def testAddVectors():
    v = MyVector(3,'g',3,[2,8,5])
    v1 = MyVector(5,'r',6,[1,2,4])
    v.addVectors(v1)
    a = np.array([8,6,2])
    comparison = v.getValues() == a
    assert comparison.all() == True
    v = MyVector(1,'g',3,[1,2,3])
    v1 = MyVector(1,'r',3,[1,2,3])
    v.addVectors(v1)
    a = np.array([5,6,7])
    comparison = v.getValues() == a
    assert comparison.all() == False

    v = MyVector(1,'r',3,[1,2,3])
    v1 = MyVector(1,'g',5,[1,2,3,4])
    try:
        v.addVectors(v1)
    except ValueError:
        assert True

def testSubtract():
    v = MyVector(1, 'r', 1, [2, 3, 4])
    v1 = MyVector(1, 'g', 1, [1, 2, 3])
    v.subtract(v1)
    a = np.array([2, 2, 2])
    comparison = v.getValues() == a
    assert comparison.all() == True
    v = MyVector(1, 'y', 2, [1, 2, 3])
    v1 = MyVector(1, 'g', 2, [1, 2, 3])
    v.subtract(v1)
    a = np.array([5, 6, 7])
    comparison = v.getValues() == a
    assert comparison.all() == False

    v = MyVector(1, 'g', 2, [2, 3, 4])
    v1 = MyVector(1, 'y', 3, [1, 2, 3, 4])
    try:
        v.subtract(v1)
    except ValueError:
        assert True

def testMultiplication():
    v1 = MyVector(1, 'r', 1, [1, 2, 3])
    v2 = MyVector(2, 'y', 2, [4, 5, 5])
    assert v1.multiplication(v2) == 29
    v1 = MyVector(1, 'r', 1, [])
    v2 = MyVector(2, 'y', 2, [1, 2, 3])
    try:
        v1.multiplication(v2)
    except ValueError:
        assert True

    v1 = MyVector(1, 'r', 1, [1, 2, 3])
    v2 = MyVector(2, 'y', 2, [1, 2, 3, 4])
    try:
        v1.multiplication(v2)
    except ValueError:
        assert True

def testSumElements():
    v1 = MyVector(1,'r',1,[1,2,3])
    assert v1.sumElements() == 6
    v1.setValues([1])
    assert v1.sumElements() == 1

    v1.setValues([])
    try:
        v1.sumElements()
    except ValueError:
        assert True

def testProduct():
    v1 = MyVector(1,'r',1,[1,2,3])
    assert v1.product() == 6
    v1.setValues([1])
    assert v1.product() == 1

    v1.setValues([])
    try:
        v1.product()
    except ValueError:
        assert True

def testAverage():
    v1 = MyVector(1,'r',1,[2,2,2])
    assert v1.average() == 2.0
    v1.setValues([1])
    assert v1.average() == 1.0

    v1.setValues([])
    try:
        v1.average()
    except ValueError:
        assert True

def testMinimum():
    v1 = MyVector(1,'r',1,[1,2,3])
    assert v1.minimum() == 1
    v1.setValues([1])
    assert v1.minimum() == 1

    v1.setValues([])
    try:
        v1.minimum()
    except ValueError:
        assert True

def testMaximum():
    v1 = MyVector(1, 'r', 1, [1, 2, 3])
    assert v1.maximum() == 3
    v1.setValues([1])
    assert v1.maximum() == 1

    v1.setValues([])
    try:
        v1.maximum()
    except ValueError:
        assert True

def testAdd():
    vrepo = VectorRepository()
    v1 = MyVector(1,'r',1,[1,2,3])
    vrepo.add(v1)
    assert vrepo.__repr__() == "[( 1, r, 1, [1 2 3] )]"

    v2 = MyVector(2,'y',2,[1,2,3])
    vrepo.add(v2)
    try:
        assert vrepo.__repr__() == "[( 1, r, 1, [1 2 3] )]"
    except AssertionError:
        assert True

    v3 = MyVector(1,'r',1,[2,3,4])
    try:
        vrepo.add(v3)
    except ValueError:
        assert True

def testGetVectorAtIndex():
    vrepo = VectorRepository()
    vrepo.add(MyVector(1,'r',1,[1,2,3]))
    assert vrepo.getVectorAtIndex(0) == "( 1, r, 1, [1 2 3] )"

    vrepo.add(MyVector(2,'y',3,[1,2,3]))
    try:
        vrepo.getVectorAtIndex('a')
    except ValueError:
        assert True

    try:
        vrepo.getVectorAtIndex(3)
    except ValueError:
        assert True

def testUpdateVectorAtIndex():
    vrepo = VectorRepository()
    vrepo.add(MyVector(1,'r',1,[1,2,3]))
    vrepo.updateVectorAtIndex(0,3,'y',2,[3,4,5])
    assert vrepo.__repr__() == "[( 3, y, 2, [3 4 5] )]"
    vrepo.add(MyVector(1,'r',1,[1,2,3]))

    try:
        vrepo.updateVectorAtIndex('a',5,'r',3,[1,2,3])
    except ValueError:
        assert True

    try:
        vrepo.updateVectorAtIndex(3,1,'r',2,[1,2,3])
    except ValueError:
        assert True

    try:
        vrepo.updateVectorAtIndex(1,3,'r',3,[2,3,4])
    except ValueError:
        assert True

def testUpdateVectorByName_id():
    vrepo = VectorRepository()
    vrepo.add(MyVector(1,'r',1,[1,2,3]))
    vrepo.updateVectorByName_id(1,3,'y',3,[6,7,8])
    assert vrepo.__repr__() == "[( 3, y, 3, [6 7 8] )]"

    vrepo.updateVectorByName_id(1,4,'r',2,[1,2,3])
    assert vrepo.__repr__() == "[( 3, y, 3, [6 7 8] )]"

    vrepo.add(MyVector(1,'g',1,[2,2,4]))
    try:
        vrepo.updateVectorByName_id(3,2,'r',1,[2,3,4])
    except ValueError:
        assert True

def testDeleteVectorByIndex():
    vrepo = VectorRepository()
    vrepo.add(MyVector(1,'r',1,[1,2,3]))
    vrepo.deleteVectorByIndex(0)
    assert vrepo.__repr__() == "[]"

    vrepo.add(MyVector(1,'r',1,[1,2,3]))
    try:
        vrepo.deleteVectorByIndex('a')
    except ValueError:
        assert True

    try:
        vrepo.deleteVectorByIndex(2)
    except ValueError:
        assert True

def testDeleteVectorByName_id():
    vrepo = VectorRepository()
    vrepo.add(MyVector(1,'r',1,[1,2,3]))
    vrepo.deleteVectorByName_id(1)
    assert vrepo.__repr__() == "[]"
    vrepo.add(MyVector(1,'r',1,[1,2,3]))

    vrepo.deleteVectorByName_id(2)
    assert vrepo.__repr__() == "[( 0, 2, 1, [3 2 1] )]"

    vrepo.deleteVectorByName_id('a')
    assert vrepo.__repr__() == "[( 3, g, 7, [2 5 6] )]"

def runAllMainTests():
    testGSVector()
    testAddScalar()
    testAddVectors()
    testSubtract()
    testMultiplication()
    testSumElements()
    testProduct()
    testAverage()
    testMinimum()
    testMaximum()
    testAdd()
    testGetVectorAtIndex()
    testUpdateVectorAtIndex()
    testUpdateVectorByName_id()
    testDeleteVectorByIndex()
    testDeleteVectorByName_id()