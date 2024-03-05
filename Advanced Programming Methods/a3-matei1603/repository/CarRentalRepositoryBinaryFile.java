package repository;

import domain.Car;
import domain.CarRental;
import repository.MemoryRepository;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class CarRentalRepositoryBinaryFile extends FileRepository<CarRental, Integer> {
    public CarRentalRepositoryBinaryFile(String fileName) {
        super(fileName);
    }

    @Override
    public void readFromFile() {

        File file = new File(fileName);
        if (! file.exists())
        {
            try {
                Map<Integer, Car> emptyMap = new HashMap<>();
                ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(fileName));
                oos.writeObject(emptyMap);
            } catch (IOException e) {
                throw new Error("Could not create new empty binary file!");
            }
        }

        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(fileName)))
        {
            data = (Map<Integer, CarRental>) ois.readObject();
        } catch (IOException | ClassNotFoundException e) {
            throw new Error("Could not read binary file!");
        }
    }
    @Override
    public void writeToFile()
    {
        try {
            ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(fileName));
            oos.writeObject(data);
            oos.close();
        } catch (IOException e) {
            throw new Error("Could not write to binary file!");
        }
    }
}