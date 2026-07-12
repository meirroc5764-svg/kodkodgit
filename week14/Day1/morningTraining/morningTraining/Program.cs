using System.Reflection;
namespace Morning.Project;


class Program
{
    static void Main()
    {
        //ReportDataException reportDataException = new ReportDataException("pesach rigth");
        //ReportDataException reportDataException1 = new ReportDataException("pesach rigth");
        //Console.WriteLine(reportDataException.Message);
        //Console.WriteLine(reportDataException1.Message);
        Console.WriteLine(DateTime.Now.ToString());
    }
}
//try
//{
//    var text = File.ReadAllText("reports.txt");
//    var priority = int.Parse(text);
//}
//catch (FileNotFoundException ex) // narrow: the file is missing
//{
//    Console.WriteLine($"No report file: {ex.FileName}");
//}
//catch (FormatException) // narrow: the contents are malformed
//{
//    Console.WriteLine("Report file has a non-numeric priority.");
//}
//finally
//{
//    Console.WriteLine("Load attempt finished."); // always runs, success or failure
//}
// A failure the built-in types do not describe: a report that parsed but is impossible.
class ReportDataException : Exception
{
    public ReportDataException(string message) : base(message) { }
    public ReportDataException(string message, Exception inner) :
    base(message, inner)
    { }

    // Used at the point the rule is known:
    static int ParsePriority(string text)
    {
        if (!int.TryParse(text, out var priority))
            throw new ReportDataException($"Priority is not a number:'{text}'");
        if (priority < 0)
            throw new ReportDataException($"Priority cannot be negative:{priority}");
        return priority;

    }
}
