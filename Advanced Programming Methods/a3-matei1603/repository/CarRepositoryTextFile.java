package repository;
import java.util.HashMap;
import java.util.Map;

import domain.Identifiable;
import domain.Car;

import java.io.*;


public class CarRepositoryTextFile extends FileRepository<Car, Integer> {
    public CarRepositoryTextFile(String filename) {
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
                    Car car = new Car(carId, stringArray[1].trim(), Integer.parseInt(stringArray[3].trim()),Integer.parseInt(stringArray[4].trim()));
                    data.put(carId, car); // Using carId as the key in the HashMap
                }
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    protected void writeToFile() {
        try(BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            for (Car c: getAll())
            {
                writer.write(c.getId() + "," +
                        c.getNameOfCar() + "," +
                        c.getFabricationYear() + "," +
                        c.getKm() + "\n ") ;

            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }


}