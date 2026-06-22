namespace d2
{
    class Tracks
    {

        static List<string> tracksIds = new();
        static List<double> speeds = new();
        static List<int> heading = new();

        static void AddTrack(string id, double speed, int angle)
        {
            tracksIds.Add(id);
            speeds.Add(speed);
            heading.Add(angle);
        }

        static bool RemoveTrackById(string id)
        {
            int index = tracksIds.IndexOf(id);
            if (index == -1) 
                return false;
            tracksIds.RemoveAt(index);
            speeds.RemoveAt(index);
            heading.RemoveAt(index);
            return true;
        }

        static string FindTrackById(string id)
        {
            int index = tracksIds.IndexOf(id);
            if (index < 0) 
                return " ";
            string track = $"ID: {tracksIds[index]}";
            track += $"speed: {speeds[index]}";
            track += $"direction: {heading[index]}";
            return track;
        }

        static List<string> ListAllTracks()
        {
            List<string> tracks = new();
            for (int i = 0; i < tracksIds.Count; i++)
            {
                tracks.Add(FindTrackById(tracksIds[i]));
            }
            return tracks;
        }

        static List<string> Filter(double threshold)
        {
            List<string> fastTracksIds = new();
            for (int i = 0; i < tracksIds.Count; i++)
            {
                if (speeds[i] > threshold) 
                    fastTracksIds.Add(tracksIds[i]);
            }
            return fastTracksIds;
        }

        static List<string> Filter(int direction)
        {
            List<string> trackInDirection = new();
            for (int i = 0; i < tracksIds.Count; i++)
            {
                if (heading[i] / 60 == direction)
                    trackInDirection.Add(tracksIds[i]);

            }
            return trackInDirection;
        }

        static void PrintList(List<string> list)
        {
            for (int i = 0; i < list.Count; i++) 
                Console.WriteLine(list[i]);
        }

        static void Main()
        {
            while (true)
            {
                Console.WriteLine("=========Track Fleet Manager========");
                Console.WriteLine("1. Add track");
                Console.WriteLine("2. Remove track");
                Console.WriteLine("3. Find track");
                Console.WriteLine("4. List tracks");
                Console.WriteLine("5. Filter tracks");
                Console.WriteLine("6. Exit");
                string choice = Console.ReadLine();
                switch (choice)
                {
                    default:
                        Console.WriteLine("Invalid optiop");
                        continue;
                    case "1":
                        {                         
                        Console.WriteLine("Add track;");
                        Console.WriteLine("Enter ID:");
                        string track_id = Console.ReadLine();
                        Console.WriteLine("Enter speed:");
                        double.TryParse(Console.ReadLine(), out double speed);
                        Console.WriteLine("Enter direction:");
                        int.TryParse(Console.ReadLine(), out int angle);
                        AddTrack(track_id, speed, angle);
                        break;
                        }

                    case "2":
                        {
                            Console.WriteLine("Remove track;");
                            Console.WriteLine("Enter ID:");
                            string track_id = Console.ReadLine();
                            bool removed = RemoveTrackById(track_id);
                            if (removed) 
                                Console.WriteLine("Track removed");
                            else 
                                Console.WriteLine("Track not found");
                            break;
                        }

                    case "3":
                        { 
                        Console.WriteLine("Find track;");
                        Console.WriteLine("Enter ID:");
                        string track_id = Console.ReadLine();
                        string track = FindTrackById(track_id);
                        if (track == " ") 
                            Console.WriteLine("Track not found");
                        else 
                            Console.WriteLine(track);
                        break;
                        }

                    case "4":
                        {
                            PrintList(ListAllTracks());
                            break;
                        }
                        

                    case "5":
                        { 
                        Console.WriteLine("1. Filter by threshold");
                        Console.WriteLine("2. Filter by clockwise direction");
                        string filtration = Console.ReadLine();
                        if (filtration == "1")
                        {
                            Console.WriteLine("Enter threshold:");
                            double.TryParse(Console.ReadLine(), out double filter);
                            PrintList(Filter(filter));
                        }
                        else if (filtration == "2")
                        {
                            Console.WriteLine("Enter diraction:");
                            int.TryParse(Console.ReadLine(), out int filter);
                            PrintList(Filter(filter));
                        }
                        break;
                        }
                    case "6":
                        { 
                        Console.WriteLine("Goodbye");
                        return;
                        }

                } // switch
            } // while 
        } // main
    } // class
} //namespace