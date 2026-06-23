namespace ind3
{
    enum ClsType { Friendly, Hostile, Unidentified }
    class In
    { 
        static void AddNewLog(List<int> sourceId, List<ClsType> classification, List<double?> strength)
        {
            Console.WriteLine("Enter source id:");
            int id;
            while (!int.TryParse(Console.ReadLine(), out id))
            {
                Console.WriteLine("Try again, Source id must be a number!");
            }
            Console.WriteLine("Enter classification:");
            ClsType clsf;
            while (!Enum.TryParse<ClsType>(Console.ReadLine(), out clsf))
            {
                Console.WriteLine("Try again, Classification must be in {Friendly, Hostile, Unidentified}!");
            }
            Console.WriteLine("Enter strength:");
            double? hertz;
            if (double.TryParse(Console.ReadLine(), out double hertzAttempt))
            {
                hertz = hertzAttempt;
            }
            else
            {
                hertz = null;
            }               
            sourceId.Add(id);
            classification.Add(clsf);
            strength.Add(hertz);
        }

        static void CalibrateStrength(ref double? hertz)
        {
            Console.WriteLine("Insert calibrated megaHertz:");
            double calibrated_hertz;
            if (double.TryParse(Console.ReadLine(), out calibrated_hertz))
                {hertz = calibrated_hertz; }
            else { hertz = null; }
            hertz = calibrated_hertz;
        }

        static void Calibrate(int id, List<int> sourceId, List<double?> strength)
        {
            int index = sourceId.IndexOf(id);
            if (index < 0) 
            {
                Console.WriteLine("id not found!");
                return;
            }
            double? hertz = strength[index];
            CalibrateStrength(ref hertz);
            strength[index] = hertz;
            Console.WriteLine("Strength calibrated");
        }


        static void ShowAll(List<int> sourceId, List<ClsType> classification, List<double?> strength)
        {
            for (int i = 0; i < sourceId.Count; i++)
            {
                string line = "";
                line += $"ID: {sourceId[i]} | ";
                line += $"Dlassification: {classification[i]} | ";
                if (strength[i] == null) { line += "unknown"; }
                else { line += $"Signal: {strength[i]} | "; }
                Console.WriteLine(line);
            }
        }

        static void Main()
        {
            List<int> sourceId = new();
            List<ClsType> classification = new();
            List<double?> strength = new();

            while (true)
            {
                Console.WriteLine("===Signal Intercept Log===");
                Console.WriteLine("1. Add Log");
                Console.WriteLine("2. Calibrate log signal");
                Console.WriteLine("3.Show all");
                Console.WriteLine("4. Exit");
                string choice = Console.ReadLine();
                switch (choice)
                {
                    case "1":
                        AddNewLog(sourceId, classification, strength);
                        break;

                    case "2":
                        Console.WriteLine("Enter source id:");
                        int id;
                        while (!int.TryParse(Console.ReadLine(), out id))
                        {
                            Console.WriteLine("Try again, Source id must be a number!");
                        }
                        Calibrate(id, sourceId, strength);
                        break;

                    case "3":
                        ShowAll(sourceId, classification, strength);
                        break;

                    case "4":
                        Console.WriteLine("Goodbye");
                        return;

                    default:
                        Console.WriteLine("Invalid option");
                        break;
                }
            }
        }
    }
}
