using System;
using System.Collections.Generic;

namespace SamePlayer
{
    public class Program
    {
        public static void Main(string[] args)
        {
            HashSet<Player> setOfPlayers = new HashSet<Player>();

            Player player1 = new Player { Type = PlayerType.Tank, Name = "Ana" };
            Player player2 = new Player { Type = PlayerType.Slayer, Name = "Paulo" };
            Player player3 = new Player { Type = PlayerType.Tank, Name = "Ana" };

            setOfPlayers.Add(player1);
            setOfPlayers.Add(player2);
            setOfPlayers.Add(player3);

            foreach (Player p in setOfPlayers)
            {
                Console.WriteLine($"{p.Name} is a {p.Type}");
            }
        }
    }
}