//using System.Net.Quic;

//class Track
//    {
//    public int Id;
//    public double Speed;
//    public double Heading;
//    public Track(int id, double speed, double heading)
//    {
//        Id = id;
//        Speed = speed;
//        Heading = heading;
//        Console.WriteLine("Track created.");
//    }
//    public Track(int id) : this(id, 0.0, 0.0) { }

//    public string ToString()
//    =>$"Track {Id}, Heading {Heading}, at {Speed}.";

//    }


//class program
//{
//    static void Main()
//    {
//        Track full = new Track(17, 412.5, 270);
//        Track quick = new Track(8);
//        Console.WriteLine(full.ToString());
//        Console.WriteLine(quick.ToString());
//    }
//}
class Track
{
    private double _heading; 
    public int Id { get; }
    public double Speed { get; set; }
    public double Heading 
    {
        get => _heading;
        set
        {
            if (value < 0 || value > 359)
                _heading = 0;
            else
                _heading = value;
        }
    }
    public Track(int id, double speed, double heading)
    {
        Id = id;
        Speed = speed;
        Heading = heading; 
    }
    public override string ToString() 
    => $"Track {Id}: {Speed} kn, heading {Heading}";
}


class program
{
    static void Main()
    {
        Track t = new Track(17, 412.5, 270);
        Console.WriteLine(t);
        t.Heading = 999; 
        Console.WriteLine(t.Heading); 
    }
}
