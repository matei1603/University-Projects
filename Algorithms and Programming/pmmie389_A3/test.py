from repository import PointRepository
from point import MyPoint
import math as m


def testCreateMyPoint():
    try:
        MyPoint("a", 2, "red")
        assert False
    except ValueError:
        assert True

    try:
        MyPoint(1, "b", "blue")
        assert False
    except ValueError:
        assert True

    try:
        MyPoint(1, 2, "purple")
        assert False
    except ValueError:
        assert True


def testgs():
    p = MyPoint(8, 15, "green")
    assert p.getCoord_x() == 8
    assert p.getCoord_y() == 15
    assert p.getColor() == "green"

    p.setCoord_x(13)
    assert p.getCoord_x() == 13
    p.setCoord_y(2)
    assert p.getCoord_y() == 2
    p.setcolor("red")
    assert p.getColor() == "red"


def testAddPoint():

    assert str(PointRepository.getAllPoints()) == "[]"
    PointRepository.addPoint(3, 4, "blue")
    assert str(PointRepository.getAllPoints()) == "[(3,4,blue)]"

    try:
        PointRepository.addPoint("x", 3, "blue")
        assert False
    except ValueError:
        assert True

    try:
        PointRepository.addPoint(0, "a", "green")
        assert False
    except ValueError:
        assert True

    try:
        PointRepository.addPoint(3, 0, "gold")
        assert False
    except ValueError:
        assert True


def testGetPointAtIndex():

    PointRepository.addPoint(2,6,"red")
    PointRepository.addPoint(3,5,"green")
    assert str(PointRepository.getPointAtIndex(0)) == "(2,6,red)"
    assert str(PointRepository.getPointAtIndex(1)) == "(3,5,green)"

    try:
        PointRepository.getPointAtIndex(-4)
    except ValueError:
        assert True

    try:
        PointRepository.getPointAtIndex(6)
    except ValueError:
        assert True


def testGetPointByColor():
    PointRepository.addPoint(5,9,"green")
    PointRepository.addPoint(0,0,"red")
    assert str(PointRepository.getPointByColor("green")) == "[(5,9,green)]"
    assert str(PointRepository.getPointByColor("red")) == "[(0,0,red)]"

    try:
        PointRepository.getPointByColor("gold")
    except ValueError:
        assert True


def testGetPointsInSquare():

    PointRepository.addPoint(2,2,"blue")
    PointRepository.addPoint(3,4,"magenta")
    PointRepository.addPoint(5,6,"green")
    assert str(PointRepository.pointsInSquare(2, 8, 6)) == "[(3,4,magenta), (5,6,green)]"

    try:
        PointRepository.pointsInSquare("x", 0, 0)
        assert False
    except ValueError:
        assert True

    try:
        PointRepository.pointsInSquare(3, "a", 0)
        assert False
    except ValueError:
        assert True

def testMinDistance():

    PointRepository.addPoint(0, 3, "magenta")
    PointRepository.addPoint(3, 4, "green")
    PointRepository.addPoint(0, 4, "red")
    assert PointRepository.minDistance() == m.sqrt(3)

    PointRepository = PointRepository()
    PointRepository.addPoint(0, 0, "magenta")
    assert str(PointRepository.getAllPoints()) == "[(0,0,magenta)]"
    try:
        PointRepository.minDistance()
    except ValueError:
        assert True


def testUpdateAtIndex():

    PointRepository.addPoint(2,5,"green")
    PointRepository.addPoint(0,0,"blue")
    assert str(PointRepository.getPointAtIndex(0)) == "(2,5,green)"
    PointRepository.updateAtIndex(0, 3, 5, "blue")
    assert str(PointRepository.getPointAtIndex(0)) == "(3,5,blue)"

    try:
        PointRepository.updateAtIndex(-17, 3, 4, "blue")
    except ValueError:
        assert True

    try:
        PointRepository.updateAtIndex(3, 2, 5, "magenta")
    except ValueError:
        assert True

    try:
        PointRepository.updateAtIndex(0, "x", 1, "green")
    except ValueError:
        assert True

    try:
        PointRepository.updateAtIndex(0, 5, "a", "green")
    except ValueError:
        assert True

    try:
        PointRepository.updateAtIndex(0, 2, 1, "gold")
    except ValueError:
        assert True

def Shiftx():
    PointRepository.addPoint(3,4,"green")
    try:
        assert PointRepository.getAllPoints() == "[3,4,green]"
    except AssertionError:
        assert True

    try:
        PointRepository.shiftOnX('x')
    except ValueError:
        assert True

def testMaxDistance():

    PointRepository.addPoint(3,6,"red")
    PointRepository.addPoint(2,5,"magenta")

    assert PointRepository.maxDistance() == 2.5

    pr1 = PointRepository()
    try:
        pr1.maxDistance()
    except ValueError:
        assert True

def testDeleteWithinDistance():

    PointRepository.addPoint(5,0,"green")
    PointRepository.addPoint(2,5,"magenta")

    point = MyPoint(2,3,"green")
    PointRepository.deleteWhithinDistance(3,point)
    try:
        assert PointRepository.getAllPoints() == "[(2,5,magenta)]"
    except AssertionError:
        assert True

    try:
        PointRepository.deleteWhithinDistance('x',point)
    except ValueError:
        assert True

def runAllTests():
    testCreateMyPoint()
    testgs()
    testAddPoint()
    testGetPointAtIndex()
    testGetPointByColor()
    testGetPointsInSquare()
    testMinDistance()
    testUpdateAtIndex()
    testShiftx()
    testMaxDistance()
    testDeleteWithinDistance()