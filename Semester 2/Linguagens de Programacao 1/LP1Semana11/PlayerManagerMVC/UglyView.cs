using System;
using System.Collections.Generic;

namespace PlayerManagerMVC
{
    public class UglyView : IView
    {
        // This view doesn't actually need a reference to the controller,
        // but generally views will need it
        private readonly Controller controller;

        public UglyView(Controller controller)
        {
            this.controller = controller;
        }

        public int MainMenu(PlayerOrder playerOrder)
        {
            Console.WriteLine("Menu");
            Console.WriteLine("----");
            Console.WriteLine("1. Insert player");
            Console.WriteLine("2. List all players");
            Console.WriteLine("3. List player with score greater than");
            Console.WriteLine(
                $"4. Change player order (currently order is {playerOrder})");
            Console.WriteLine("0. Exit");
            Console.WriteLine("");
            Console.Write("> ");

            return int.Parse(Console.ReadLine());
        }

        public PlayerOrder AskPlayerOrder()
        {
            Console.WriteLine("Player order");
            Console.WriteLine("------------");
            Console.WriteLine(
                $"{(int)PlayerOrder.ByScore}. Order by score");
            Console.WriteLine(
                $"{(int)PlayerOrder.ByName}. Order by name");
            Console.WriteLine(
                $"{(int)PlayerOrder.ByNameReverse}. Order by name (reverse)");
            Console.WriteLine("");
            Console.Write("> ");

            return Enum.Parse<PlayerOrder>(Console.ReadLine());
        }

        public void InvalidOption()
        {
            Console.WriteLine("\nInvalid option! Press any key to continue...");
            Console.ReadKey();
            Console.WriteLine();
        }

        public void ShowPlayers(IEnumerable<Player> players)
        {
            Console.WriteLine();
            foreach (Player p in players)
            {
                Console.WriteLine($"-> {p}");
            }
            Console.WriteLine("\nPress any key to continue...");
            Console.ReadKey();
            Console.WriteLine();
        }

        public (string, int) AskForPlayer()
        {
            string name;
            int score;

            Console.WriteLine();
            Console.WriteLine("Insert player data");
            Console.WriteLine("------------------");
            Console.WriteLine();
            Console.Write("Name > ");
            name = Console.ReadLine();
            Console.Write("Score > ");
            score = int.Parse(Console.ReadLine());

            return (name, score);
        }

        public int AskForMinimumScore()
        {
            Console.WriteLine();
            Console.Write("Minimum score? > ");
            return int.Parse(Console.ReadLine());
        }
    }
}