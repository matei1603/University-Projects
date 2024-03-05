package repository;

import domain.Car;
import domain.CarRental;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class CarDatabaseRepository extends DBRepository<Car,Integer>{


    public CarDatabaseRepository(String tablename)
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
                    String nameofcar = resultSet.getString("nameofcar");
                    int fabricationYear = resultSet.getInt("FabricationYear");
                    int km = resultSet.getInt("km");
                    Car car = new Car(id,nameofcar,fabricationYear,km);
                    super.add(car);
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
    public void add(Car car)
    {
        try
        {
            openConnection();
            String insertString = "INSERT INTO " + tableName + " VALUES(?, ?, ?, ?);";
            try (PreparedStatement ps = conn.prepareStatement(insertString))
            {
                ps.setInt(1,car.getId());
                ps.setString(2, car.getNameOfCar());
                ps.setInt(3, car.getFabricationYear());
                ps.setInt(4, car.getKm());
                super.add(car);
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
    public void update(Car car)
    {
        remove(car.getId());
        add(car);

    }
}
