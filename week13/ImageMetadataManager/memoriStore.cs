using System;
namespace Project.Sensor
{
    public class MemoryStore : Imagesever,ISensorScore
    {
        private List<ISensorScore> _sensor;

        public MemoryStore() 
        {
            _sensor = new List<ISensorScore>();
        }
        public void Save(ISensorScore sensorScore)
        {
             _sensor.Add(sensorScore);
        }
        public void count()
        {
            Console.WriteLine(_sensor.Count);
        }
    }
}