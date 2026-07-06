using Project.Sensor;
using System;
namespace Program.sensor
{
    class SatelliteImage : BaseSensor
    {
        public override int Score => 0;

        public SatelliteImage(int Id, double ClodeClover) : base(Id, ClodeClover) { }

        public override string GetSensorName()
        {
            return "SatelliteImage";
        }

    }
}