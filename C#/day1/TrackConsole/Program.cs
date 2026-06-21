namespace csharp
{
    class ConsoleReadout
    {
        static void Main()
        {
            
            int id;
            Console.Write("Enter Track ID:");
            string raw = Console.ReadLine();
            while (!int.TryParse(raw, out id))
            {               
                Console.WriteLine("ID must be a number");               
                Console.Write("Enter Track ID:");
                raw = Console.ReadLine();
            }


            int speed;
            Console.Write("Enter Speed:");
            raw = Console.ReadLine();
            while (!int.TryParse(raw, out speed))
            {               
                Console.WriteLine("Speed must be a number");               
                Console.Write("Enter Speed:");
                raw = Console.ReadLine();
            }


            int direction;
            Console.Write("Enter Direction:");
            raw = Console.ReadLine();
            while (!int.TryParse(raw, out direction))
            {              
                Console.WriteLine("Direction must be a number");               
                Console.Write("Enter Direction:");
                raw = Console.ReadLine();               
            }
            if (direction < 0 || direction > 359)
            {
                Console.WriteLine("Direction must be an angle");
            }


            Console.Write("Enter Status:");
            string status = Console.ReadLine();

            string threshold;
            if (speed < 100) threshold = "slow";
            else if (speed < 200) threshold = "medium";
            else threshold = "fast";


            int heading = direction / 30;
            double kpm = speed / 60.0;


            Console.WriteLine($" === Track Report ===");
            Console.WriteLine($"Track ID: {id}");
            Console.WriteLine($"Speed: {speed} kph({threshold})");
            Console.WriteLine($"Heading: {direction} degrees");
            Console.WriteLine($"Status: {status}");
            Console.WriteLine($"Hourly direction {heading}");
            Console.WriteLine($"Kilometer per minute {kpm}");

        }
    }
}

