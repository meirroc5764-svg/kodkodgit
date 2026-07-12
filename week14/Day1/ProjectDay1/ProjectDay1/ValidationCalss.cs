using System;
using Program.Exseptions;
using Program.FileReader;
using Program.repots;
namespace Program.Validation
{
    class Validations
    {
        //FileRead fileRead = new FileRead();
        public List<Report> ValidatePriority(string allData)
        {
            List<Report> ValidData = new List<Report>();
            try
            {
                //string all_data = fileRead.GetData(path);
                foreach (string line in allData.Split("\n"))
                {
                    string[] splitLine = line.Split(" ");

                    if (ValidationsLine(splitLine))
                    {
                        Report report = new Report(splitLine[0], splitLine[1], splitLine[2]);
                        ValidData.Add(report);
                    }
                }
            }
            
            catch(FileNotFoundException ex)
            {
                Console.WriteLine(ex.Message);
            }
            
            catch (Exception ex)
            {
                Console.WriteLine($"you have Exteption {ex}");
            }
            return ValidData;
            
        }
        private bool ValidationsLine(string[] splitLine)
        {
            if (splitLine.Length != 3)
                throw new FormatException($"line.Length not valid{splitLine.Length}");

            if (!int.TryParse(splitLine[2], out int Priority) || !int.TryParse(splitLine[0], out int id))
            {
                throw new FormatException("number Is invalid");
            }
            if (Priority < 0)
            {
                throw new NegativeClasificationExseption($"{Priority} is invalid");
            }
            return true;
        }
    }
}