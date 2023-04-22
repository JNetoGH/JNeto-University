using System;
using System.Linq;

namespace ArgLongString{
    class Exec {
        static void Main(string[] args) {
            args.ToList().ForEach(s => Console.WriteLine(s.Length > 4 ? s.ToUpper() : ""));
        }        
    }
}
