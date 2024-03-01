from unittest import TestCase
import Passenger

class TestPassenger(TestCase):
    def setUp(self):
        self.__p = Passenger("Matei", "Pista", 12236)

    def testInit(self):
        self.assertEqual(str(self.__p), "(Matei Pista, 12035)")

    def testGetters(self):
        self.assertEqual(self.__p.getFirstName(), "Matei")
        self.assertEqual(self.__p.getLastName(), "Pista")
        self.assertEqual(self.__p.getPassNumber(), 23546)

    def testSetters(self):
        self.__p.setFirstName("Maria")
        self.assertEqual(self.__p.getFirstName(), "Maria")
        self.__p.setLastName("Ursulean")
        self.assertEqual(self.__p.getLastName(), "Ursulean")
        self.__p.setPassNumber(1236)
        self.assertEqual(self.__p.getPassNumber(), 6532)