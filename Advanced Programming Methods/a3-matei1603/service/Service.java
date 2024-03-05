package service;
import domain.Car;
import domain.Customer;
import domain.CarRental;
import repository.MemoryRepository;
import repository.CarRepositoryTextFile;
import repository.CarRentalRepositoryTextFile;
import repository.CarRepositoryBinaryFile;
import repository.CarRentalRepositoryBinaryFile;
import repository.FileRepository;


    public class Service {
        private FileRepository<Car, Integer> carRepository;
        private FileRepository<CarRental, Integer> carRentalRepository;

        public Service(String carFilePath, String carRentalFilePath, String repositoryType) {
            if (repositoryType.equalsIgnoreCase("binary")) {
                carRepository = new CarRepositoryBinaryFile(carFilePath);
                carRentalRepository = new CarRentalRepositoryBinaryFile(carRentalFilePath);
            } else {
                carRepository = new CarRepositoryTextFile(carFilePath);
                carRentalRepository = new CarRentalRepositoryTextFile(carRentalFilePath);
            }
        }


/*        public Service() {

        }*/

        public void addCar(Car car) {
            carRepository.add(car);
        }

        public Car getCarById(Integer id) {
            return carRepository.findbyid(id);
        }

        public void updateCar(Car car) {
            carRepository.update(car);
        }

        public void removeCar(Integer id) {

            carRepository.remove(id);

        }

        public Iterable<Car> getAllCars() {
            return carRepository.getAll();
        }


        public void addRental(Integer id, Car car, Customer customer) {
            CarRental rental = new CarRental(id, car, customer);
            carRentalRepository.add(rental);
        }


        public CarRental getRentalById(Integer id) {
            return carRentalRepository.findbyid(id);
        }

        public void updateRental(CarRental rental) {
            carRentalRepository.update(rental);
        }

        public void removeRental(Integer id) {
            carRentalRepository.remove(id);
        }

        public Iterable<CarRental> getAllRentals() {
            return carRentalRepository.getAll();
        }

    }



