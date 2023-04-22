using System;

namespace Specials {
    class Program {

        static void PrintCyanText(string txt) {
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine(txt);
            Console.ResetColor();
        }
    
        static void Main(string[] args) {
        
            PrintCyanText("\nEx 6");
            Console.WriteLine($"Positive Infinity: {double.PositiveInfinity}");
            Console.WriteLine($"Negative Infinity: {double.NegativeInfinity}");
            Console.WriteLine($"Nan: {float.NaN}\n");
        
            PrintCyanText("EX 7 (Overflow Integers)");
            Int32 signed32BitsInteger = Int32.MaxValue;
            Console.WriteLine($"32 bits integer: {(Int32) signed32BitsInteger + 1}\n");

            PrintCyanText("EX 7 (Overflow Floating Point)");
            Single decimal32Bits = Single.MaxValue * 123;
            Double decimal64Bits = (Double) Decimal.MaxValue + 2;
            Console.WriteLine($"32 bits: {decimal32Bits}");
            Console.WriteLine($"64 bits: {decimal64Bits}\n");
        
            PrintCyanText("EX 7 (Underflow Floating Point)");
            Single singlePrecision1, singlePrecision2;
            singlePrecision1 = singlePrecision2 = 10000000000.000003f;
            Console.WriteLine(singlePrecision1 == singlePrecision2 + 0.00000000000001);
        
        }
    
    }
}



