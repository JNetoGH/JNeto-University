using System;

namespace Lucas
{
    class Program
    {
        static void Main(string[] args)
        {
            int index_in_index = int.Parse(args[0]);
            Console.WriteLine(Lucas(index_in_index));
        }

        private static int Lucas(int n)
        {
            return n switch
            {
                0 => 2,
                1 => 1,
                _ => Lucas(n - 1) + Lucas(n - 2)
            };
        }
    }
}