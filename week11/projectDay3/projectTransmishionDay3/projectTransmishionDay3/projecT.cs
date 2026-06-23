using System;
namespace Day3
{
    enum Classification
    {
        Friendly,
        Hostile,
        Unidentified
    }
    
    class projectT
    {
        

        static void Main()
        {

        }
        
        static int ChekInput()
        {
            bool test = false;
            int userInt = 0;
            while (test == false)
            {
                string? userIn = Console.ReadLine();
                if (int.TryParse(userIn, out userInt))
                    test = true;
                else
                    Console.WriteLine("not number");


            }
            return userInt;
        }
        
        static List<int> IntData(int numList)
        {
            List<int> signalId = new List<int>();
            List<int> strehngSignal = new List<int>();

            if (numList > 2||numList < 1)
            {
                Console.WriteLine($"no have data num :{numList}");
                return null;
            }

            if (numList == 1)
                return signalId;
            else
                return strehngSignal;
        }
        
        static List<Classification> StrData()
        {
            List<Classification> ClasificationData = new List<string>();
            return ClasificationData;
        }

        static void createSignal(Classification userC, int NumStreng)
        {

        }
    }
}