using System;
using System.Collections.Generic;

namespace StringCollections
{
    class Program
    {
        
        static void Main(string[] args)
        {

            List<string> namesList = new List<string>() {"lala", "lele", "lili", "lolo", "lulu"};
            
            Stack<string> namesStack = new Stack<string>();
            namesStack.Push("lala");
            namesStack.Push("lele");
            namesStack.Push("pipi");
            namesStack.Push("popo");
            namesStack.Push("pupu");
            
            Queue<string> namesQueue = new Queue<string>();
            namesQueue.Enqueue("lala");
            namesQueue.Enqueue("lele");
            namesQueue.Enqueue("zizi");
            namesQueue.Enqueue("zozo");
            namesQueue.Enqueue("zuzu");
            
            HashSet<string> namesSet = new HashSet<string>();
            namesSet.Add("lala");
            namesSet.Add("lele");
            namesSet.Add("riri");
            namesSet.Add("roro");
            namesSet.Add("ruru");

            foreach (var str in namesList)
                Console.WriteLine(str);
            
            foreach (var str in namesStack)
                Console.WriteLine(str);
            
            foreach (var str in namesQueue)
                Console.WriteLine(str);
            
            foreach (var str in namesSet)
                Console.WriteLine(str);
            
        }
    }
}