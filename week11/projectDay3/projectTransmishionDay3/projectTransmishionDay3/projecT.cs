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
            List<int> signalId = new List<int>();
            List<int?> strehngSignal = new List<int?>();
            List<Classification> ClasificationData = new List<Classification>();

            while (true)
            {
                Console.WriteLine("====Menu====");
                Console.WriteLine("1. show all signal");
                Console.WriteLine("2. add signal");
                Console.WriteLine("3. remove signal by id");
                Console.WriteLine("4. More");
                Console.WriteLine("5. exit");

                string userChoise = Console.ReadLine();

                if (userChoise != null)
                {
                    Console.WriteLine("not varibale choise");
                    continue;
                }

                if (userChoise == "1")
                {
                    ShowAll(signalId, strehngSignal, ClasificationData);
                }

                if (userChoise == "2")
                {
                    
                    //createSignal()
                }
            }
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
        static int? ChekInput2()
        {
            bool test = false;
            int userInt = 0;
            while (test == false)
            {
                string userIn = Console.ReadLine();
                if (userIn == null || userIn == "null")
                    return null;
                else if (int.TryParse(userIn, out userInt))
                    test = true;
                else
                    Console.WriteLine("enter number or null");


            }
            return userInt;
        }

        static void createSignal(Classification userC, int? NumStreng, List <int> idS, List <Classification> classif, List <int?> strengS)
        {
            int signalId = idS.Count;
            idS.Add(signalId + 1);
            classif.Add(userC);
            strengS.Add(NumStreng ?? null);
        }

        static void updateStreng(int id, int strangS, List <int> lId, List <int> StrangSignal)
        {
            for(int i = 0; i == lId.Count; i++)
            {
                if (id == lId[i])
                    StrangSignal[i] = strangS;

            }
        }
        static void ShowAll(List<int> lid, List<int?> StrengS, List<Classification> Classif)
        {
            for (int i = 0; i == lid.Count; i++)
            {
                Console.WriteLine($"id:{lid[i]}");
                Console.WriteLine($"Classification:{Classif[i]}");
                Console.WriteLine($"Signal Streng:{StrengS[i]}");
                Console.WriteLine("==================");


            }
        }
    }
}