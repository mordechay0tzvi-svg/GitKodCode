static void TryDouble(int n)
{
n = n * 2;
}
static void AddOne(List<int> xs)
{
xs.Add(1);
}

int x = 10;
TryDouble(x);
Console.WriteLine(x);
List<int> list = new List<int>();
AddOne(list);
Console.WriteLine(list.Count);

static bool FindSpeed(string id, out double speed)
{
speed = 0;
if (id == "TR-1") { speed = 420.5; return true; }
return false;
}
if (FindSpeed("tr-1", out double s))
Console.WriteLine($"found: {s}");
else
Console.WriteLine("not found");
Console.WriteLine(s);

//enum TrackStatus { Active, Lost, Intercepted }
//TrackStatus st = TrackStatus.Active;
//Console.WriteLine(st);
//if (st == TrackStatus.Active)
//    Console.WriteLine("track is active");

double? speed = null; 
Console.WriteLine(speed.HasValue); 
Console.WriteLine(speed ?? -1); 
speed = 412.5; 
Console.WriteLine(speed.HasValue); 
Console.WriteLine(speed.Value); 

