class Test
{
    static void Main()
    {
        int a = 7;
        int b = 2;
        Console.WriteLine(a / b); // 3 <- both are int, the fraction is dropped
        Console.WriteLine(7.0 / 2); // 3.5 <- one side is double, so theresult is double
        int total = 7;
        int count = 2;
        double average = (double)total / count; // cast one side to double first
        Console.WriteLine(average); // 3.5
    }
}        

       