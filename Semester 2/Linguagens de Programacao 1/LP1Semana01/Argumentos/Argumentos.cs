using System;
using System.Linq;

namespace Argumentos {
    internal static class Program {
        static void Main(string[] args) => args.ToList().ForEach(s => Console.WriteLine(s));
    }
}
