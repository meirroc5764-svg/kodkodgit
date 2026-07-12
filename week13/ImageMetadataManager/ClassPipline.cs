using System;
namespace Project.Sensor
{
    class Pipline
    {
        private Imagesever _sever;
        public Pipline(Imagesever sever) 
        {
            _sever = sever;
        }
        public void create(ISensorScore img)
        {
            _sever.Save(img);
        }
        public void Cont()
        {
            _sever.count();
        }
    }
}