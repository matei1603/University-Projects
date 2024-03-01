import helper
import criterias
import Plane
import Passenger


class Airport:
    '''
    The airport class
    '''
    def __init__(self):
        self.__data = []

    def getSize(self):
        '''
        Gets the size
        :return:
        '''
        return len(self.__data)

    def add(self,plane):
        '''
        :param plane: the plane
        :return:
        '''
        self.__data.append(plane)

    def getAllPlanes(self):
        '''
        Gets all planes
        :return:
        '''
        return self.__data[:]

    def deletePlaneAtIndex(self,index):
        '''
        :param index: the index
        :return:
        '''
        if helper.isInt(index):
            if index >= 0 and index < len(self.__data):
                del(self.__data[index])
            else:
                raise ValueError("The index is invalid!")
        else:
            raise ValueError("The index is invalid!")

    def __repr__(self):
        return str(self.__data)

    def sortPassengersByLastName(self, index):
        '''
        :param index: the index
        :return:
        '''
        if helper.isInt(index):
            if index >= 0 and index < len(self.__data):
                helper.bubbleSort(self.__data[index].getListOfPassengers(), criterias.sortByLastName)
            else:
                raise ValueError("The index is invalid!")
        else:
            raise ValueError("The index is invalid!")

    def sortPlanesByNumberOfPassengers(self):
        '''
        :return:
        '''
        if len(self.__data) == 0:
            raise ValueError("The airport is empty!")
        else:
            helper.bubbleSort(self.__data, criterias.sortByLen)

    def sortByNumberOfPassengersFirstName(self, startingSubstring):
        if len(self.__data) == 0:
            raise ValueError("The airport is empty!")
        else:
            helper.bubbleSort(self.__data, criterias.sortByStartingSubstring, startingSubstring)

    def sortPlanesAccordingToConcatenation(self):
        '''
        :return:
        '''
        if len(self.__data) == 0:
            raise ValueError("The airport is empty!")
        else:
            return helper.bubbleSort(self.__data,criterias.sortByConcatenation)

    def identifyByPassengerFirst3(self):
        '''
        :return:
        '''
        if len(self.__data) == 0:
            raise ValueError("The airport is empty!")
        else:
            return helper.search(self.__data,criterias.findByFirst3)

    def identifyByNameContainingString(self,index,containString):
        '''
        :param index: the index
        :param containString:
        :return:
        '''
        if len(self.__data) == 0:
            raise ValueError("The airport is empty!")
        else:
            if helper.isInt(index):
                if index >= 0 and index < len(self.__data):
                    return helper.search(self.__data[index].getListOfPassengers(), criterias.findByString,containString)
                else:
                    raise ValueError("The index is invalid!")
            else:
                raise ValueError("The index is invalid!")

    def identifyPlaneByPassengerName(self, name):
        '''
        :param name: string
        :return:
        '''
        if len(self.__data) == 0:
            raise ValueError("The airport is empty!")
        else:
            return helper.search(self.__data, criterias.findByName, name)

    def backtrackk(self, groups, current_group, planes, k, destination, airline):
        if len(current_group) == k:
            groups.append(current_group)
            return

        airlines = set()
        for plane in planes:
            if plane.destination != destination or plane.airline == airline or plane.airline in airlines:
                continue
            airlines.add(plane.airline)
            self.backtrackk(groups, current_group + [plane], planes, k, destination, airline)

    def form_groups_by_destination_and_airline(self, k, destination, airline):
        groups = []
        self.backtrackk(groups, [], self.planes, k, destination, airline)
        return groups