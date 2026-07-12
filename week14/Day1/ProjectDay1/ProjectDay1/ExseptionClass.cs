using System;
namespace Program.Exseptions
{
    class NegativeClasificationExseption : Exception
    {
        public NegativeClasificationExseption(string Message):base (Message) { }
        public NegativeClasificationExseption(string Message, Exception inner) 
            : base (Message, inner) 
        { }
    }
}