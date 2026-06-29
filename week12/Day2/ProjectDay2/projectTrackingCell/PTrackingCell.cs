using System;
namespace projectTC
{
    class Program
    {
        static void Main()
        {
            List<Platform> platforms = new List<Platform>();

            platforms.Add(new AirPlatform(1, 500, 90, 30000));
            platforms.Add(new AirPlatform(2, 0, 180, 30000));

            platforms.Add(new SeaPlatform(3, 25, 270, 100));
            platforms.Add(new SeaPlatform(4, 20, 45, 500));

            platforms.Add(new GroundPlatform(5, 60, 180, "Road"));
            platforms.Add(new GroundPlatform(6, 50, 90, "Lava"));

            foreach (Platform platform in platforms)
            {
                Console.WriteLine(platform.StatusLine());
                Console.WriteLine($"Trackable: {platform.IsTrackable()}");
                Console.WriteLine();
            }
        }
    }

    abstract class Platform
    {
        protected int _trackId;
        protected double _speedKnots;
        protected double _heading;

        public int TrackId
        {
            get { return _trackId; }
        }

        public double Speedknots
        {
            get
            {
                return _speedKnots;
            }
            set
            {
                if(value >= 0.0)
                    _speedKnots = value;
                else
                    _speedKnots = 0.0;
            }

        }
        public double Heading
        {
            get => _heading;
            set
            {
                if (value < 0 || value > 359)
                {
                    _heading = 0;
                }
                else
                {
                    _heading = value;
                }
            }
        }
        protected Platform(int TrackId, double speedKnots, double heading)
        {
            _trackId = TrackId;
            Speedknots = speedKnots;
            Heading = heading;
        }
        public abstract string StatusLine();

        public abstract bool IsTrackable();



    }
    class AirPlatform : Platform
    {
        protected double _altitudeFeet;

        public double AiritudeFeet
        {
            get => _altitudeFeet;
            set => _altitudeFeet = value;
        }

        public AirPlatform(int TrackId, double SpeedKnots, double Heading, double altitudeFeet)
            : base (TrackId, SpeedKnots,Heading)
        {
            AiritudeFeet = altitudeFeet;
        }
        public override string StatusLine()
        {
            return $"id: {TrackId}, SpeedKnots: {Speedknots}, Heading: {Heading}, AltitudeFeet: {AiritudeFeet}";
        }

        public override bool IsTrackable()
        {
            if ((AiritudeFeet < 60000 & AiritudeFeet > 100) & Speedknots > 0)
                return true;
            else
                return false;
        }
    }
    class SeaPlatform : Platform
    {
        protected double _deptMeters;

        public double DepthMeters
        {
            get => _deptMeters;
            set => _deptMeters = value;
        }
        public SeaPlatform(int TrackId, double SpeedKnots, double Heading, double depthMeters)
            : base(TrackId, SpeedKnots, Heading)
        {
            DepthMeters = depthMeters;
        }

        public override string StatusLine()
        {
            return $"id: {TrackId}, SpeedKnots: {Speedknots}, Heading: {Heading}, DepthMeters: {DepthMeters}";
        }

        public override bool IsTrackable()
        {
            if (DepthMeters < 301 & DepthMeters > 0)
                return true;
            else
                return false;
        }
    }
    class GroundPlatform : Platform
    {
        protected string _terraintype;

        public string TerrainType
        {
            get => _terraintype;
            set => _terraintype = value;
        }
        public GroundPlatform(int TrackId, double SpeedKnots, double Heading, string terrainType)
            : base(TrackId, SpeedKnots, Heading)
        {
            TerrainType = terrainType;
        }

        public override string StatusLine()
        {
            return $"id: {TrackId}, SpeedKnots: {Speedknots}, Heading: {Heading}, TerrainType: {TerrainType}";
        }

        public override bool IsTrackable()
        {
            if (TerrainType.ToLower() == "tunnel")
                return true;
            else
                return false;
        }
    }
}   
