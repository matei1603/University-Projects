import Plane
import Passenger
import Airport

def dataExamples():
    a = Airport()
    a.add(Plane(2,"WizzAir", 4, "Dubai", [Passenger("Matei", "Pista", 1234), Passenger("Lucian", "Bote", 2345), Passenger("Catalin", "Morosanu", 1224)]))
    print(a)
    print()

    a.sortPassengersByLastName(0)
    print(a.getAllPlanes())
    print()

    a.add(Plane(2,"WizzAir", 2,"Suceava", [Passenger("Marin", "Barbu", 2364), Passenger("Maria", "Garoafa", 5678)]))
    a.sortPlanesByNumberOfPassengers()
    print(a.getAllPlanes())
    print()

    a.sortByNumberOfPassengersFirstName("Mat")
    print(a.getAllPlanes())
    print()

    a.sortPlanesAccordingToConcatenation()
    print(a.getAllPlanes())
    print()

    print(a.identifyByPassengerFirst3())
    print()

    print(a.identifyByNameContainingString(1,"Mat"))
    print()

    print(a.identifyPlaneByPassengerName("Matei Pista"))
    print()

    a.add(Plane(3,"Ryanair", 3, "Viena", [Passenger("Maria", "Ursulean", 2364)]))
    print(a.getAllPlanes())
    print()

    print(a.identifyPlaneByPassengerName("Maria Ursulean"))
    print()

dataExamples()