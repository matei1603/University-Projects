import VectorRepository
import MyVector
import runAllLogicTests
import runAllMainTests

def printMenu():
    msg = "**************************** \n"
    msg += "\t 1. Add a scalar  \n"
    msg += "\t 2. Add two vectors \n"
    msg += "\t 3. Subtract two vectors \n"
    msg += "\t 4. Multiply two vectors \n"
    msg += "\t 5. Sum of elements in a vector \n"
    msg += "\t 6. Product of elements in a vector \n"
    msg += "\t 7. Average of elements in a vector \n"
    msg += "\t 8. Min of a vector \n"
    msg += "\t 9. Max of a vector \n"
    msg += "\t 10. Add a vector to the repository \n"
    msg += "\t 11. Get all vectors \n"
    msg += "\t 12. Get a vector at a given index \n"
    msg += "\t 13. Update a vector at a given index \n"
    msg += "\t 14. Update a vector identified by name_id \n"
    msg += "\t 15. Delete a vector by index \n"
    msg += "\t 16. Delete a vector by name_id \n"
    msg += "\t 17. Plot all vectors in a chart based on the type and colour of each vector \n"
    msg += "\t 18. Vector data examples \n"
    msg += "\t 19. Repository data examples \n"
    msg += "\t 20. Exit \n"
    msg += "****************************"
    print(msg)

def vectorDataExamples():
    '''
    Data examples on vector operations
    :return:
    '''
    vector = MyVector(1,'g',3,[2,3,4])
    vector1 = MyVector(3,'r',4,[4,3,2])

    print("Initial values: ")
    print(vector.__repr__())
    print(vector1.__repr__())
    print()

    vector.addScalar(1)
    print(vector.__repr__())
    # ( 1, 'g', 2, [3, 4, 5] )
    print()

    vector.addVectors(vector1)
    print(vector.__repr__())
    # ( 1, 'g', 3, [5, 6, 6] )
    print()

    vector.subtract(vector1)
    print(vector.__repr__())
    # ( 1, 'g', 3, [-2, 0, 2] )
    print()

    print(vector.multiplication(vector1))
    #25
    print()

    print(vector.sumElements())
    #17
    print()

    print(vector.product())
    # 24
    print()

    print(vector.average())
    # 2.83333
    print()

    print(vector.minimum())
    # 2
    print()

    print(vector.maximum())
    #6
    print()

    print(vector1.average())
    print()

def repoDataExamples():
    '''
    :return:
    '''
    print("Initial values: ")
    print(VectorRepository.__repr__())
    print()

    v1 = MyVector(2,'g',3,[2,3,4])
    VectorRepository.add(v1)
    print(VectorRepository.getAllVectors())
    print()

    v2 = MyVector(3,'r',1,[2,3,5])
    VectorRepository.add(v2)
    print(VectorRepository.getAllVectors())
    print()

    print(VectorRepository.getVectorAtIndex(1))
    print()

    VectorRepository.updateVectorAtIndex(1,2,'g',2,[1, 2, 3])
    print(VectorRepository.getAllVectors())
    print()

    VectorRepository.updateVectorByName_id(1,2,'g',3,[2, 3, 4])
    print(VectorRepository.getAllVectors())
    print()

    VectorRepository.deleteVectorByIndex(0)
    print(VectorRepository.getAllVectors())
    print()

    v3 = MyVector(1,'r',1,[3, 5, 6])
    VectorRepository.add(v3)
    print(VectorRepository.getAllVectors())
    print()

    VectorRepository.deleteVectorByName_id(1)
    print(VectorRepository.getAllVectors())
    print()

    v4 = MyVector(1,'g',1,[2,2,5])
    VectorRepository.add(v4)
    print(VectorRepository.getAllVectors())
    print()


    print(VectorRepository.getVectorAtIndex(0))
    print()

def start():
    vrepo = VectorRepository()
    stop = False
    while stop == False:
        try:
            printMenu()
            option = int(input("Select an option: "))
            runAllLogicTests()
            runAllMainTests()
            if option == 1:
                name_id = int(input("Enter name_id: "))
                colour = input("Enter the colour: ")
                type = int(input("Enter the type: "))
                values = []
                n = int(input("Enter the number of elements of the values: "))
                for i in range(n):
                    elem = int(input("Enter the element: "))
                    values.append(elem)
                scalar = int(input("Enter the scalar: "))
                try:
                    vector = MyVector(name_id,colour,type,values)
                    vector.addScalar(scalar)
                    print(vector.__repr__())
                except ValueError as ve:
                    print(ve)
            elif option == 2:
                name_id = int(input("Enter name_id: "))
                colour1 = input("Enter the colour: ")
                type1 = int(input("Enter the type: "))
                values1 = []
                n = int(input("Enter the number of elements of the values: "))
                for i in range(n):
                    elem1 = int(input("Enter the element: "))
                    values1.append(elem1)
                name_id2 = int(input("Enter name_id: "))
                colour2 = input("Enter the colour: ")
                type2 = int(input("Enter the type: "))
                values2 = []
                n2 = int(input("Enter the number of elements of the values: "))
                for i in range(n2):
                    elem2 = int(input("Enter the element: "))
                    values2.append(elem2)
                try:
                    vector = MyVector(name_id,colour1,type1,values1)
                    vector1 = MyVector(name_id2,colour2,type2,values2)
                    vector.addVectors(vector1)
                    print(vector.__repr__())
                except ValueError as ve:
                    print(ve)
            elif option == 3:
                name_id = int(input("Enter name_id: "))
                colour1 = input("Enter the colour: ")
                type1 = int(input("Enter the type: "))
                values1 = []
                n = int(input("Enter the number of elements of the values: "))
                for i in range(n):
                    elem1 = int(input("Enter the element: "))
                    values1.append(elem1)
                name_id2 = int(input("Enter name_id: "))
                colour2 = input("Enter the colour: ")
                type2 = int(input("Enter the type: "))
                values2 = []
                n2 = int(input("Enter the number of elements of the values: "))
                for i in range(n2):
                    elem2 = int(input("Enter the element: "))
                    values2.append(elem2)
                try:
                    vector = MyVector(name_id,colour1,type1,values1)
                    vector1 = MyVector(name_id2,colour2,type2,values2)
                    vector.subtract(vector1)
                    print(vector.__repr__())
                except ValueError as ve:
                    print(ve)
            elif option == 4:
                name_id = int(input("Enter name_id: "))
                colour1 = input("Enter the colour: ")
                type1 = int(input("Enter the type: "))
                values1 = []
                n = int(input("Enter the number of elements of the values: "))
                for i in range(n):
                    elem1 = int(input("Enter the element: "))
                    values1.append(elem1)
                name_id2 = int(input("Enter name_id: "))
                colour2 = input("Enter the colour: ")
                type2 = int(input("Enter the type: "))
                values2 = []
                n2 = int(input("Enter the number of elements of the values: "))
                for i in range(n2):
                    elem2 = int(input("Enter the element: "))
                    values2.append(elem2)
                try:
                    vector = MyVector(name_id,colour1,type1,values1)
                    vector1 = MyVector(name_id2,colour2,type2,values2)
                    vector.multiplication(vector1)
                    print(vector.__repr__())
                except ValueError as ve:
                    print(ve)
            elif option == 5:
                name_id = int(input("Enter name_id: "))
                colour1 = input("Enter the colour: ")
                type1 = int(input("Enter the type: "))
                values1 = []
                n = int(input("Enter the number of elements of the values: "))
                for i in range(n):
                    elem1 = int(input("Enter the element: "))
                    values1.append(elem1)
                try:
                    vector = MyVector(name_id,colour1,type1,values1)
                    print(vector.sumElements())
                except ValueError as ve:
                    print(ve)
            elif option == 6:
                name_id = int(input("Enter name_id: "))
                colour1 = input("Enter the colour: ")
                type1 = int(input("Enter the type: "))
                values1 = []
                n = int(input("Enter the number of elements of the values: "))
                for i in range(n):
                    elem1 = int(input("Enter the element: "))
                    values1.append(elem1)
                try:
                    vector = MyVector(name_id, colour1, type1, values1)
                    print(vector.product())
                except ValueError as ve:
                    print(ve)
            elif option == 7:
                name_id = int(input("Enter name_id: "))
                colour1 = input("Enter the colour: ")
                type1 = int(input("Enter the type: "))
                values1 = []
                n = int(input("Enter the number of elements of the values: "))
                for i in range(n):
                    elem1 = int(input("Enter the element: "))
                    values1.append(elem1)
                try:
                    vector = MyVector(name_id, colour1, type1, values1)
                    print(vector.average())
                except ValueError as ve:
                    print(ve)
            elif option == 8:
                name_id = int(input("Enter name_id: "))
                colour1 = input("Enter the colour: ")
                type1 = int(input("Enter the type: "))
                values1 = []
                n = int(input("Enter the number of elements of the values: "))
                for i in range(n):
                    elem1 = int(input("Enter the element: "))
                    values1.append(elem1)
                try:
                    vector = MyVector(name_id, colour1, type1, values1)
                    print(vector.minimum())
                except ValueError as ve:
                    print(ve)
            elif option == 9:
                name_id = int(input("Enter name_id: "))
                colour1 = input("Enter the colour: ")
                type1 = int(input("Enter the type: "))
                values1 = []
                n = int(input("Enter the number of elements of the values: "))
                for i in range(n):
                    elem1 = int(input("Enter the element: "))
                    values1.append(elem1)
                try:
                    vector = MyVector(name_id, colour1, type1, values1)
                    print(vector.maximum())
                except ValueError as ve:
                    print(ve)
            elif option == 10:
                name_id = int(input("Enter name_id: "))
                colour1 = input("Enter the colour: ")
                type1 = int(input("Enter the type: "))
                values1 = []
                n = int(input("Enter the number of elements of the values: "))
                for i in range(n):
                    elem1 = int(input("Enter the element: "))
                    values1.append(elem1)
                try:
                    vector = MyVector(name_id, colour1, type1, values1)
                    vrepo.add(vector)
                except ValueError as ve:
                    print(ve)
            elif option == 11:
                vrepo.getAllVectors()
            elif option == 12:
                index =  int(input("Enter the index: "))
                try:
                    vrepo.getVectorAtIndex(index)
                except ValueError as ve:
                    print(ve)
            elif option == 13:
                index = int(input("Enter the index: "))
                newName_id = int(input("Enter name_id: "))
                newColour = input("Enter the colour: ")
                newType = int(input("Enter the type: "))
                newValues = []
                newN = int(input("Enter the number of elements of the values: "))
                for i in range(newN):
                    newElem = int(input("Enter the element: "))
                    newValues.append(newElem)
                try:
                    vrepo.updateVectorAtIndex(index,newName_id,newColour,newType, newValues)
                except ValueError as ve:
                    print(ve)
            elif option == 14:
                name_id = int(input("Enter the index: "))
                newName_id = int(input("Enter name_id: "))
                newColour = input("Enter the colour: ")
                newType = int(input("Enter the type: "))
                newValues = []
                newN = int(input("Enter the number of elements of the values: "))
                for i in range(newN):
                    newElem = int(input("Enter the element: "))
                    newValues.append(newElem)
                try:
                    vrepo.updateVectorByName_id(name_id, newName_id, newColour, newType, newValues)
                except ValueError as ve:
                    print(ve)
            elif option == 15:
                index = int(input("Enter the index: "))
                try:
                    vrepo.deleteVectorByIndex(index)
                except ValueError as ve:
                    print(ve)
            elif option == 16:
                name_id = int(input("Enter name_id: "))
                try:
                    vrepo.deleteVectorByName_id(name_id)
                except ValueError as ve:
                    print(ve)
            elif option == 17:
                vrepo.chartByTypeAndColour()
            elif option == -1:
                vectorDataExamples()
            elif option == -2:
                repoDataExamples()
            elif option == 0:
                print("END")
                stop = True
            else:
                print("Invalid !")
        except ValueError:
            print("Invalid !")