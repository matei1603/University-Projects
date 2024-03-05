package utils;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class Utils {
    private Properties properties;

    public Utils(String filePath) {
        this.properties = new Properties();
        try {
            FileInputStream input = new FileInputStream(filePath);
            properties.load(input);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String getRepositoryType() {
        return properties.getProperty("Repository");
    }

    public String getCarRepositoryFile() {
        return properties.getProperty("Car");
    }

    public String getCarRentalRepositoryFile() {
        return properties.getProperty("CarRental");
    }
}

