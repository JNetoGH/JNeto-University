using System;

namespace GameSixFriday
{
    public class Program
    {
        private static void Main()
        {
            GameLevel gl = new GameLevel(15, Difficulty.Hard);

            gl.SetFoeInRoom(2, new Foe("Darth Vader"));
            gl.SetFoeInRoom(5, new Foe("Borg Queen"));
            gl.SetFoeInRoom(11, new Foe("Thanos"));
            gl.SetFoeInRoom(12, new Foe("Xenomorph"));

            Console.WriteLine($"Difficulty: {gl.GetDifficulty()}");

            Console.WriteLine($"Number of rooms: {gl.GetNumRooms()}");

            Console.WriteLine($"Number of foes: {gl.GetNumFoes()}");

            gl.PrintFoes();

            // Este programa mostra o seguinte no ecrã:
            //
            // Difficulty: Hard
            // Number of rooms: 15
            // Number of foes: 4
            // Room 2: Darth Vader
            // Room 5: Borg Queen
            // Room 11: Thanos
            // Room 12: Xenomorph
        }
    }
}