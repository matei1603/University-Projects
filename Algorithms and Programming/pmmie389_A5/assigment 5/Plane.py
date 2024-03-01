import helper


class Plane:
    '''
    Plane class with the requested elements
    '''
    def __init__(self, number, airline, numberOfSeats,destination,listOfPassengers):
        if helper.isInt(number):
            self.__number = number
        else:
            raise ValueError("Is not an int!")
        self.__airline = airline
        if helper.isInt(numberOfSeats):
            self.__numberOfSeats = numberOfSeats
        else:
            raise ValueError("Is not an int!")
        self.__destination = destination
        if len(listOfPassengers) <= numberOfSeats:
            self.__listOfPassengers = listOfPassengers[:]
        else:
            raise ValueError("The number of seats is smaller!")

    def getNumber(self):
        '''
        Gets number
        :return:
        '''
        return self.__number

    def getAirline(self):
        '''
        Gets airline
        :return:
        '''
        return self.__airline

    def getNumberOfSeats(self):
        '''
        Gets no of seats
        :return:
        '''
        return self.__numberOfSeats

    def getDestination(self):
        '''
        Gets destination
        :return:
        '''
        return self.__destination

    def getListOfPassengers(self):
        '''
        Gets list of pass.
        :return:
        '''
        return self.__listOfPassengers

    def setNumber(self, newNumber):
        '''
        :param newNumber: the new number
        :return:
        '''
        if helper.isInt(newNumber):
            self.__number = newNumber
        else:
            raise ValueError("Is not an int!")

    def setAirline(self,newAirline):
        '''
        :param newAirline: the new airline
        :return:
        '''
        self.__airline = newAirline

    def setNumberOfSeats(self, newNumberOfSeats):
        '''

        :param newNumberOfSeats: the new number of seats
        :return:
        '''
        if helper.isInt(newNumberOfSeats):
            self.__numberOfSeats = newNumberOfSeats
        else:
            raise ValueError("Is not an int!")

    def setDestination(self, newDestination):
        '''
        :param newDestination: the new destination
        :return:
        '''
        self.__destination = newDestination

    def addPassenger(self, passenger):
        '''
        :param passenger: the passenger
        :return:
        '''
        if len(self.__listOfPassengers) < self.__numberOfSeats:
            self.__listOfPassengers.append(passenger)
        else:
            raise ValueError("There are no other beds!")

    def updatePassengerAtIndex(self,index,newFirstName,newLastName,newPassNumber):
        '''
        :param index: the index
        :param newFirstName: the new first name
        :param newLastName: the new last name
        :param newPassNumber: the new pass no
        :return:
        '''
        if helper.isInt(index):
            if index >= 0 and index < len(self.__listOfPassengers):
                self.__listOfPassengers[index].setFirstName(newFirstName)
                self.__listOfPassengers[index].setLastName(newLastName)
                if helper.isInt(newPassNumber):
                    self.__listOfPassengers[index].setPassNumber(newPassNumber)
                else:
                    raise ValueError("The pass no is invalid!")
            else:
                raise ValueError("The index is invalid!")
        else:
            raise ValueError("The index is invalid!")

    def deleteAtIndex(self,index):
        '''
        :param index: the index
        :return:
        '''
        if helper.isInt(index):
            if index >= 0 and index < len(self.__listOfPassengers):
                del(self.__listOfPassengers[index])
            else:
                raise ValueError("The index is invalid!")
        else:
            raise ValueError("The index is invalid!")

    def backtrack(self, groups, current_group, passengers, k):
        if len(current_group) == k:
            groups.append(current_group)
            return

        last_names = set()
        for passenger in passengers:
            if passenger.last_name in last_names:
                continue
            last_names.add(passenger.last_name)
            self.backtrack(groups, current_group + [passenger], passengers, k)

    def form_groups_by_lastname(self, k):
        groups = []
        self.backtrack(groups, [], self.passengers, k)
        return groups

    def __repr__(self):
        return "(" + str(self.__number) + ", " + self.__airline + ", " + str(self.__numberOfSeats) + ", " + self.__destination + ", " + str(self.__listOfPassengers) + ")"
