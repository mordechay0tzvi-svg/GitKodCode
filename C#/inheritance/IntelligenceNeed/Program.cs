abstract class Platform
{
    protected int _trackid { get; }
    private double _speedknots { get; set; }
    public double SpeedKnots {
        get { return _speedknots; }
        set { if (value < 0) { _speedknots = value * -1; } else { _speedknots = value; } } }
    private double _heading { get; set; }
    public double Heading { 
        get { return _heading; } 
        set { if (value < 0 || value > 359) { _heading = 0; } else { _heading = value; } } }

    protected Platform(int trackId, double speedKnots, double heading)
    {
        _trackid = trackId;
        SpeedKnots = speedKnots;
        Heading = heading;
    }
    public abstract string StatusLine();
    public abstract bool IsTrackable();
}

class AirPlatform : Platform
{
    private double _altitudeFeet { get; set; }
    public double AltitudeFeet {
        get { return _altitudeFeet; }
        set { if (value < 0) { value = 0; } _altitudeFeet = value; } }

    public AirPlatform(int trackId, double speedKnots, double heading, double AltitudeFeet) :base(trackId, speedKnots, heading) 
        { _altitudeFeet = AltitudeFeet; }
    public override bool IsTrackable() {return (60000 < _altitudeFeet || _altitudeFeet < 100);}
    public override string StatusLine()
        => $"Track: {_trackid} | {SpeedKnots} knots | {Heading}^  {AltitudeFeet} high\n";
}

class SeaPlatform : Platform
{
    private double _depthMeters { get; set; }
    public double DepthMeters{
        get { return _depthMeters; }
        set { if (value < 0) { value *= -1; } _depthMeters = value; }
    }

    public SeaPlatform(int trackId, double speedKnots, double heading, double DepthMeters) : base(trackId, speedKnots, heading)
        { _depthMeters = DepthMeters; }
    public override bool IsTrackable() { return (300 < DepthMeters || DepthMeters < 0); }
    public override string StatusLine()
        => $"Track: {_trackid} | {SpeedKnots} knots | {Heading}^ | {DepthMeters} deep\n";
}

class GroundPlatform : Platform
{
    private string _terrainType { get; set; }
    
    public GroundPlatform(int trackId, double speedKnots, double heading, string TerrainType) : base(trackId, speedKnots, heading)
        { _terrainType = TerrainType; }
    public override bool IsTrackable() { return (_terrainType != "tunnel"); }
    public override string StatusLine()
        => $"Track: {_trackid} | {SpeedKnots} knots | {Heading}^ | On: {_terrainType}\n";
}

class Prog 
{
        static void Main()
    {
        List<Platform> allPlatforms = new()
        {
            new AirPlatform(10001, 250.5, 188.1, 40000.9),
            new AirPlatform(10002, 200.0, 95.6, 20.0),
            new SeaPlatform(10003, 60, 66.6, 301.1),
            new SeaPlatform(10004, 57.3, 77.3, 13),
            new GroundPlatform(10005, 25.7, 180.0, "tunnel"),
            new GroundPlatform(10006, 29.8, 30.4, "sand")
        };
        foreach (Platform obj in allPlatforms)
        {
            Console.WriteLine(obj.IsTrackable());
            Console.WriteLine(obj.StatusLine());
        }
        Console.ReadKey();

    }
}


