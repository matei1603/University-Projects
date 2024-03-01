import helper

class Passenger:
    '''
    Passenger class with first name, last name, passport number
    '''
    def __init__(self, firstName,lastName, passNumber):
        self.__firstName = firstName
        self.__lastName = lastName
        if helper.isInt(passNumber):
            self.__passNumber = passNumber
        else:
            raise ValueError("The passport number is not an int!")

    def getFirstName(self):
        '''
        Gets first name
        :return:
        '''
        return self.__firstName

    def getLastName(self):
        '''
        Gets last name
        :return:
        '''
        return self.__lastName

    def getPassNumber(self):
        '''
        Gets passport number
        :return:
        '''
        return self.__passNumber

    def setFirstName(self, newFirstName):
        '''
        Sets first name
        :param newFirstName: the new first name
        :return:
        '''
        self.__firstName = newFirstName

    def setLastName(self, newLastName):
        '''
        Sets last name
        :param newLastName: the new last name
        :return:
        '''
        self.__lastName = newLastName

    def setPassNumber(self, newPassNumber):
        '''
        Sets passport number
        :param newPassNumber: the new passport number
        :return:
        '''
        self.__passNumber = newPassNumber

    def __repr__(self):
        return "(" + self.__firstName + " " + self.__lastName + ", " + str(self.__passNumber) + ")"
