package tests;

import domain.Car;
import domain.CarRental;
import domain.Customer;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CarRentalTest {

    @Test
    public void testGetCar() {
        Car car = new Car(1, "Opel", 2001, 3000000);
        Customer customer = new Customer(1, "Pista Matei", 20);
        CarRental carRental = new CarRental(1, car, customer);
        assertEquals(car, carRental.getCar());
    }

    @Test
    public void testSetCar() {
        Car car = new Car(1, "Opel", 2001, 3000000);
        Customer customer = new Customer(1, "Pista Matei", 20);
        CarRental carRental = new CarRental(1, null, customer);
        carRental.setCar(car);
        assertEquals(car, carRental.getCar());
    }

    @Test
    public void testGetCustomer() {
        Car car = new Car(1, "Opel", 2001, 3000000);
        Customer customer = new Customer(1, "Pista Matei", 20);
        CarRental carRental = new CarRental(1, car, customer);
        assertEquals(customer, carRental.getCustomer());
    }

    @Test
    public void testSetCustomer() {
        Car car = new Car(1, "Opel", 2001, 3000000);
        Customer customer = new Customer(1, "Pista Matei", 20);
        CarRental carRental = new CarRental(1, car, null);
        carRental.setCustomer(customer);
        assertEquals(customer, carRental.getCustomer());
    }

    @Test
    public void testToString() {
        Car car = new Car(1, "Opel", 2001, 3000000);
        Customer customer = new Customer(1, "Pista Matei", 20);
        CarRental carRental = new CarRental(1, car, customer);
        assertEquals("Car - Opel Customer - Pista Matei", carRental.toString());
    }

    @Test
    public void testGetId() {
        Car car = new Car(1, "Opel", 2001, 3000000);
        Customer customer = new Customer(1, "Pista Matei", 20);
        CarRental carRental = new CarRental(123, car, customer);
        assertEquals(123, carRental.getId());
    }
}
