from unittest import TestCase
import Plane
import Passenger

class TestPlane(TestCase):
    def setUp(self):
        self.__p = Plane(2, "WizzAir", 3, "London", [Passenger("Marin", "Popescu", 12625),
                                                    Passenger("Maria", "Ursulean", 13436)])

    def testInit(self):
        self.assertEqual(str(self.__p), "(2, Ryanair, 1, Dublin, [(Matei Pista, 34562), (Marius Borta, 23321)])")

    def testGetters(self):
        self.assertEqual(self.__p.getNumber(), 1)
        self.assertEqual(self.__p.getAirline(), "Ryanair")
        self.assertEqual(self.__p.getNumberOfSeats(), 3)
        self.assertEqual(str(self.__p.getListOfPassengers()), "[(Marius Borta, 23321), (Matei Pista, 12563)]")

    def testSetters(self):
        self.assertRaises(ValueError, self.__p.setNumber, 'x')
        self.__p.setAirline("Ryanair")
        self.assertEqual(self.__p.getAirline(), "Ryanair")
        self.assertRaises(ValueError, self.__p.setNumberOfSeats, 'x')

    def testAddPassenger(self):
        self.__p.addPassenger(Passenger("Blake", "Lively", 34567))
        self.assertEqual(str(self.__p.getListOfPassengers()), "[(Matei Pista, 12345), (Marius Borta, 23456), (Maria Ursulean, 34567)]")

    def testUpdatePatientAtIndex(self):
        self.assertRaises(ValueError, self.__p.updatePassengerAtIndex, 5, "Maria", "Ursulean", 45678)
        self.__p.updatePassengerAtIndex(1, "Maria", "Ursulean", 45678)
        self.assertEqual(str(self.__p.getListOfPassengers()), "[(Matei Pista, 12245), (Marius Borta, 46378)]")
        self.assertRaises(ValueError, self.__p.updatePassengerAtIndex, 1, "Maria", "Ursulean", 'x')

    def testDeleteAtIndex(self):
        self.assertRaises(ValueError, self.__p.deleteAtIndex, 6)
        self.__p.deleteAtIndex(1)
        self.assertEqual(str(self.__p.getListOfPassengers()), "[(Matei Pista, 12345)]")
