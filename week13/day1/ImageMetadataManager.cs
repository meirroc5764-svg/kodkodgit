using System;
using static System.Net.Mime.MediaTypeNames;
namespace ImageMetadataManager.bad
{
    class ImageMetadataManager
    {
        public int Id;
        public double CloudCover;
        public string Sensor;

        public ImageMetadataManager(int id, double cloudCover, string sensor)
        {
            Id = id;
            CloudCover = cloudCover;
            Sensor = sensor;
        }

        public bool IsValid()
        {
            if (CloudCover < 0) return false;
            if (CloudCover > 100) return false;
            return true;
        }

        public string Format()
        {
            return $"Image {Id}: {CloudCover}% cloud[{Sensor}].";
        }
        public void SaveToFile(string path)
        {
            File.WriteAllText(path, Format());
        }
        public int Score()
        {
            switch(Sensor)
            {
                case "SAR":
                    return 100 - (int)CloudCover;

                case "EO":
                    return 60 - (int)CloudCover;

                case "IR":
                    return 40 - (int)CloudCover;

                default: return 0;
            }
        }

    }
   
}