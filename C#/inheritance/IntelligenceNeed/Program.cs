abstract class Platform
{
    private int _trackid { get; }
    private double _speedknots { get; set; }
    public double SpeedKnots {
        get { return _speedknots; }
        set { if (value < 0) { _speedknots = value * -1; } else { _speedknots = value} } }
    private double _heading { get; set; }
    public Heading { 
        get { return _heading; } 
        set { if (value < 0 || value > 359) { _heading = value 0; } else { _heading = value} } }

    protected Platform(int trackId, double speedKnots, double heading)
    {
        _trackid = trackId;
        SpeedKnots = speedKnots;
        Heading = heading;
    }
    public abstract string StatusLine()
        => $"Track: {_trackid} | {SpeedKnots} knots | {Heading}^ \n";

    public abstract bool IsTrackable() { }
}

