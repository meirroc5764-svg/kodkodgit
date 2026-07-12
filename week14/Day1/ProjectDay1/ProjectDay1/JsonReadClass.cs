using System;
using Program.Intreface;
using System.Text.Json;
using Program.repots;
namespace Program.JsonRead
{
    class ReadJson : IReader
    {
        public string GetData(string path)
        {
            if(!File.Exists(path))
                throw new FileNotFoundException();
            return File.ReadAllText(path);
        }

        public void PutInJson(string path, List<Report> validData)
        {
            var options = new JsonSerializerOptions
            {
                WriteIndented = true,
            };

            string json = JsonSerializer.Serialize(validData,options);

            File.WriteAllText(path, json);


        }
    }
}