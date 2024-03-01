import math
from point import MyPoint
'''import matplotlib.pyplot as plt'''


def getAllPoints(self):
  return self.__PointList


def addPoint(self, x, y, color):
    if isNumber(x) and isNumber(y) and (color in ["red", "green", "blue", "yellow", "magenta"]):
        self.__PointList.append(MyPoint(x, y, color))
    else:
        raise ValueError("Coordinates need to be numbers and color should be valid")

def isNumber(value):

    if int(value) == value or float(value) == value:
        return True
    else:
        raise ValueError("Value is not a number")

def getPointAtIndex(pointList,index):
    '''

    :param pointList: The list
    :param index: The index
    :return: The value on the specified index
    '''

    if index >= 0 and index < len(pointList):
        return pointList[index]
    else:
        raise ValueError("Invalid index!")

def getPointsWithColor(pointList,color):
    '''

    :param pointList: The list
    :param color: The specified color
    :return: The points of a specified color
    '''

    colorList = []
    if color in ["red", "green", "blue", "yellow", "magenta"]:
        for elem in pointList:
            if elem.getColor() == color:
                colorList.append(elem)
        return colorList
    else:
        raise ValueError("Invalid color!")

def GetpointsInSquare(pointList, topLeftCorner_x, topLeftCorner_y, length):
    '''

    :param pointList: The list
    :param topLeftCorner_x: coord
    :param topLeftCorner_y: coord
    :param length: The lenght
    :return: Points that are inside the given square
    '''

    squareList = []
    if isNumber(topLeftCorner_x) and isNumber(topLeftCorner_y) and isNumber(length):
        for elem in pointList:
            if int(elem.getCoord_x()) > int(topLeftCorner_x) and int(elem.getCoord_y()) < int(topLeftCorner_y):
                if int(elem.getCoord_x()) < int(topLeftCorner_x) + int(length) and int(elem.getCoord_y()) > int(topLeftCorner_y) - int(length):
                    squareList.append(elem)
        return squareList
    else:
        raise ValueError("Coordinates must be numbers!")

def minDistance(pointList):
    '''

    :param pointList: The list
    :return: The minimum distance between 2 points
    '''
    if len(pointList) < 2:
        raise ValueError("Not enough points!")
    else:
        for i in range(len(pointList)):
            for j in range(i+1,len(pointList)):
                dist = math.sqrt((pointList[j].getCoord_x() - pointList[i].getCoord_x()) ** 2 + (pointList[j].getCoord_y() - pointList[i].getCoord_y()) ** 2)

                minimum= dist
                if (dist < minimum):
                    minimum = dist
    return minimum

def updateAtIndex(pointList,index,newCoord_x,newCoord_y,newColor):
    '''

    :param pointList: The list
    :param index: The given index
    :param newCoord_x: coord
    :param newCoord_y: coord
    :param newColor: The new color
    :return: The updated list
    '''

    if index >= 0 and index < len(pointList):
        pointList[index].setCoord_x(newCoord_x)
        pointList[index].setCoord_y(newCoord_y)
        pointList[index].setColor(newColor)
    else:
        raise ValueError("Invalid index!")

def delByIndex(pointList, index):
    '''
    :param pointList: The list
    :param index: The given index
    :return: The updated list
    '''

    if index >= 0 and index < len(pointList):
        del(pointList[index])
    else:
        raise ValueError("Invalid index!")

def delInSquare(pointList,topLeftCorner_x,topLeftCorner_y,lenght):
    '''

    :param pointList: The list
    :param topLeftCorner_x: coord
    :param topLeftCorner_y: coord
    :param lenght: The length
    :return: The updated list
    '''

    if isNumber(topLeftCorner_x) and isNumber(topLeftCorner_y) and isNumber(lenght):
        i = 0
        while i < len(pointList):
            if pointList[i].getCoord_x() > topLeftCorner_x and pointList[i].getCoord_y() < topLeftCorner_y and pointList[i].getCoord_x() < topLeftCorner_x + lenght and pointList[i].getCoord_y() > topLeftCorner_y - lenght:
                    del(pointList[i])
            else:
                i += 1
    else:
        raise ValueError("Coordinates must be numbers!")

def char(pointList):

    x = []
    y = []
    col = []
    for elem in pointList:
        x.append(elem.getCoord_x())
        y.append(elem.getCoord_y())
        col.append(elem.getColor())
    plt.scatter(x, y, c=col)
    plt.show()

def dist(point1,point2):
    '''

    :param point1: The first point
    :param point2: The second point
    :return: The distance between the points
    '''

    dist = math.sqrt((point2.getCoord_x() - point1.getCoord_x()) ** 2 + (
                point2.getCoord_y() - point1.getCoord_y()) ** 2)
    return dist

def maxDistance(pointList):
    '''

    :param pointList: The list
    :return: The maximum distance
    '''

    # 13
    maximum = 0
    dist = 0
    if len(pointList) < 2:
        raise ValueError("Not enough points!")
    else:
        for i in range(len(pointList)):
            for j in range(i+1,len(pointList)):
                dist = math.sqrt((pointList[j].getCoord_x() - pointList[i].getCoord_x()) ** 2 + (pointList[j].getCoord_y() - pointList[i].getCoord_y()) ** 2)
                if (dist > maximum):
                    maximum = dist
    return maximum

def Shiftx (pointList,shift):
    '''

    :param pointList: The list
    :param shift: The shift
    :return: The updated list
    '''

    if isNumber(shift):
        for elem in pointList:
            elem.setCoord_x(elem.getCoord_x() + shift)
    else:
        raise ValueError("Shift must be a number!")

def deleteWithinDistance(pointList,distance,point):
    '''

    :param pointList: The list
    :param distance: The given distance
    :param point: The point we verify
    :return:
    '''

    # 20
    if isNumber(distance):
        i = 0
        while i < len(pointList):
            if dist(pointList[i],point) <= distance:
                del(pointList[i])
            else:
                i += 1
    else:
        raise ValueError("The distance must be a number!")
