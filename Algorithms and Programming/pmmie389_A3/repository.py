import logic


class PointRepository:
    def __init__(self):
        self.__PointList = []

    def getPointAtIndex(self,index):
        return logic.getPointAtIndex(self.__PointList, index)

    def getPointByColor(self,color):
        return logic.getPointsWithColor(self.__PointList, color)

    def pointsInSquare(self, topLeftCorner_x, topLeftCorner_y, length):
        return logic.pointsInSquare(self.__PointList, topLeftCorner_x, topLeftCorner_y, length)

    def minDistance(self):
        return logic.minDistance(self.__PointList)

    def updateAtIndex(self,index,newCoord_x,newCoord_y,newColor):
        return logic.updateAtIndex(self.__PointList, index, newCoord_x, newCoord_y, newColor)

    def delByIndex(self,index):
        return logic.delByIndex(self.__PointList, index)


    def delInSquare(self, topLeftCorner_x, topLeftCorner_y, length):
        return logic.delInSquare(self.__PointList, topLeftCorner_x, topLeftCorner_y, length)

    def chart(self):
        return logic.char(self.__PointList)

    def deleteWhithinDistance(self,distance,point):
        return logic.deleteWithinDistance(self.__PointList, distance, point)

    def maxDistance(self):
        return logic.maxDistance(self.__PointList)

    def shiftOnX(self,shift):
        return logic.shiftOnX(self.__PointList, shift)

    def __repr__(self):
        return str(self.__PointList)


    def __str__(self):
        return str(self.__PointList)
