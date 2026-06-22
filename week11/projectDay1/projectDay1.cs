using System;
namespace projectDay1
{
    class firstPdirroject
    {
        static void Main()

        {
            bool UserInput = false;
            int myId = 0;


            while (UserInput == false)
            {
                Console.Write("Enter a id:");
                string UserId = Console.ReadLine();
                if (int.TryParse(UserId, out myId))
                {
                    UserInput = true;
                }
            }
            
            UserInput = false;
            int heading = 0;


            while (UserInput == false)
            {
                Console.Write("Enter a heading:");
                string UserHeading = Console.ReadLine();
                if (int.TryParse(UserHeading, out heading))
                {
                    UserInput = true;
                }
            }

            UserInput = false;
            int speed = 0;


            while (UserInput == false)
            {
                Console.Write("Enter a speed:");
                string UserSpeed = Console.ReadLine();
                if (int.TryParse(UserSpeed, out speed))
                {
                    string wordSpeed;
                    if (speed < 60) ;
                    {
                        wordSpeed = "slow";
                    }
                    else if (speed < 100) ;
                    {
                        wordSpeed = "medium";
                    }
                    else if (speed > 100) ;
                    {
                        wordSpeed = "fast";
                    }


                    UserInput = true;
                }
            }

            