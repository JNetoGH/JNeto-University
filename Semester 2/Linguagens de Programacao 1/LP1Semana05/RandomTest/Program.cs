using System;

namespace RandomTest
{
    public class Program
    {
        private static void Main(string[] args)
        {
            Random r1 = new Random(1233);
            Random r2 = new Random(212);
            
            for (int i = 0; i < 4; i++)
                Console.WriteLine(r1.Next());
           
            Console.WriteLine();
            
            for (int i = 0; i < 4; i++)
                Console.WriteLine(r2.Next());
        }
    }
}
