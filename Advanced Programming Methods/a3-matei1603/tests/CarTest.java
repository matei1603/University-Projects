package tests;

import domain.Car;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class CarTest {

    @Test
    public void testGetNameOfCar() {
        Car car = new Car(1, "Opel", 2001, 300000);
        assertEquals("Opel", car.getNameOfCar());
    }
    @Test
    public void testGetFabricationYear() {
        Car car = new Car(1, "Opel", 2001, 300000);
        assertEquals(2001, car.getFabricationYear());
    }
    @Test
    public void testGetKm() {
        Car car = new Car(1, "Opel", 2001, 300000);
        assertEquals(300000, car.getKm());
    }
    @Test
    public void testSetNameOfCar() {
        Car car = new Car(1, "Opel", 2001, 300000);
        car.setNameOfCar("Opel");
        assertEquals("Opel", car.getNameOfCar());
    }
    @Test
    public void testSetFabricationYear() {
        Car car = new Car(1, "Opel", 2001, 300000);
        car.setFabricationYear(2001);
        assertEquals(2001, car.getFabricationYear());
    }
    @Test
    public void testSetKm() {
        Car car = new Car(1, "Opel", 2001, 300000);
        car.setKm(10);
        assertEquals(10, car.getKm());
    }
    @Test
    public void testToString() {
        Car car = new Car(1, "Opel", 2001, 300000);
        assertEquals("Car: Opel - 2001, car has 300000 km .", car.toString());
    }
    @Test
    public void testGetId() {
        Car car = new Car(1, "Opel", 2001, 300000);
        assertEquals(1, car.getId());
    }
}
