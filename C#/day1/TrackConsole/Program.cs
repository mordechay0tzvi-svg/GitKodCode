namespace CsHARP
{
    class ConsoleReadout
    {
        static void Main()
        {
            
            string raw = "start"
            while (!int.TryParse(raw, out int id))
            {
                if (!raw == "start")
                {
                    Console.Write("Enter Track ID:");
                }
                
                raw = Console.ReadLine();
                Console.WriteLine("ID must be a number");
                
            }

            raw = "start"
            while (!int.TryParse(raw, out int speed))
            {
                if (!raw == "start")
                {
                    Console.WriteLine("Speed must be a number");
                }
                Console.Write("Enter Speed:");
                raw = Console.ReadLine();
            }


            raw = "start"
            while (!int.TryParse(raw, out int direction))
            {
                if (!raw == "start")
                {
                    Console.WriteLine("Direction must be a number");
                }
                Console.Write("Enter Direction:");
                raw = Console.ReadLine();
            }

            if (direction < 0 || direction > 359)
            {
                Console.WriteLine("Direction must be an angle");
                return;
            }


            Console.Write("Enter Status:");
            string status = Console.ReadLine();


            string threshhold;
            if (speed < 100) threshhold = "slow";
            else if (speed < 200) threshhold = "medium";
            else threshhold = "fast";


            int heading = direction / 30;
            double kpm = speed / 60.0;


            Console.WriteLine($" === Track Report ===");
            Console.WriteLine($"Track ID: {id}");
            Console.WriteLine($"Speed: {speed} kph({threshhold})");
            Console.WriteLine($"(Heading: {direction} degrees");
            Console.WriteLine($"Status: {status}");
            Console.WriteLine($"Hourly direction {heading}");
            Console.WriteLine($"Kilometer per minute {kpm}");


        }
    }
}

