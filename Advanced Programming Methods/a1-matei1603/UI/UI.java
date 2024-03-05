package UI;

import service.Service;
import domain.Car;
import domain.Customer;

import java.util.Scanner;


public class UI {
    private Service service;
    private Scanner scanner;

    public UI(Service service) {
        this.service = service;
        this.scanner = new Scanner(System.in);
    }

    public void run() {
        boolean exit = false;
        while (!exit) {
            System.out.println("Choose a number:");
            System.out.println("1. Add Car");
            System.out.println("2. Update Car");
            System.out.println("3. Remove Car");
            System.out.println("4. List All Cars");
            System.out.println("5. Exit");
            int choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    addCar();
                    break;

                case 2:
                    updateCar();
                    break;

                case 3:
                    removeCar();
                    break;

                case 4:
                    listAllCars();
                    break;

                case 5:
                    exit = true;
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
        }
    }

    private void addCar() {
        System.out.println("Please enter car details:");
        System.out.print("ID: ");
        Integer ID= Integer.valueOf(scanner.nextLine());
        System.out.print("Name: ");
        String name = scanner.nextLine();
        System.out.print("Fabrication Year: ");
        int fabricationYear = scanner.nextInt();
        System.out.print("Km: ");
        int km = scanner.nextInt();
        scanner.nextLine();




        Car car = new Car(ID, name, fabricationYear, km);
        service.addCar(car);
        System.out.println("The car has been added successfully.");
    }




    private void updateCar() {
        System.out.print("Please enter CarID to update: ");
        String carId = scanner.nextLine().trim();
        Car carToUpdate = service.getCarById(Integer.valueOf(carId));

        if (carToUpdate != null) {
            System.out.println("Please enter new details for the car:");
            System.out.print("Car info - Name: ");
            String name = scanner.nextLine();
            System.out.print("Car info - Fabrication Year: ");
            int fabricationYear = scanner.nextInt();
            System.out.print("Car info - Km: ");
            int km = scanner.nextInt();
            scanner.nextLine();

            carToUpdate.setNameOfCar(name);
            carToUpdate.setFabricationYear(fabricationYear);
            carToUpdate.setKm(km);

            service.updateCar(carToUpdate);
            System.out.println("The car has been updated successfully.");
        } else {
            System.out.println("Specified ID not found.");
        }
    }


    private void removeCar() {
        System.out.print("Please enter CarID to remove: ");
        String carId = scanner.nextLine().trim();
        try {
            service.removeCar(Integer.valueOf(carId));
            System.out.println("The car has been removed successfully.");
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }



    private void listAllCars() {
        System.out.println("List of Cars:");
        for (Car car : service.getAllCars()) {
            System.out.println("CarID: " + car.getId() + "  --  " + car);
        }
    }

}

