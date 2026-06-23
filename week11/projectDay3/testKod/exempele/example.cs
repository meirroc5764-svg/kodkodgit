using System;
namespace project
{
    class Day3()
    {
        static void Main()
        {
            int x = 10;
            
            List<int> num = new List<int>();
            num.Add(1);
            num.Add(2);
            
            TryDuble(x);
            Console.WriteLine(x);
            
            AddOne(num);
            Console.WriteLine(string.Join(",",num));
            
            if (FindSpeed("TR-1", out double s))
            Console.WriteLine($"found: {s}");
            else
                Console.WriteLine("not found");

            Console.Write(s);
        }
        static void TryDuble(int n)
        {
            n = n * 2;
        }
        static void AddOne(List<int> xs)
        {
            xs.Add(1);
        }
        static bool FindSpeed(string id, out double speed)
        {
            speed = 0; // out parameters must be set before returning
            if (id == "TR-1") 
            {
                speed = 420.5;
                return true; 
            }
            return false;
        }

    }
}
