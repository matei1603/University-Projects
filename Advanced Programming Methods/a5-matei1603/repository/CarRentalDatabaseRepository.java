package repository;

import domain.Car;
import domain.CarRental;
import domain.Customer;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class CarRentalDatabaseRepository extends DBRepository<CarRental,Integer>{


    public CarRentalDatabaseRepository(String tablename)
    {
        super(tablename);
        getData();
    }

    @Override
    public void getData() {
        try
        {
            openConnection();
            String selectString = "SELECT * FROM " + tableName + ";";
            try (PreparedStatement ps = conn.prepareStatement(selectString))
            {
                ResultSet resultSet = ps.executeQuery();
                while (resultSet.next())
                {
                    int id = resultSet.getInt("id");
                    int idcar=resultSet.getInt(("carid"));
                    String nameofcar = resultSet.getString("nameofcar");
                    int fabricationYear = resultSet.getInt("FabricationYear");
                    int km = resultSet.getInt("km");
                    int idc=resultSet.getInt(("customerid"));
                    String name=resultSet.getString("customername");
                    int age=resultSet.getInt("age");
                    CarRental carRental = new CarRental(id,new Car(idcar,nameofcar,fabricationYear,km),new Customer(idc,name,age));
                    super.add(carRental);
                }
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        finally {
            try {
                closeConnection();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
    }

    @Override
    public void add(CarRental carRental)
    {
        try
        {
            openConnection();
            String insertString = "INSERT INTO " + tableName + " VALUES(?, ?, ?, ?, ?, ?, ?, ?);";
            try (PreparedStatement ps = conn.prepareStatement(insertString))
            {
                ps.setInt(1,carRental.getId());
                ps.setInt(2, carRental.getCar().getId());
                ps.setString(3, carRental.getCar().getNameOfCar());
                ps.setInt(4, carRental.getCar().getFabricationYear());
                ps.setInt(5, carRental.getCar().getKm());
                ps.setInt(6, carRental.getCustomer().getId());
                ps.setString(7, carRental.getCustomer().getName());
                ps.setInt(8, carRental.getCustomer().getAge());




                super.add(carRental);
                ps.executeUpdate();

            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        finally {

            try {
                closeConnection();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
    }

    @Override
    public void remove(Integer id)
    {

        try
        {
            openConnection();
            String deleteString = "DELETE FROM " + tableName + " WHERE Id = ?";
            try (PreparedStatement ps = conn.prepareStatement(deleteString))
            {
                ps.setInt(1,id);
                ps.executeUpdate();
                super.remove(id);
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        finally {

            try {
                closeConnection();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
    }

    @Override
    public void update(CarRental carRental)
    {
        remove(carRental.getId());
        add(carRental);
    }
}
