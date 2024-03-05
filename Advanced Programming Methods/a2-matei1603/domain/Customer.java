package domain;

public class Customer implements Identifiable{
    Integer id;
    String name;
    int age;
    public Customer(Integer id,String name, int age){

        this.id = id;
        this.name = name;
        this.age = age;
    }
//getters
    public int getAge(){
        return age;
    }
    public String getName(){
        return name;
    }
//setters
    public void setAge(int Age){
        this.age=Age;
    }
    public void setName(String Name){
        this.name=Name;
    }
    @Override
    public int getId()
    {
        return id;

    }
}
