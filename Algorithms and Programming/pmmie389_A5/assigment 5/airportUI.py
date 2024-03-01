import Passenger
import Plane

class AirportUI:

    def __init__(self, ctrl):
        self.__ctrl = ctrl

    def __repr__(self):
        return str(self.__ctrl)

    @staticmethod
    def printMenu():
        '''
        Menu
        :return:
        '''
        msg = "****************************** \n"
        msg += "\t Airport: \n"
        msg += "\t 1 - View plane list \n"
        msg += "\t 2 - Add plane \n"
        msg += "\t 3 - Sort the passengers in a plane by last name \n"
        msg += "\t 4 - Sort planes according to the number of passengers \n"
        msg += "\t 5 - Sort planes according to the number of passengers with the first name starting with a given substring \n"
        msg += "\t 6 - Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination \n"
        msg += "\t 7 - Identify planes that have passengers with passport numbers starting with the same 3 letters \n"
        msg += "\t 8 - Identify  passengers  from  a  given  plane  for  which  the  first  name  or  last  namecontain a string given as parameter \n"
        msg += "\t 9 - Identify plane/planes where there is a passenger with given name \n"
        msg += "\t ************************** \n"
        msg += "\t 0 - Exit"
        print(msg)

    @staticmethod
    def readPassenger():
        '''
        Reads pass.
        :return:
        '''
        firstName = input("Passenger's first name: ")
        lastName = input("Passenger's last name: ")
        passNumber = int(input("Passenger's passport number: "))
        return Passenger(firstName, lastName, passNumber)

    def readPlane(self):
        '''
        Reads plane
        :return:
        '''
        listOfPassengers = []
        number = int(input("Plane's number: "))
        airline = input("Plane's airline: ")
        numberOfSeats = int(input("Plane's number of seats: "))
        destination = input("Plane's destination: ")
        passengers = int(input("Plane's number of passengers: "))
        for i in range(passengers):
            listOfPassengers.append(AirportUI.readPassenger())
        return Plane(number, airline, numberOfSeats,destination, listOfPassengers)

    def printPlaneList(self):
        '''
        Prints the list
        :return:
        '''
        print("Plane's list is: ")
        for elem in self.__ctrl.getAllPlanes():
            print(elem)

    def start(self):
        '''
        Start
        :return:
        '''
        while True:
            try:
                AirportUI.printMenu()
                option = int(input("Enter the option: "))
                if option == 1:
                    self.printPlaneList()
                elif option == 2:
                    plane = self.readPlane()
                    self.__ctrl.addPlane(plane)
                elif option == 3:
                    index = int(input("Enter an index: "))
                    self.__ctrl.sortPassengersByLastName(index)
                elif option == 4:
                    self.__ctrl.sortPlanesByNumberOfPassengers()
                elif option == 5:
                    firstName = input("Enter the first name: ")
                    self.__ctrl.sortByNumberOfPassengersFirstName(firstName)
                elif option == 6:
                    self.__ctrl.sortPlanesAccordingToConcatenation()
                elif option == 7:
                    print(self.__ctrl.identifyByPassengerFirst3())
                elif option == 8:
                    index = int(input("Enter the index: "))
                    containingString = input("Enter the containing string: ")
                    print(self.__ctrl.identifyByNameContainingString(index,containingString))
                elif option == 9:
                    name = input("Enter the full name: ")
                    print(self.__ctrl.identifyPlaneByPassengerName(name))
                elif option == 10:
                    k = input("Enter k's value: ")
                    print(self.__ctrl.form_groups_by_lastname(k))
                elif option == 11:
                    k = input("Enter k's value: ")
                    print(self.__ctrl.form_groups_by_destination_and_airline(k))
                elif option == 0:
                    print("Goodbye!")
                    break
                else:
                    print("The option is invalid!")
            except ValueError:
                print("Invalid!")