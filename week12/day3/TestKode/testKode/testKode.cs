

using System;
namespace Day3
{

    class Program
    {
        static void Main()
        {
            ITrackable thing = new Track(17); // can hold it by the interface type
            Console.WriteLine(thing.Describe());
        }
    }
    interface ITrackable // a pure contract: no fields, no bodies
    {
        string Describe(); // any ITrackable promises to provide this
    }
    class Track : ITrackable // Track promises to fulfil the contract
    {
        public int Id { get; }
        public Track(int id) { Id = id; }
        public string Describe() // fulfilling the promise (no `override` needed)
        => $"Track {Id}";
    }


       
    

    
}
