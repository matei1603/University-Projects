package gui;
import domain.Car;
import domain.CarRental;
import domain.Customer;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;
import service.Service;

import java.util.ArrayList;
import java.util.List;

public class Controller {
    private Service service;

    public Controller(Service service) {

        this.service = service;
    }
    @FXML
    private Button addcar;

    @FXML
    private Button addrental;

    @FXML
    private TextField carid1;

    @FXML
    private TextField carid2;

    @FXML
    private TextField carname1;

    @FXML
    private TextField carname2;

    @FXML
    private Button carolder;

    @FXML
    private TextField customerage;

    @FXML
    private TextField customerid;

    @FXML
    private TextField customername;

    @FXML
    private TextField fabricationyear1;

    @FXML
    private TextField fabricationyear2;

    @FXML
    private Button filname;

    @FXML
    private ListView<Car> filtredcars;

    @FXML
    private Button idrange;

    @FXML
    private TextField km1;

    @FXML
    private TextField km2;

    @FXML
    private Button kmgreater;

    @FXML
    private Button newmillow;

    @FXML
    private Button removecar;

    @FXML
    private Button removerental;

    @FXML
    private TextField rentalid;

    @FXML
    private Button updatecar;

    @FXML
    private Button updaterental;

    @FXML
    private ListView<CarRental> viewcarrentals;

    @FXML
    private ListView<Car> viewcars;

    void populateList() {
        Iterable<Car> carIterable = service.getAllCars();
        List<Car> carList = new ArrayList<>();
        carIterable.forEach(carList::add);
        ObservableList<Car> cars = FXCollections.observableArrayList(carList);
        viewcars.setItems(cars);

        Iterable<CarRental> rentalIterable = service.getAllRentals();
        List<CarRental> rentalList = new ArrayList<>();
        rentalIterable.forEach(rentalList::add);
        ObservableList<CarRental> rentals = FXCollections.observableArrayList(rentalList);
        viewcarrentals.setItems(rentals);
    }


    public void initialize() {
        populateList();
    }


    @FXML
    void addCarClick() {
        try {
            Integer id = Integer.parseInt(carid1.getText());
            String name = carname1.getText();
            int fabricationyear = Integer.parseInt(fabricationyear1.getText());
            int km = Integer.parseInt(km1.getText());
            Car car = new Car(id, name,fabricationyear, km);
            service.addCar(car);
            populateList();
        } catch (Exception e) {
            System.out.println(e.getMessage());
            Alert alert = new Alert(Alert.AlertType.ERROR, e.getMessage());
            alert.setTitle("Something went wrong");
            alert.showAndWait();
        }
    }
    @FXML
    void addRentalClick() {
        try {
            Integer id = Integer.parseInt(carid2.getText());
            String carname = carname2.getText();
            Integer fabricationyear = Integer.parseInt(fabricationyear2.getAccessibleText());
            Integer km = Integer.parseInt(km2.getText());
            Integer idCustomer = Integer.parseInt(customerid.getText());
            String name = customername.getText();
            Integer age = Integer.parseInt(customerage.getText());
            Integer rid = Integer.parseInt(rentalid.getText());
            Car car= new Car(id,carname,fabricationyear,km);
            Customer customer=new Customer(idCustomer,name,age);
            service.addRental(rid,car,customer);
            populateList();
        } catch (Exception e) {
            System.out.println(e.getMessage());
            Alert alert = new Alert(Alert.AlertType.ERROR, e.getMessage());
            alert.setTitle("Something went wrong");
            alert.showAndWait();
        }

    }
    @FXML
    void removeCarClick() {
        try {
            Integer id = Integer.parseInt(carid1.getText());
            service.removeCar(id);
            populateList();
        } catch (Exception e) {
            System.out.println(e.getMessage());
            Alert alert = new Alert(Alert.AlertType.ERROR, e.getMessage());
            alert.setTitle("Something went wrong");
            alert.showAndWait();
        }
    }
    @FXML
    void removeRentalClick() {
        try {
            Integer id = Integer.parseInt(rentalid.getText());
            service.removeRental(id);
            populateList();
        } catch (Exception e) {
            System.out.println(e.getMessage());
            Alert alert = new Alert(Alert.AlertType.ERROR, e.getMessage());
            alert.setTitle("Something went wrong");
            alert.showAndWait();
        }
    }
    @FXML
    void updateCarClick() {
        try {
            Integer id = Integer.parseInt(carid1.getText());
            String name = carname1.getText();
            Integer fabricationyear = Integer.parseInt(fabricationyear1.getText());
            Integer km = Integer.parseInt(km1.getText());
            Car car= new Car(id, name, fabricationyear, km);
            service.updateCar(car);
            populateList();
        } catch (Exception e) {
            System.out.println(e.getMessage());
            Alert alert = new Alert(Alert.AlertType.ERROR, e.getMessage());
            alert.setTitle("Something went wrong");
            alert.showAndWait();
        }
    }
    @FXML
    void updateCarRentalClick() {
        try {
            Integer id = Integer.parseInt(carid2.getText());
            String name = carname2.getText();
            Integer fabricationyear = Integer.parseInt(fabricationyear2.getText());
            Integer km = Integer.parseInt(km2.getText());
            Integer idCustomer = Integer.parseInt(customerid.getText());
            String csname = customername.getText();
            Integer age = Integer.parseInt(customerage.getText());
            Integer rid = Integer.parseInt(rentalid.getText());
            Customer customer=new Customer(idCustomer,csname,age);
            Car car= new Car(id, name, fabricationyear, km);
            CarRental carRental= new CarRental(rid, car, customer);
            service.updateRental(carRental);
            populateList();
        } catch (Exception e) {
            System.out.println(e.getMessage());
            Alert alert = new Alert(Alert.AlertType.ERROR, e.getMessage());
            alert.setTitle("Something went wrong");
            alert.showAndWait();
        }
    }
    @FXML
    void getKmGreaterClick() {
        try {
            Integer km = Integer.parseInt(km1.getText());
            ObservableList<Car> cars = FXCollections.observableArrayList(service.getCarsKmGreater(km));
            filtredcars.setItems(cars);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
    @FXML
    void getCarOlderClick() {
        try {
            Integer fabricationyear = Integer.parseInt(fabricationyear1.getText());
            ObservableList<Car> cars = FXCollections.observableArrayList(service.getAllOlderCars(fabricationyear));
            filtredcars.setItems(cars);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }
    @FXML
    void getFiltredNameClick() {
        try {
            String name = carname1.getText();
            ObservableList<Car> cars = FXCollections.observableArrayList(service.getCarsWithName(name));
            filtredcars.setItems(cars);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
    @FXML
    void getCarinIdRangeClick() {
        try {
            Integer idcar = Integer.parseInt(carid1.getText());
            Integer idcar1 = Integer.parseInt(carid2.getText());
            ObservableList<Car> cars = FXCollections.observableArrayList(service.getAllCarsByIdRange(idcar,idcar1));
            filtredcars.setItems(cars);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }
    @FXML
    void getCarNewerwithMilLowerClick() {
        try {
            Integer fabricatinYear = Integer.parseInt(fabricationyear1.getText());
            Integer km = Integer.parseInt(km1.getText());
            ObservableList<Car> cars = FXCollections.observableArrayList(service.getAllCarsNewerWithMileageLow(fabricatinYear,km));
            filtredcars.setItems(cars);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }

}