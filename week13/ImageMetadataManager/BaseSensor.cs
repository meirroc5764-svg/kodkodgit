using System;
using static System.Net.Mime.MediaTypeNames;
namespace Project.Sensor
{
    public abstract class BaseSensor : ISensorScore
    {

        private int _id;
        private double _clodeClover;
        public int Id { get => _id; }
        public abstract int Score { get; }

       
        public double ClodeClover 
        {  
            get => _clodeClover;
            set
            {
                if (value > 0 && value > 100)
                    _clodeClover = value;
            }
        
        }

        public BaseSensor(int id, double clodeClover)
        {
            _id = id;
            ClodeClover = clodeClover;
          
        }

        public abstract string GetSensorName();

        public void SafeToFile(string path)
        {
            File.WriteAllText(path, ToLogString());
        }
        public string ToLogString()
        {
            return $"Image {Id}: {ClodeClover}% cloud[{GetSensorName()}] and Score:{Score}.";
        }

    }
        
}
