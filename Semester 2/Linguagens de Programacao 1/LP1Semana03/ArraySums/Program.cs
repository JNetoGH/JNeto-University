using System;

namespace ArraySums {
    class Program {
        
        private delegate void MatrixAction(float[,] matrix, int lineIndex, int columnIndex, float[] lineSums, float[] columnSums);

        static void Main(string[] args) {
            
            Console.Write("\nnumber of lines: ");
            int lines = int.Parse(Console.ReadLine());
            Console.Write("number of columns: ");
            int columns = int.Parse(Console.ReadLine());
            Console.WriteLine(" ");
            float[,] floatMatrix = new float[lines, columns];
            
            MatrixAction InitMatrixViaCli = (matrix, lineIndex, columnIndex, lineSums, columnSums) => {
                Console.Write($"insert value to position [{lineIndex}][{columnIndex}]: ");
                matrix[lineIndex, columnIndex] = Convert.ToSingle(Console.ReadLine());
            };

            MatrixAction SumLinesAndColumns = (matrix, lineIndex, columnIndex, lineSums, columnSums) => {
                Console.Write($"[{matrix[lineIndex, columnIndex]}]");
                lineSums[lineIndex] += matrix[lineIndex, columnIndex];
                columnSums[columnIndex] += matrix[lineIndex, columnIndex];
                bool hasFinishedLine = columnIndex == matrix.GetLength(1) - 1;
                if (!hasFinishedLine) return;
                Console.WriteLine($" → line sum {lineIndex}: {lineSums[lineIndex]}");
                bool hasFinishedTheMatrix = lineIndex == matrix.GetLength(0) - 1 && columnIndex == matrix.GetLength(1) - 1;
                if (!hasFinishedTheMatrix) return;
                Console.WriteLine(" ");
                for (int i = 0; i < columnSums.Length; i++) Console.WriteLine($"column sum {i}: {columnSums[i]}");
            };
            
            RunOverMatrix(InitMatrixViaCli, floatMatrix);
            Console.WriteLine("\nMatrix (lines and columns sum)\n");
            RunOverMatrix(SumLinesAndColumns, floatMatrix);
            Console.WriteLine(" ");
        }

        private static void RunOverMatrix(MatrixAction matrixAction, float[,] matrix) {
            float[] lineSums = new float[matrix.GetLength(0)];
            float[] columnSums = new float[matrix.GetLength(1)];
            for (int lineIndex = 0; lineIndex < matrix.GetLength(0); lineIndex++) {
                for (int columnIndex = 0; columnIndex < matrix.GetLength(1); columnIndex++) {
                    matrixAction(matrix, lineIndex, columnIndex, lineSums, columnSums);
                }
            }
        }
        
    }
}