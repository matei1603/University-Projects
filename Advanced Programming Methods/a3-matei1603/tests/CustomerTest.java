package tests;

import domain.Customer;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CustomerTest {

    @Test
    public void testGetAge() {
        Customer customer = new Customer(1, "Pista Matei", 20);
        assertEquals(20, customer.getAge());
    }

    @Test
    public void testGetName() {
        Customer customer = new Customer(1, "Pista Matei", 20);
        assertEquals("Pista Matei", customer.getName());
    }

    @Test
    public void testSetAge() {
        Customer customer = new Customer(1, "Pista Matei", 20);
        customer.setAge(25);
        assertEquals(25, customer.getAge());
    }

    @Test
    public void testSetName() {
        Customer customer = new Customer(1, "Pista Matei", 20);
        customer.setName("Sabin Barboi");
        assertEquals("Sabin Barboi", customer.getName());
    }

    @Test
    public void testGetId() {
        Customer customer = new Customer(1, "Pista Matei", 20);
        assertEquals(1, customer.getId());
    }
}
