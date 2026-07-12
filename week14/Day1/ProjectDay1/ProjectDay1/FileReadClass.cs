using System;
using Program.Intreface;
namespace Program.FileReader
{
    class FileRead : IReader
    {
        public string GetData(string path)
        {
            if(!File.Exists(path))
                throw new FileNotFoundException();
            
            return File.ReadAllText(path);           

        }
    }
}