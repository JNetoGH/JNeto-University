using System;
using System.Text;

namespace TiposVarios {
    
    internal static class Exec {
        
        private static void Main(string[] args) {
            
            // Setting encoder
            Console.OutputEncoding = Encoding.UTF8;
            
            
            #region Integers
            
            // Guardados nos formatos de Módulo e Sinal(MS), Complemento para 1(c1) e Complemento para 2(c2), 1 bit é reservado para o sinal.
            sbyte n1 = 120; // 8 bits  => 1 byte:  (MS/c1/c2) sign(0)0000000
            short n2 = 651; // 16 bits => 2 bytes: (MS/c1/c2) sign(0)0000000.00000000
            int n3 = 10;    // 32 bits => 4 bytes: (MS/c1/c2) sign(0)0000000.00000000.00000000.00000000
            long n4 = 645;  // 64 bits => 8 bytes: (MS/c1/c2) sign(0)0000000.00000000.00000000.00000000.00000000.00000000.00000000.00000000

            // Alternatives (System Structs), é exatamente a mesma coisa que usar os alias A.K.A short, long, etc...
            // o compilador vai reescrever usando as structs de System.IntX equivalentes anyway.
            Byte n5 = 13;
            Int16 n6 = 13;
            Int32 n7 = 13134;
            Int64 n8 = 13123;
            
            // Unsigned Integers: o 1º bit deixa de ser reservardo para o sinal, liberando esse bit para storage, porém, o número é sempre positivo.
            byte n9  = 225;   // 8 bits  => 1 byte:  (ALWAYS POSITIVE) 00000000
            ushort n10 = 986; // 16 bits => 2 bytes: (ALWAYS POSITIVE) 00000000.00000000
            uint n11 = 464;   // 32 bits => 4 bytes: (ALWAYS POSITIVE) 00000000.00000000.00000000.00000000
            ulong n12 = 1561; // 64 bits => 8 bytes: (ALWAYS POSITIVE) 00000000.00000000.00000000.00000000.00000000.00000000.00000000.00000000
        
            // Literals (Hexadecimal/Binário): é simplesmente uma notação que vem antes do número que permite escrever fora do formato de base 10. 
            int n13 = 0b1001;
            int n14 = 0x54EA;
            
            // Printa os números na tela
            ValueType[] arr = new ValueType[] { n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14 };
            Console.WriteLine(" ");
            for (int i = 0; i < arr.Length; i++) 
                Console.WriteLine($"{arr[i].GetType().Name} n{i} = {arr[i]}");
            Console.WriteLine(" ");

            #endregion
            
            
            #region Unicode

            char character1 = '\u1342';
            Console.WriteLine($"character 1: {character1}");
            
            char character2 = '\u5554';
            Console.WriteLine($"character 2: {character2}");

            #endregion

            
            #region Reais
            
            // Guardados em formatos como o IE754, exemplo em 32 bits: sign(0) expoente(0000000) mantissa(00000000.00000000.00000000)
            float   n15 = 30.342139844f; // 32 bits => 4 bytes
            double  n16 = -13123.44243d; // 64 bits => 8 bytes
            decimal n17 = 151541.98498m; // 128 bits => 16 bytes
            
            // Alternatives (System Structs), o mesmo caso dos integers.
            Single  n18 = 13123.13123f;
            Double  n19 = 13123.12312d;
            Decimal n20 = 52434.13132m;
            
            // Printa os números na tela
            ValueType[] arr2 = new ValueType[] { n15, n16, n17, n18, n19, n20 };
            Console.WriteLine(" ");
            for (int i = 0; i < arr2.Length; i++) 
                Console.WriteLine($"{arr2[i].GetType().Name} n{i+15} = {arr2[i]}");
            Console.WriteLine(" ");
            
            #endregion
            
            
            #region Booleans
            
            var randNum = new Random().Next(1, 10);
            bool flag =  randNum > 5;
            Console.WriteLine($"flag ({randNum} > 5)?: {flag}");

            bool isMorning = DateTime.Now.TimeOfDay.Hours is < 12 and > 4;
            Console.WriteLine($"is it Morning now ({DateTime.Now})? {isMorning}");
            
            #endregion
        }
    }
}