package domain;


import java.io.Serializable;

public class CarRental implements Identifiable, Serializable {
    private int id;
    private Car car;
    private Customer customer;

    public CarRental(Integer id,Car car, Customer customer) {
        this.id = id;
        this.car = car;
        this.customer = customer;

    }

    @Override
    public int getId() {
        return id;
    }

    public Car getCar() {
        return car;
    }

    public void setCar(Car car) {
        this.car=car;

    }
    public Customer getCustomer()
    {
        return customer;
    }

    public void setCustomer(Customer customer)
    {
        this.customer = customer;
    }
    public String toString() {
        return "Car - " + car.getNameOfCar() + " Customer - " + customer.getName();
    }

}