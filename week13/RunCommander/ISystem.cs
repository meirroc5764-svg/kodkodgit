using System;
using Command.commander;
namespace Command.Interface
{
    interface IUndoable
    {
        public void Undo();
    }

    interface IRetryable
    {
        public void Retry();
    }

    interface ICommandLogger
    {
        void LogResult(Command command, bool success);
    }






}