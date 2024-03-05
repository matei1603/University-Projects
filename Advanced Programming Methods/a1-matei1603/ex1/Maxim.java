package ex1;


public class Maxim {
    public static void main(String[] args)
    {
        // Checking if length of args array is greater than 0
        if (args.length > 0) {
            double mmaxim = Double.parseDouble(args[0]);

            for (String val : args) {
                if (Double.parseDouble(val) > mmaxim){
                    mmaxim = Double.parseDouble(val);
                }
            }
            System.out.println(mmaxim);
        }
        else {
            System.out.println("there are no args");
        }
}
}
