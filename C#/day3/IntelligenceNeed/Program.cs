using System.ComponentModel;

namespace ind3
{
    class In
    { 
        enum Cls {Friendly, Hostile, Unidentified}
        List <int> sourceId = new();
        List<Cls> classification = new();
        List <double?> strength = new();

        static void AddNewLog()
        {
            Console.WriteLine("Enter source id:");
            int id;
            while (!int.TryParse(Console.ReadLine(), out id)
            {
                Console.WriteLine("Source id must be a number!")
            }
            Console.WriteLine("Enter classification:");
            Cls clsf;
            while (!Cls.TryParse(Console.ReadLine(), out clsf)
            {
                Console.WriteLine("Classification must be in {Friendly, Hostile, Unidentified}!")
            }
            Console.WriteLine("Enter strength:");
            double? hertz;
            while (!double.TryParse(Console.ReadLine(), out hertz)
            {
                Console.WriteLine("Strength must be number!")
            }

        }
        














        static void Main()
        {

        }
    }
}