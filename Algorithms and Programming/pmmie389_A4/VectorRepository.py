import logic
import matplotlib.pyplot as plt


class VectorRepository:
    def __init__(self):
        self.__data = []

    def add(self,vector):
        for i in range(len(self.__data)):
            if self.__data[i].getName_Id() == vector.getName_Id():
                raise ValueError("Name_id is supposed to be unique!")
        self.__data.append(vector)

    def getSize(self):
        '''
        :return: The size
        '''
        return len(self.__data)

    def getAllVectors(self):
        '''

        :return: All vectors
        '''
        return self.__data

    def getVectorAtIndex(self,index):
        '''

        :param index: The index
        :return: The vector at the specified index
        '''
        if logic.isInt(index):
            if index >= 0 and index < len(self.__data):
                return self.__data[index].__repr__()
            else:
                raise ValueError("The index is invalid!")

    def updateVectorAtIndex(self,index,newName_id,newColour,newType,newValues):
        '''

        :param index: the index
        :param newName_id: the new id
        :param newColour: the new color
        :param newType: the new type
        :param newValues: the new values
        :return: The updated vector
        '''
        if logic.isInt(index):
            if index >= 0 and index < len(self.__data) and logic.isInt(index):
                for i in range(len(self.__data)):
                    if self.__data[i].getName_Id() == newName_id:
                        raise ValueError("Name_id must be unique!")
                self.__data[index].setName_Id(newName_id)
                self.__data[index].setColour(newColour)
                self.__data[index].setType(newType)
                self.__data[index].setValues(newValues)
            else:
                raise ValueError("The index is invalid!")

    def updateVectorByName_id(self,name_id,newName_id,newColour,newType,newValues):
        '''
        :param name_id: the new id
        :param newName_id: the new name
        :param newColour: the new color
        :param newType: the new type
        :param newValues: the new values
        :return: the updated vector
        '''
        i = 0
        while i < len(self.__data):
            if self.__data[i].getName_Id() == name_id:
                for j in range(len(self.__data)):
                    if self.__data[i].getName_Id() == newName_id:
                        raise ValueError("The introduced Name_id must be different!")
                self.__data[i].setName_Id(newName_id)
                self.__data[i].setColour(newColour)
                self.__data[i].setType(newType)
                self.__data[i].setValues(newValues)
                break
            else:
                i += 1

    def deleteVectorByIndex(self,index):
        '''
        :param index: the index
        :return: the updated vector
        '''
        if logic.isInt(index):
            if index >= 0 and index < len(self.__data) and logic.isInt(index):
                del(self.__data[index])
            else:
                raise ValueError("The index is invalid!")

    def deleteVectorByName_id(self,name_id):
        '''
        :param name_id:
        :return: the updated vector
        '''
        i = 0
        while i < len(self.__data):
            if self.__data[i].getName_Id() == name_id:
                del(self.__data[i])
                break
            else:
                i += 1

    def chartByTypeAndColour(self):
        '''
        :return:
        '''
        for i in range(len(self.__data)):
            vec_type = self.__data[i].getType()
            vec_color = self.__data[i].getColour()
            vec_ind = []
            for j in range(len(self.__data[i].getValues())):
                vec_ind.append(j)
            vec_val = self.__data[i].getValues()
            if vec_type == 1:
                m = 'o'
            elif vec_type == 2:
                m = 's'
            elif vec_type == 3:
                m = 'v'
            else:
                m = 'd'
            plt.scatter(vec_indices,vec_val,c=vec_color,marker=m)
        plt.show()

    def __repr__(self):
        return str(self.__data)
