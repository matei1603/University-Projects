package ex1;

public class Prime
{
    public static boolean isPrime(int x)
    {
        if(x<2)
            return false;
        for(int i=2;i*i<=x;i++)
        {
            if(x%i==0)
                return false;
        }
        return true;

    }

    public static void main(String[] args)
    {
        if(args.length>0)
        {
            for (String x : args)
                if (isPrime(Integer.parseInt(x)))
                    System.out.println(x);
        }
        else
            System.out.println("There are no args");



    }






    }