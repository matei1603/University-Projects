package service;
import domain.Car;
import domain.Customer;
import Repository.MemoryRepository;


public class Service {
    private MemoryRepository<Car,Integer> carRepository;

    public Service()
    {
        carRepository = new MemoryRepository<>();

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


}


