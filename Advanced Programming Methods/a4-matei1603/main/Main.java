package main;

import ui.UI;
import domain.Car;
import domain.Customer;
import service.Service;


public class Main {
    public static void main(String[] args) {
        Service service = new Service();


/*        Car car1 = new Car(1, "Opel Astra", 2003, 320000);

        Car car2 = new Car(2, "Golf 5", 2008, 150000);

        Car car3 = new Car(3, "Mercedes S", 2018, 20000);

        Car car4 = new Car(4, "BMW X6", 2023, 10000);

        Car car5 = new Car(5, "Dacia Logan", 2016, 35000);
        service.addCar(car1);
        service.addCar(car2);
        service.addCar(car3);
        service.addCar(car4);
        service.addCar(car5);

        Customer customer1 = new Customer(100,"Vlad", 22);
        Customer customer2 = new Customer(101,"Andrei ", 21);
        Customer customer3 = new Customer(102,"Gabriel", 36);
        Customer customer4 = new Customer(103,"Daniel", 45);
        Customer customer5 = new Customer(104,"Marcel", 68);




        service.addRental(50,car1, customer1);
        service.addRental(51,car2, customer2);
        service.addRental(52,car3, customer3);
        service.addRental(53,car4, customer4);
        service.addRental(54,car5, customer5);*/



        UI UI = new UI(service);
        UI.run();

    }
}

