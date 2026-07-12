using Program.sensor;
using Project.Sensor;
using System;
namespace Project.Program
{
    class Program
    {
        static void Main()
        {
            Imagesever obj = new MemoryStore();

            Pipline my_obj = new Pipline(obj);
            my_obj.Cont();


        }
    }
}