package domain;


import java.io.Serializable;

public class Car implements Identifiable, Serializable {
    private int id;
    private String nameOfCar;
    private int km;
    private int fabricationYear;

    public Car(Integer id, String nameOfCar, int fabricationYear, int km) {
        this.id =id;
        this.nameOfCar = nameOfCar;
        this.fabricationYear = fabricationYear;
        this.km = km;
    }

    public String getNameOfCar()
    {

        return nameOfCar;
    }

    public int getFabricationYear()
    {
        return fabricationYear;
    }

    public int getKm()
    {
        return km;
    }

    public void setNameOfCar(String newNameOfCar)
    {
        this.nameOfCar = newNameOfCar;
    }

    public void setFabricationYear(int newFabricationYear)
    {
        this.fabricationYear = newFabricationYear;
    }

    public void setKm(int newKm)
    {
        this.km = newKm;
    }


    public String toString()
    {
        return "Car: " + nameOfCar + " - " + fabricationYear + ", car has " + km + " km .";
    }

    @Override
    public int getId()


    {
        return id;
    }
}

