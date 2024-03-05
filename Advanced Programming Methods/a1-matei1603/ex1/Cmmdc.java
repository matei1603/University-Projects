package ex1;

public class Cmmdc {
    // returns gcd between a and b
    static int gcd(int a, int b)
    {
        if (b == 0)
            return a;
        return gcd(b, a%b);
    }

    // returns gcd in array
    static int findGCD(int arr[], int n)
    {
        int sol = arr[0];
        for (int element: arr)
        {
            sol = gcd(sol, element);
        }

        return sol;
    }



    public static void main(String[] args)
    {

        if (args.length > 0) {

            int len = args.length;
            int [] arr = new int [len];
            for (int i = 0; i < len; i++) {
                arr[i] = Integer.parseInt(args[i]);
            }
            System.out.println(findGCD(arr, len));
        }
        else {
            System.out.println("there are no args");
        }
 }

}
