using System;
using System.Collections.Generic;

namespace RandomDice
{
    public class Dice
    {
        public int Value { get; private set; }

        public Dice() => Value = new Random().Next(1, 7);
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("\nInsert the total of dices: ");
            int totalOfDices = int.Parse(Console.ReadLine());

            List<Dice> dices = new List<Dice>();
            Console.WriteLine("\nDices: ");
            for (int i = 0; i < totalOfDices; i++)
            {
                dices.Add(new Dice());
                if (i == totalOfDices - 1)
                    Console.Write(dices[i].Value);
                else
                    Console.Write(dices[i].Value + " ");
            }

            Console.WriteLine("\n\nSum:");
            int sumOfDices = 0;
            dices.ForEach(dice => sumOfDices += dice.Value);
            Console.WriteLine(sumOfDices);
        }
    }
}