using System;
namespace Project.Sensor
{
    public interface ISensorScore
    {
        public string ToLogString();
    }
    public interface IRetaskablte
    {
        void retask();
    }

    public interface IThermalCalibratable
    {
        void CalibrateThermal();
    }
}