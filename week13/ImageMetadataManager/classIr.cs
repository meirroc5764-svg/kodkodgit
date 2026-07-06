using System;
namespace Project.Sensor
{
    class IrSensor : BaseSensor, IThermalCalibratable
    {
        private int Base = 40;

        public void CalibrateThermal()
        {
            Console.WriteLine("conect god");
        }
        public IrSensor(int id, double clodeClover) : base(id, clodeClover) { }

        public override int Score => Base - (int)ClodeClover;

        public override string GetSensorName()
        {
            return "Ir";
        }
    }
}