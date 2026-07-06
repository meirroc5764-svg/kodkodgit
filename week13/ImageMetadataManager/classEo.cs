using System;
namespace Project.Sensor
{
    class EoSensor : BaseSensor
    {
        private int Base = 60; 
        public EoSensor(int id, double clodeClover) : base(id, clodeClover){ }

        public override int Score => Base - (int)ClodeClover;

        public override string GetSensorName()
        {
            return "Eo";
        }
    }
}