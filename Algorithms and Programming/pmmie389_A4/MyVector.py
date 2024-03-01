import logic
import numpy as np

class MyVector:
    def __init__(self, name_id, colour, type, values):
        self.__name_id = name_id
        if colour in ['r', 'g', 'b', 'y', 'm']:
            self.__colour = colour
        else:
            raise ValueError("The color is invalid!")
        if logic.isIntGZero(type):
            self.__type = type
        else:
            raise ValueError("The type must be an int > 0!")
        self.__values = np.array(values[:])

    def getName_Id(self):
        return self.__name_id

    def getColour(self):
        return self.__colour

    def getType(self):
        return self.__type

    def getValues(self):
        return self.__values[:]

    def setName_Id(self,newName_id):
        self.__name_id = newName_id

    def setColour(self,newColour):
        if newColour in ['r', 'g', 'b', 'y', 'm']:
            self.__colour = newColour
        else:
            raise ValueError("The color is invalid!")

    def setType(self,newType):
        if logic.isIntGZero(newType):
            self.__type = newType
        else:
            raise ValueError("The type is invalid!")

    def setValues(self,newValues):
        self.__values = np.array(newValues[:])

    def addScalar(self,value):
        '''
        :param value: The value
        :return: The updated vector
        '''
        if logic.isNumber(value):
            for i in range(len(self.__values)):
                self.__values[i] += value
        else:
            raise ValueError("The introduced scalar is not a number!")

    def length(self, other):
        '''
        :param other: MyVector
        :return: The updated vector
        '''
        if len(self.__values) == len(other.getValues()):
            if len(self.__values) == 0:
                return None
            for i in range(len(self.__values)):
                self.__values[i] += other.getValues()[i]
        else:
            raise ValueError("The vectors do not have the same length!")

    def subtract(self,other):
        '''

        :param other: MyVector
        :return: The updated vector
        '''
        if len(self.__values) == len(other.getValues()):
            if len(self.__values) == 0:
                return None
            for i in range(len(self.__values)):
                self.__values[i] -= other.getValues()[i]
        else:
            raise ValueError("The vectors do not have the same length!")

    def multiplication(self,other):
        '''
        :param other: MyVector
        :return:The updated vector
        '''
        summ = 0
        if len(self.__values) == len(other.getValues()):
            if len(self.__values) == 0:
                raise ValueError("Empty array!")
            for i in range(len(self.__values)):
                self.__values[i] *= other.getValues()[i]
            for i in range(len(self.__values)):
                summ += self.__values[i]
            return summ
        else:
            raise ValueError("The vectors do not have the same length!")

    def sumElements(self):
        '''

        :return:The sum
        '''
        summ=0
        if len(self.__values) == 0:
            raise ValueError("The vector is empty!")
        for i in range(len(self.__values)):
            summ = summ + self.__values[i]
        return summ


    def product(self):
        '''
        :return:The product
        '''
        product = 1
        if len(self.__values) == 0:
            raise ValueError("The vector is empty!")
        for i in range(len(self.__values)):
            product = product * self.__values[i]
        return product

    def average(self):
        '''
        Returns the average of the array
        :return:The avg
        '''
        summ = 0
        if len(self.__values) == 0:
            raise ValueError("The vector is empty!")
        for i in range(len(self.__values)):
            summ += self.__values[i]
        return summ/len(self.__values)

    def minimum(self):
        '''
        :return: The minimum
        '''
        if len(self.__values) == 0:
            raise ValueError("The vector is empty!")
        return self.__values.min()

    def maximum(self):
        '''
        :return: The maximum
        '''
        if len(self.__values) == 0:
            raise ValueError("The vector is empty!")
        return self.__values.max()

    def __repr__(self):
        return "( " + str(self.__name_id) + ', ' + self.__colour + ', ' + str(self.__type) + ', ' + str(self.__values) + " )"