using System;

namespace ManipulaVar {
    
    class Program {
        
        static void Main(string[] args) {

            try {
                int value = int.Parse(args[0]);
                int copy1 = value;
                int copy2 = value;
                copy1++;
                --copy2;
                Console.WriteLine($"copy1++: {copy1}");
                Console.WriteLine($"--copy2: {copy2}");
            }
            catch (FormatException e) {
                Console.WriteLine("args[0] is not a valid integer number");
            }

        }
    }
}