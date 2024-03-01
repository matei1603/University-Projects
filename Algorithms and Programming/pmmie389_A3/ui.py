from repository import PointRepository
from point import MyPoint
import test

def print_input_menu():

    msg = "Menu:\n"
    msg += "\t 1. Add a point to the repository\n"
    msg += "\t 2. Get all points\n"
    msg += "\t 3. Get a point at a given index\n"
    msg += "\t 4. Get all points of a given color\n"
    msg += "\t 5. Get all points that are inside a given square\n"
    msg += "\t 6. Get the minimum distance between two points\n"
    msg += "\t 7. Update a point at a given index\n"
    msg += "\t 8. Delete a point by index\n"
    msg += "\t 9. Delete all points that are inside a given square\n"
    msg += "\t 10. Plot all points in a chart\n"
    msg += "\t 13. Get the maximum distance between two points\n"
    msg += "\t 16. Shift all points on the x axis\n"
    msg += "\t 20. Delete all points within a certain distance from a given point\n"
    msg += "\t 100. Data examples\n"
    msg += "\t 0. Exit\n"
    print(msg)


def dataExamples():

    PointRepository.addPoint(1,1,"red")
    PointRepository.addPoint(2,2,"blue")
    PointRepository.addPoint(3,3,"green")
    PointRepository.addPoint(4,4,"yellow")
    PointRepository.addPoint(5,5,"magenta")

    print("Initial values:")
    print(str(PointRepository.getAllPoints()))
    print()

    print("1 - Add a point")
    PointRepository.addPoint(1, 2, "red")
    print(PointRepository.getAllPoints())
    print()

    print("2 - Get all points")
    print(PointRepository.getAllPoints())
    print()

    print("3 - Get point by index (0)")
    print(PointRepository.getPointAtIndex(0))
    print()

    print("4 - Get point by color(red)")
    print(PointRepository.getPointByColor("red"))
    print()

    print("5 - Point in square (8,2,1)")
    print(PointRepository.pointsInSquare(8, 2, 1))
    print()

    print("6 - The minimum distance between 2 points")
    print(PointRepository.minDistance())
    print()

    print("7 - Update a point at a given index (0)")
    PointRepository.updateAtIndex(2, 13, 5, "green")
    print(PointRepository.getAllPoints())
    print()

    print("8 - Delete at index (3)")
    PointRepository.delByIndex(3)
    print(PointRepository.getAllPoints())
    print()

    print("9 - Delete all points that are inside the square (2,8,4)")
    PointRepository.delInSquare(2, 8, 4)
    print(PointRepository.getAllPoints())
    print()

    print("13 - The maximum distance between 2 points")
    print(PointRepository.maxDistance())
    print()

    print("16 - Shift all points on the x-axis by 3")
    PointRepository.shiftOnX(3)
    print(PointRepository.getAllPoints())
    print()

    print("20 - Delete all points within distance = 2 from the point (2,6,blue)")
    point = MyPoint(2,6,"blue")
    PointRepository.deleteWhithinDistance(2,point)
    print(PointRepository.getAllPoints())
    print()

def main():
    test.runAllTests()

    stop = False
    while stop == False:
        try:
            print_input_menu()
            command = int(input("Please select a command: "))
            if command == 1:
                x = int(input("Please enter x: "))
                y = int(input("Please enter y: "))
                color = input("Please enter the color: ")
                try:
                    PointRepository.addPoint(x,y,color)
                except ValueError as ve:
                    print(ve)
            elif command == 2:
                print(PointRepository.getAllPoints())
            elif command == 3:
                index = int(input("Enter the index: "))
                try:
                    print(PointRepository.getPointAtIndex(index))
                except ValueError as ve:
                    print(ve)
            elif command == 4:
                color = input("Enter the color: ")
                try:
                    print(PointRepository.getPointByColor(color))
                except ValueError as ve:
                    print(ve)
            elif command == 5:
                topLeftCorner_x = int(input("Enter the top left corner x: "))
                topLeftCorner_y = int(input("Enter the top left corner y: "))
                lenght = int(input("Enter the length: "))
                try:
                    print(PointRepository.pointsInSquare(topLeftCorner_x,topLeftCorner_y,lenght))
                except ValueError as ve:
                    print(ve)
            elif command == 6:
                try:
                    print(PointRepository.minDistance())
                except ValueError as ve:
                    print(ve)
            elif command == 7:
                index = int(input("Enter the index: "))
                newCoord_x = int(input("Enter the new x: "))
                newCoord_y = int(input("Enter the new y: "))
                newColor = input("Enter the new color: ")
                try:
                    print(PointRepository.updateAtIndex(index,newCoord_x,newCoord_y,color))
                except ValueError as ve:
                    print(ve)
            elif command == 8:
                index = int(input("Enter the index: "))
                try:
                    print(PointRepository.delByIndex(index))
                except ValueError as ve:
                    print(ve)
            elif command == 9:
                topLeftCorner_x = int(input("Enter the top left corner x: "))
                topLeftCorner_y = int(input("Enter the top left corner y: "))
                lenght = int(input("Enter the length: "))
                try:
                    print(PointRepository.delInSquare(topLeftCorner_x,topLeftCorner_y,lenght))
                except ValueError as ve:
                    print(ve)
            elif command == 10:
                PointRepository.chart()
            elif command == 13:
                try:
                    print(PointRepository.maxDistance())
                except ValueError as ve:
                    print(ve)
            elif command == 16:
                shift = int(input("Enter shift: "))
                try:
                    print(PointRepository.shiftOnX(shift))
                except ValueError as ve:
                    print(ve)
            elif command == 20:
                x = int(input("Please enter the x: "))
                y = int(input("Please enter the y: "))
                color = input("Please enter the color: ")
                point = MyPoint(2,3,"magenta")
                try:
                    point.setCoord_x(x)
                except ValueError as ve:
                    print(ve)
                try:
                    point.setCoord_y(y)
                except ValueError as ve:
                    print(ve)
                try:
                    point.setColor(color)
                except ValueError as ve:
                    print(ve)
                distance = int(input("Enter the distance: "))
                try:
                    PointRepository.deleteWhithinDistance(distance,point)
                except ValueError as ve:
                    print(ve)
            elif command == 0:
                print("You have finished!")
                stop = True
            elif command == 100:
                dataExamples()
            else:
                print("Invalid command!")
        except ValueError as ve:
            print(ve)