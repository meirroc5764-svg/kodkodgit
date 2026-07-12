using Program.FileReader;
using Program.JsonRead;
using System;
using Program.Validation;
namespace Program.running
{
    class Program
    {
        static void Main()
        {
            FileRead fileRead = new FileRead();
            ReadJson readJson = new ReadJson();
            Validations validation = new Validations();

            Console.WriteLine("Enter a path");
            string path = Console.ReadLine();

            var reports = validation.ValidatePriority(fileRead.GetData(path));

            readJson.PutInJson("reports.json", reports);
        }
    }
}