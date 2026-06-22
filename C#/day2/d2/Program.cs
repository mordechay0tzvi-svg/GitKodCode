namespace d2
{
    class d2
    {
        static void arrayvslist()
        {
            int[] sectorIds = new int[3];
            sectorIds[0] = 10;
            sectorIds[1] = 20;
            sectorIds[2] = 30;
            Console.WriteLine(sectorIds.Length);
            List<double> speeds = new List<double>();
            speeds.Add(412.5);
            speeds.Add(95.0);
            speeds.Remove(95.0);
            Console.WriteLine(speeds.Count);


        }
        static void Main()
        {
            arrayvslist();
            Console.ReadKey();
        }
    }
}