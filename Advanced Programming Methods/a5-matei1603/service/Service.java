package service;
import domain.Car;
import domain.Customer;
import domain.CarRental;
import repository.*;

import java.io.FileReader;
import java.util.List;
import java.util.Properties;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;


public class Service {
    private MemoryRepository<Car,Integer> carRepository;
    private MemoryRepository<CarRental, Integer> carRentalRepository;

    private void service() {
        try (FileReader fr = new FileReader("settings.properties")) {
            Properties properties = new Properties();
            properties.load(fr);
            String RepositoryType = properties.getProperty("Repository");
            String cardata = properties.getProperty("Car");
            String carrentaldata = properties.getProperty("CarRental");
            switch (RepositoryType) {
                case "Memory":
                    carRepository = new CarRepository();
                    carRentalRepository = new CarRentalRepository();
                    break;

                case "DataBase":
                    carRepository = new CarDatabaseRepository(cardata);
                    carRentalRepository = new CarRentalDatabaseRepository(carrentaldata);
                    break;
                default:
                    System.out.println("Invalid vehicleRepoType: " + RepositoryType);
                    break;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    public Service()
    {
        service();
    }

    public void addCar(Car car)

    {
        carRepository.add(car);
    }

    public Car getCarById(Integer id)

    {
        return carRepository.findbyid(id);
    }

    public void updateCar(Car car)

    {
        carRepository.update(car);
    }

    public void removeCar(Integer id)
    {

        carRepository.remove(id);

    }

    public Iterable<Car> getAllCars()

    {
        return carRepository.getAll();
    }


    public void addRental(Integer id,Car car, Customer customer)
    {
        CarRental rental = new CarRental(id,car, customer);
        carRentalRepository.add(rental);
    }


    public CarRental getRentalById(Integer id)

    {
        return carRentalRepository.findbyid(id);
    }

    public void updateRental(CarRental rental)

    {
        carRentalRepository.update(rental);
    }

    public void removeRental(Integer id)
    {
        carRentalRepository.remove(id);
    }

    public Iterable<CarRental> getAllRentals()
    {
        return carRentalRepository.getAll();
    }

    public List<Car> getCarsKmGreater(float Km)
    {
        return StreamSupport.stream(carRepository.getAll().spliterator(), false)
                .filter(car -> Km <= car.getKm())
                .collect(Collectors.toList());
    }
    public List<Car> getAllOlderCars(float Year)
    {
        return StreamSupport.stream(carRepository.getAll().spliterator(), false)
                .filter(car -> Year >= car.getFabricationYear() )
                .collect(Collectors.toList());
    }
    public List <Car> getCarsWithName(String Name){
        return StreamSupport.stream(carRepository.getAll().spliterator(), false)
                .filter(car -> car.getNameOfCar().contains(Name))
                .collect(Collectors.toList());
    }
    public List<Car> getAllCarsByIdRange(float minId, float maxId)
    {
        return StreamSupport.stream(carRepository.getAll().spliterator(), false)
                .filter(car -> minId <= car.getId() && car.getId() <= maxId)
                .collect(Collectors.toList());
    }
    public List<Car> getAllCarsNewerWithMileageLow(float Year, float Km)
    {
        return StreamSupport.stream(carRepository.getAll().spliterator(), false)
                .filter(car -> Year <= car.getFabricationYear() && car.getKm() <= Km)
                .collect(Collectors.toList());
    }
}


