from unittest import TestCase
import Airport
import Plane
import Passenger

class TestAirport(TestCase):
    def setUp(self):
        self.__a = Airport()

    def testInit(self):
        self.assertEqual(str(self.__a), "[]")

    def testAdd(self):
        self.__a.add(Plane(1, "WizzAir", 3, "Suceava", [Passenger("Matei", "Pista", 12345),
                                             Passenger("Marin", "Barbu", 23456)]))
        self.assertEqual(str(self.__a), "[(1, Ryanair, 3, Suceava, [(Matei Pista, 12345), (Marin Barbu, 23456)])]")
        self.__a.add(Plane(2, "Tarom", 4, "Cluj", [Passenger("Eduard", "Alucai", 34567),
                                          Passenger("Maria", "Ursulean", 45678)]))
        self.assertEqual(str(self.__a), "[(1, Tarom, 3, Suceava, [(Matei Pista, 12345), (Marin Barbu, 23456)]), (2, Tarom, 4, Cluj, [(Eduard Alucai, 34567), (Maria Ursulean, 45678)])]")

    def testSortPassengersByLastName(self):
        self.__a.add(Plane(1, "WizzAir", 3, "Suceava", [Passenger("Matei", "Pista", 12345),
                                             Passenger("Marin", "Barbu", 23456)]))
        self.__a.sortPassengersByLastName(0)
        self.assertEqual(str(self.__a.getAllPlanes()), "[(1, WizzAir, 3, Suceava, [(Marin Barbu, 23456), (Matei Pista, 12345)])]")
        self.__a.add(Plane(2, "Wizzair", 4, "Cluj", [Passenger("Eduard", "Alucai", 34567),
                                          Passenger("Maria", "Ursulean", 45678)]))
        self.__a.sortPassengersByLastName(0)
        self.assertEqual(str(self.__a.getAllPlanes()), "[(1, WizzAir, 3,Suceava, [(Marin Barbu, 23456), (Matei Pista, 12345)]), (2, Tarom, 4, Cluj, [(Eduard Alucai, 34567), (Maria Ursulean, 45678)])]")

    def testSortPlanesByNumberOfPassengers(self):
        self.assertRaises(ValueError, self.__a.sortPlanesByNumberOfPassengers)
        self.__a.add(Plane(1, "WizzAir", 3, "Suceava", [Passenger("Matei", "Pista", 12345),
                                             Passenger("Marin", "Barbu", 23456), Passenger("Vlad", "Tibichi", 54321)]))
        self.__a.add(Plane(2, "Wizzair", 4, "Cluj", [Passenger("Eduard", "Alucai", 34567),
                                          Passenger("Maria", "Ursulean", 45678)]))
        self.__a.sortPlanesByNumberOfPassengers()
        self.assertEqual(str(self.__a.getAllPlanes()), "[(2, Tarom, 4, Cluj, [(Eduard Alucai, 34567), (Maria Ursulean, 45678)]), (1, WizzAir, 3, Suceava, [(Matei Pista, 12345), (Marin Barbu, 23456), (Vlad Tibichi, 54321)])]")

    def testSortByNumberOfPassengersFirstName(self):
        self.assertRaises(ValueError, self.__a.sortByNumberOfPassengersFirstName, "Dwa")
        self.__a.add(Plane(1, "WizzAir", 3, "Suceava", [Passenger("Matei", "Pista", 12345),
                                             Passenger("Marin", "Barbu", 23456)]))
        self.__a.add(Plane(2, "Wizzair", 4, "Cluj", [Passenger("Eduard", "Alucai", 34567),
                                          Passenger("Maria", "Ursulean", 45678)]))
        self.__a.sortByNumberOfPassengersFirstName("Mat")
        self.assertEqual(str(self.__a.getAllPlanes()), "[(2, Tarom, 4, Cluj, [(Eduard Alucai, 34567), (Maria Ursulean, 45678)]), (1, WizzAir, 3, Suceava, [(Matei Pista, 12345), (Marin Barbu, 23456)])]")

    def testSortPlanesAccordingToConcatenation(self):
        self.assertRaises(ValueError, self.__a.sortPlanesAccordingToConcatenation)
        self.__a.add(Plane(2, "Tarom", 4, "Cluj", [Passenger("Eduard", "Alucai", 34567),
                                          Passenger("Maria", "Ursulean", 45678)]))
        self.__a.add(Plane(1, "WizzAir", 3, "Suceava", [Passenger("Matei", "Pista", 12345),
                                             Passenger("Marin", "Barbu", 23456)]))
        self.__a.sortPlanesAccordingToConcatenation()
        self.assertEqual(str(self.__a.getAllPlanes()), "[(1, WizzAir, 3, Suceava, [(Matei Pista, 12345), (Marin Barbu, 23456)]), (2, Tarom, 4, Cluj, [(Eduard Alucai, 34567), (Maria Ursulean, 45678)])]")

    def testIdentifyByPassengerFirst3(self):
        self.assertRaises(ValueError, self.__a.identifyByPassengerFirst3)
        self.__a.add(Plane(1, "WizzAir", 3, "Suceava", [Passenger("Matei", "Pista", 12345), Passenger("Marin", "Barbu", 12356)]))
        self.__a.add(Plane(2, "Wizzair", 4, "Cluj", [Passenger("Eduard", "Alucai", 34567),
                                          Passenger("Maria", "Ursulean", 45678)]))
        self.assertEqual(str(self.__a.identifyByPassengerFirst3()), "[(1, WizzAir, 3, Suceava, [(Matei Pista, 12345), (Marin Barbu, 12356)])]")

    def testIdentifyByNameContainingString(self):
        self.assertRaises(ValueError, self.__a.identifyByNameContainingString, 0, "Mat")
        self.__a.add(Plane(1, "WizzAir", 3, "Suceava", [Passenger("Matei", "Pista", 12345), Passenger("Marin", "Barbu", 12356)]))
        self.__a.add(Plane(2, "Tarom", 4, "Cluj", [Passenger("Eduard", "Alucai", 34567),
                                          Passenger("Maria", "Ursulean", 45678)]))
        self.assertRaises(ValueError, self.__a.identifyByNameContainingString, 6, "Mat")
        self.assertEqual(str(self.__a.identifyByNameContainingString(0, "Mat")), "[(Matei Pista, 12345)]")

    def testIdentifyPlaneByPassengerName(self):
        self.assertRaises(ValueError, self.__a.identifyPlaneByPassengerName, "Matei Pista")
        self.__a.add(Plane(1, "WizzAir", 3, "Suceava", [Passenger("Matei", "Pista", 12345),
                                             Passenger("Marin", "Barbu", 23456)]))
        self.__a.add(Plane(2, "Tarom", 4, "Cluj", [Passenger("Eduard", "Alucai", 34567),
                                          Passenger("Maria", "Ursulean", 45678)]))
        self.assertEqual(str(self.__a.identifyPlaneByPassengerName("Eduard Alucai")), "[(2, Tarom, 4, Cluj, [(Eduard Alucai, 34567), (Maria Ursulean, 45678)])]")