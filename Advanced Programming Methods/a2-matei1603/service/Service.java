package service;
import domain.Car;
import domain.Customer;
import domain.CarRental;
import repository.MemoryRepository;


public class Service {
    private MemoryRepository<Car,Integer> carRepository;
    private MemoryRepository<CarRental, Integer> carRentalRepository;

    public Service()
    {
        carRepository = new MemoryRepository<>();
        carRentalRepository = new MemoryRepository<>();
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

}


