using Command.Interface;
using System;
namespace Command.commander
{
    abstract class Command
    {
        private string _rawline;
        private string _target;
        public string RawLine 
        { 
            get => _rawline;
            set => _rawline = value;
            
        }
        public string Target 
        { 
            get => _target;
            set
            {
                if (value == null)
                {
                    throw new ArgumentException("no have target");
                }
                else
                {
                    _target = value;
                }
            }
                
        }
        protected Command(string rawLine, string target)
        {
            RawLine = rawLine;
            Target = target;
        }
        public abstract bool Execute();
    }


    class CreateFileCommand : Command,IUndoable
    {
        public CreateFileCommand(string rawLine, string fileName) : base(rawLine, fileName)
        {
            
        }
        public void Undo()
        {
            Console.WriteLine($"SIMULATED File '{Target}' deleted(undo)");
        }
        public override bool Execute()
        {
            if (Target.StartsWith("_"))
            {
                Console.WriteLine($"SIMULATED] File '{Target}' created");
                return false;
            }
            return true;
            
        }
    }

    class SendEmailCommand : Command
    {
        public SendEmailCommand(string rawLine, string emailAddress) : base(rawLine, emailAddress)
        {

        }

        public override bool Execute()
        {
            if (!Target.Contains("@"))
            {
                Console.WriteLine($"[SIMULATER] Email sent to '{Target}");
                return false;
            }
            return true;
        }

    }
    class BackupCommand : Command,IUndoable,IRetryable
    {
        public BackupCommand(string rawLine, string datasetName) : base(rawLine, datasetName)
        {

        }
        public override bool Execute()
        {
            if (Target.StartsWith("_CORRUPT") || Target.StartsWith("_LOCKED"))
            {
                return false;
            }
            Console.WriteLine($"[SIMULATED] Dataset '{Target}' backed");
            return true;
        }
        public void Undo()
        {
            Console.WriteLine($"[SIMULATED] Backup of '{Target}' removed (undo)");
        }

        public void Retry()
        {
            Execute();
            Console.WriteLine($"[SIMULATED] Retrying backup of '{Target}");
        }

    }
}