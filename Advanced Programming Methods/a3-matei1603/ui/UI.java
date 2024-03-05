package ui;

import service.Service;
import domain.Car;
import domain.Customer;
import domain.CarRental;
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
            System.out.println("2. Add CarRental");
            System.out.println("3. Update Car");
            System.out.println("4. Update CarRental");
            System.out.println("5. Remove Car");
            System.out.println("6. Remove CarRental");
            System.out.println("7. List All Cars");
            System.out.println("8. List All CarRentals");
            System.out.println("9. Exit");
            int choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    addCar();
                    break;
                case 2:
                    addCarRental();
                    break;
                case 3:
                    updateCar();
                    break;
                case 4:
                    updateCarRental();
                    break;
                case 5:
                    removeCar();
                    break;
                case 6:
                    removeCarRental();
                    break;
                case 7:
                    listAllCars();
                    break;
                case 8:
                    listAllCarRentals();
                    break;
                case 9:
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


    private void addCarRental() {
        System.out.println("Please enter rental details:");
        System.out.print("Car info - Name: ");
        String carName = scanner.nextLine();
        System.out.print("Car info - Fabrication Year: ");
        int fabricationYear = scanner.nextInt();
        System.out.print("Car info - Kilometers: ");
        int km = scanner.nextInt();
        scanner.nextLine();
        System.out.print("Customer info - Name: ");
        String customerName = scanner.nextLine();
        System.out.print("Customer info - Age: ");
        int age = scanner.nextInt();
        scanner.nextLine();
        System.out.print("ID: ");

        try {
            Integer ID= Integer.valueOf(scanner.nextLine());
            Car car = new Car(ID, carName, fabricationYear, km);
            Customer customer = new Customer(ID,customerName, age);
            service.addRental(ID,car, customer);

            System.out.println("The CarRental has been added successfully.");

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
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

    private void updateCarRental() {
        System.out.print("Please enter CarRentalID to update: ");
        String rentalId = scanner.nextLine().trim();
        CarRental rentalToUpdate = service.getRentalById(Integer.valueOf(rentalId));

        if (rentalToUpdate != null) {
            System.out.println("Please enter new details for the rental:");
            System.out.print("Car info - Name: ");
            String carName = scanner.nextLine();
            System.out.print("Car info - Fabrication Year: ");
            int fabricationYear = scanner.nextInt();
            System.out.print("Car info - Kilometers: ");
            int km = scanner.nextInt();
            scanner.nextLine();
            System.out.print("Customer info - Name: ");
            String customerName = scanner.nextLine();
            System.out.print("Customer info - Age: ");
            int age = scanner.nextInt();
            scanner.nextLine();

            try {
                rentalToUpdate.getCar().setNameOfCar(carName);
                rentalToUpdate.getCar().setFabricationYear(fabricationYear);
                rentalToUpdate.getCar().setKm(km);
                rentalToUpdate.getCustomer().setName(customerName);
                rentalToUpdate.getCustomer().setAge(age);
                service.updateRental(rentalToUpdate);

                System.out.println("The CarRental has been updated successfully.");

            } catch (Exception e) {
                System.out.println("Error: " + e.getMessage());
            }
        } else {
            System.out.println("The CarRental ID was not found.");
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


    private void removeCarRental() {
        System.out.print("Please enter RentalID to remove: ");
        String rentalId = scanner.nextLine();
        try {
            service.removeRental(Integer.valueOf(rentalId));
            System.out.println("The CarRental has been removed successfully.");
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

    private void listAllCarRentals() {
        System.out.println("List of Rentals:");
        for (CarRental rental : service.getAllRentals()) {
            System.out.println("RentalID: " + rental.getId() + " -- " + rental);
        }
    }
}

