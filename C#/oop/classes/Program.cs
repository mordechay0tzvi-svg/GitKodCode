using System.Net.Quic;

class Track
    {
    public int Id;
    public double Speed;
    public double Heading;
    public Track(int id, double speed, double heading)
    {
        Id = id;
        Speed = speed;
        Heading = heading;
        Console.WriteLine("Track created.");
    }
    public Track(int id) : this(id, 0.0, 0.0) { }

    public string ToString()
    =>$"Track {Id}, Heading {Heading}, at {Speed}.";
    
    }


class program
{
    static void Main()
    {
        Track full = new Track(17, 412.5, 270);
        Track quick = new Track(8);
        Console.WriteLine(full.ToString());
        Console.WriteLine(quick.ToString());
    }
}
