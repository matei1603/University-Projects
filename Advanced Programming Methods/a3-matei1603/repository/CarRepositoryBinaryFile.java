package repository;

import domain.Car;
import repository.MemoryRepository;

import java.io.*;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class CarRepositoryBinaryFile extends FileRepository<Car, Integer> {
    public CarRepositoryBinaryFile(String fileName) {
        super(fileName);
        readFromFile();
    }

    @Override
    public void readFromFile() {

        File file = new File(fileName);
        if (! file.exists())
        {
            try {
                HashMap<Integer, Car> emptyMap = new HashMap<>();
                ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(fileName));
                oos.writeObject(emptyMap);
            } catch (IOException e) {
                throw new Error("Could not create new empty binary file!");
            }
        }

        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(fileName)))
        {
            data = (HashMap<Integer, Car>) ois.readObject();
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