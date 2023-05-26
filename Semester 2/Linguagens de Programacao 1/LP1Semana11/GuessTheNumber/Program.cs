using System;

namespace GuessTheNumber
{
    public class Program
    {
        private static void Main()
        {
            new Controller(new View(), new Model()).RunGame();
        }
    }
}
