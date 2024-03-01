class MyPoint:
    def __init__(self, coord_x, coord_y, color):
        self.__coord_x = coord_x
        self.__coord_y = coord_y
        if color in ["red", "green","blue","yellow", "magenta"]:
            self.__color = color
        else:
            raise ValueError("The color is not correct!")
    def getCoord_x(self):
        return self.__coord_x
    def getCoord_y(self):
        return self.__coord_y
    def getColor(self):
        return self.__color

    def setCoord_x(self, NewCoord_x):
        self.__coord_x= NewCoord_x
    def setCoord_y(self, NewCoord_y):
        self.__coord_X= NewCoord_y
    def setcolor(self, NewColor):
        if NewColor in ["red", "green","blue","yellow", "magenta"]:
            self.__color = NewColor
        else:
            raise ValueError("The color is not correct!")
    def __str__(self):
        return "(" + str(self.getCoord_x()) +"," + str(self.getCoord_y()) + ")" + " of color " + str(self.getColor())
p = MyPoint(1, 2, "yellow")
print(p)
try:
    pp=MyPoint(3, 4, "black")
except ValueError as ve:
    print(ve)
print(p)

