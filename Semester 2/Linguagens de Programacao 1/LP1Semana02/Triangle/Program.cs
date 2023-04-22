using System;

namespace Triangle {
    class Program {
        
        private static void PrintTriangle(int size, char symbol) {
            for (int i = 1; i < size + 1; i++) {
                for (int j = 0; j < i; j++) {
                    Console.Write(symbol);
                }
                Console.WriteLine();
            }
        }

        static void Main(string[] args) {
            Console.WriteLine();
            PrintTriangle(int.Parse(args[0]), char.Parse(args[1]));
        }
    }
}