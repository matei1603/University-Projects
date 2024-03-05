package tests;

import domain.Car;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class MemoryTest {

    @Test
    public void testCarConstruction() {
        int id = 1;
        String nameOfCar = "Opel";
        int fabricationYear = 2001;
        int km = 3000000;

        Car opelCar = new Car(id, nameOfCar, fabricationYear, km);

        Assertions.assertEquals(id, opelCar.getId());
        Assertions.assertEquals(nameOfCar, opelCar.getNameOfCar());
        Assertions.assertEquals(fabricationYear, opelCar.getFabricationYear());
        Assertions.assertEquals(km, opelCar.getKm());
    }

    @Test
    public void testCarModification() {
        int id = 2;
        String nameOfCar = "Range Rover";
        int fabricationYear = 2016;
        int km = 150000;

        Car rangeRoverCar = new Car(id, nameOfCar, fabricationYear, km);

        String newName = "BMW";
        int newFabricationYear = 2022;
        int newKm = 20000;

        rangeRoverCar.setNameOfCar(newName);
        rangeRoverCar.setFabricationYear(newFabricationYear);
        rangeRoverCar.setKm(newKm);

        Assertions.assertEquals(newName, rangeRoverCar.getNameOfCar());
        Assertions.assertEquals(newFabricationYear, rangeRoverCar.getFabricationYear());
        Assertions.assertEquals(newKm, rangeRoverCar.getKm());
    }

}
