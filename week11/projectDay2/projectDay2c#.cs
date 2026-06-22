using System;
namespace day2
{
    class Test
    {
        static string userInput;
        static int userNum;


        static List<int> trackId = new List<int>();
        static List<int> trackSpeed = new List<int>();
        static List<string> trackHeading = new List<string>();

        static void Main()
        {

        }
        static int TestUserInt(string userInput)
        {
            bool test = false;

            while (test == false)
            {
                userInput = Console.ReadLine();
                if (int.TryParse(userInput, out userNum))
                {
                    test = true;
                }
            }
            return userNum;
        }
        static string TestUserStr(string userInput)
        {
            bool test = true;

            while (test == false)
            {
                userInput = Console.ReadLine();
                if (int.TryParse(userInput, out userNum))
                {
                    test = false;
                }
            }
            return userInput;
        }
        static void AddTrack(int id, int speed,string heading)
        {
            trackId.Add(id);
            trackSpeed.Add(speed);
            trackHeading.Add(heading);
            Console.WriteLine(trackId.Count);
        }
        static void removeTrack(int id)
        {
            for (int i = trackId.Count - 1; i > 0; i--)
            {
                if (trackId[i] == id)
                {
                    trackId.Remove(trackId[i]);
                    trackSpeed.Remove(trackId[i]);
                    trackHeading.Remove(trackHeading[i]);
                    Console.WriteLine(trackId.Count);
                }
            
            }
        }
        static void FindTrackById(int id)
        {
            for (int i = trackId.Count - 1; i > 0; i--)
            {
                if (trackId[i] == id)
                {
                    Console.WriteLine(trackId[i]);
                    Console.WriteLine(trackId[i]);
                    Console.WriteLine(trackHeading[i]);
                }

            }
        }
        static List<int> FilterTrack(int speed)
        {
            List<int> ids = new List<int>();
            for (int i = trackSpeed.Count  - 1; i > 0; i -- )
            {
                if (trackSpeed[i] == speed)
                {
                    ids.Add(trackId[i]);
                }
            }
            return ids;

        }
        static List<int> FilterTrack(string heading)
        {
            List<int> ids = new List<int>();
            for (int i = trackSpeed.Count - 1; i > 0; i--)
            {
                if (trackHeading[i] == heading)
                {
                    ids.Add(trackId[i]);
                }
            }
            return ids;

        }
        static void ShowAll()
        {
            for (int i = 0; i == trackId.Count; i ++)
            {
                Console.WriteLine(trackId[i]);
                Console.WriteLine(trackSpeed[i]);
                Console.WriteLine(trackHeading[i]);
                Console.WriteLine("==================");
            }
        }
        static int Count()
        {
            return trackId.Count;
        }
        static int AvergeSpeeed()
        {
            return trackSpeed.Sum() / trackSpeed.Count;
        }
        static int FastestTrack()
        {
            return trackSpeed.Max();
        }

    }

}


