using System;
namespace Program.repots
{
    class Report
    {
        private string _id;
        private string _category;
        private string _priority;

        public string Id
        {
            get => _id;
            set => _id = value;
        }

        public string Category
        {
            get => _category;
            set => _category = value;
        }

        public string Priority
        {
            get => _priority;
            set => _priority = value;
        }
        public Report(string id, string category, string priority)
        {
            Id = id;
            Category = category;
            Priority = priority;
        }
    }
}