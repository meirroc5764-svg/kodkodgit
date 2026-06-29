using System;
namespace KodDay3
{
    //class Track
    //{
    //    private double _heading; // private field — guarded
    //    public int Id { get; } // read-only after construction
    //    public double Speed { get; set; }
    //    public double Heading // property with validation

    //    {
    //        get => _heading;
    //        set
    //        {
    //            if (value < 0 || value > 359)
    //                _heading = 0; // correct an invalid value at the gate
    //            else
    //                _heading = value;

    //        }
    //    }
    //    public Track(int id, double speed, double heading)
    //    {
    //        Id = id;
    //        Speed = speed;
    //        Heading = heading; // goes through the validating setter
    //    }
    //    public override string ToString() // the object prints itself
    //    => $"Track {Id}: {Speed} kn, heading {Heading}";

    //}
    class age
    {
        private int age;
        public int Age
        {
            get
            {
                return age;
            }

            set
            {
                age = value;
            }
        }
        public age(int Age)
        {
            Age = age
        }

    }
    class program
    {
        static void Main()
        {
            //// create two objects from the one blueprint:
            //Track a = new Track(17, 412.5,200);
            //Track b = new Track(8, 95.0,2000);
            //b._heading = 5;
            //Console.WriteLine($"{a.Id} at {a.Speed} kn");

        }
    }



}
