class AirportController:

    def __init__(self, arepo):
        self.__arepo = arepo

    def getAllPlanes(self):
        return self.__arepo.getAllPlanes()

    def deletePlaneAtIndex(self, index):
        return self.__arepo.deletePlaneAtIndex(index)

    def addPlane(self, plane):
        self.__arepo.add(plane)

    def sortPassengersByLastName(self,index):
        return self.__arepo.sortPassengersByLastName(index)

    def sortPlanesByNumberOfPassengers(self):
        return self.__arepo.sortPlanesByNumberOfPassengers()

    def sortByNumberOfPassengersFirstName(self, firstName):
        return self.__arepo.sortByNumberOfPassengersFirstName(firstName)

    def sortPlanesAccordingToConcatenation(self):
        return self.__arepo.sortPlanesAccordingToConcatenation()

    def identifyByPassengerFirst3(self):
        return self.__arepo.identifyByPassengerFirst3()

    def identifyByNameContainingString(self, index, containingString):
        return self.__arepo.identifyByNameContainingString(index, containingString)

    def identifyPlaneByPassengerName(self, name):
        return self.__arepo.identifyPlaneByPassengerName(name)
