using System;
using System.Collections.Generic;
using System.Linq;

namespace ChangeString {
    class Program {
        
        static void Main(string[] args) {
            Console.Write("\ninsert a string: ");
            string str = Console.ReadLine();
            
            Console.Write("\ninsert a char to be removed from the string: ");
            char c = Convert.ToChar(Console.ReadLine());
            
            Console.WriteLine($"\nresult: {ChopOut(str, c)}");
        }

        private static string ChopOut(string str, char charToBeRemoved) {
            List<char> list = str.ToCharArray().ToList();
            list.RemoveAll((currentChar) => currentChar == charToBeRemoved);
            return new string(list.ToArray());
        }
        
    }
}