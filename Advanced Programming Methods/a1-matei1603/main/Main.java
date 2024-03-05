package main;

import UI.UI;
import domain.Car;

import service.Service;


public class Main {
    public static void main(String[] args) {
        Service service = new Service();

        Car car1 = new Car(1, "Opel Astra", 2003, 320000);

        Car car2 = new Car(2, "Golf 5", 2008, 150000);

        Car car3 = new Car(3, "Mercedes S", 2018, 20000);

        Car car4 = new Car(4, "BMW X6", 2023, 10000);

        Car car5 = new Car(5, "Dacia Logan", 2016, 35000);
        service.addCar(car1);
        service.addCar(car2);
        service.addCar(car3);
        service.addCar(car4);
        service.addCar(car5);

        UI UI = new UI(service);
        UI.run();

    }
}

