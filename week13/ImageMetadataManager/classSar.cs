using System;
namespace Project.Sensor
{
    class SarSensor : BaseSensor
    {
        protected int Base = 60;
        public SarSensor(int id, double clodeClover) : base(id, clodeClover) { }

        public override int Score => Base - (int)ClodeClover;
        public override string GetSensorName()
        {
            return "Sar";
        }
    }
}