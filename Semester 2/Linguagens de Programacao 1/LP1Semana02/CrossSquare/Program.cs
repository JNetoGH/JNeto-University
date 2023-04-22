using System;

namespace CrossSquare {
    class Program {
        
        private static void PrintCrossSquare(int size) {
            for (int lineIndex = 0; lineIndex < size; lineIndex++) {
                for (int columnIndex = 0; columnIndex < size; columnIndex++) {
                    bool isVerticeOrAresta = lineIndex == 0 || lineIndex == size - 1 || columnIndex == 0 || columnIndex == size - 1;
                    // main diagonal
                    if (lineIndex == columnIndex && !isVerticeOrAresta)
                        Console.Write("X");
                    // secondary diagonal
                    else if (columnIndex == size - lineIndex - 1  && !isVerticeOrAresta)
                        Console.Write("X");
                    else if (isVerticeOrAresta)
                        Console.Write("#");
                    else
                        Console.Write(" ");
                }
                Console.WriteLine();
            }
        }

        static void Main(string[] args) {
            int size = int.Parse(args[0]);
            PrintCrossSquare(size);
        }
    }
}