using System;
namespace test
{
    class TestDay2
    {

        static List<string> tracks = new List<string>(); // ids
        static List<double> speeds = new List<double>(); // matching speeds

        static void Main()
        {
            TestDay2.AddTrack("33", 22.4);
            TestDay2.AverageSpeed();
        }
        static void AddTrack(string id, double speed) // typed inputs,returns nothing
        {
            tracks.Add(id);
            speeds.Add(speed);
        }
        static double AverageSpeed() // returns a double
        {
            if (speeds.Count == 0) return 0.0;
            double sum = 0;
            foreach (double s in speeds) sum += s;
            return sum / speeds.Count;
        }
    }
}