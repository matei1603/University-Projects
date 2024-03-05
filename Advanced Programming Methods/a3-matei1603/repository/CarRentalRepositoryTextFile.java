package repository;
import java.util.HashMap;
import java.util.Map;
import domain.Customer;
import repository.MemoryRepository;

import domain.CarRental;
import domain.Identifiable;
import domain.Car;

import java.io.*;




public class CarRentalRepositoryTextFile extends FileRepository<CarRental, Integer> {
    public CarRentalRepositoryTextFile(String filename) {
        super(filename);
    }

    @Override
    protected void readFromFile() {
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] stringArray = line.split(",");
                if (stringArray.length != 5) {
                    continue;
                } else {
                    int carId = Integer.parseInt(stringArray[0].trim());
                    Car car = new Car(carId, stringArray[1].trim(), Integer.parseInt(stringArray[2].trim()),Integer.parseInt(stringArray[3].trim()));
                    int customerId = Integer.parseInt(stringArray[4].trim());
                    Customer customer = new Customer(customerId, stringArray[5].trim(), Integer.parseInt(stringArray[6].trim()));
                    CarRental carRental = new CarRental(carId, car, customer);
                    super.add(carRental);
                }
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    protected void writeToFile() {
        try(BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            for (CarRental carRental: getAll())
            {
                writer.write(carRental.getId() + "," +
                        carRental.getCar() + "," +
                        carRental.getCustomer() + "\n");


            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }


}