using System;
using BulbsPuzzle.Enums;
using BulbsPuzzle.Interfaces;

namespace BulbsPuzzle
{
    /// <summary>
    /// This class is the entry point of the game
    /// </summary>
    class Program
    {
        /// <summary>
        /// The Main method runs the Game Loop 
        /// </summary>
        static void Main(string[] args)
        {
            Bulb[] bulbs = { new Bulb(), new Bulb(), new Bulb() };
            IBulbButton[] buttons = { new SimpleButton(bulbs[0]), new SwitchButton(bulbs[0], bulbs[1]), new SwitchButton(bulbs[1], bulbs[2]) };
            
            for (int i = 0; i < 6; i++)
            {
                // UI
                Console.WriteLine($"\nROUND {i+1}/6");
                PrintBulbs(bulbs);
                PrintButtonLabels();
                Console.Write("\nPlease Select a Button (1, 2 or 3): ");
                
                // Input Validation Loop
                int buttonIndex = 0;
                while (true)
                {
                    bool isInputValid = true;
                    try
                    {
                        buttonIndex = int.Parse(Console.ReadLine());
                        if (buttonIndex < 1 || buttonIndex > 3)
                            throw new Exception();
                    }
                    catch (Exception e)
                    {
                        isInputValid = false;
                        Console.Write("Invalid Input, please pick a button from 1 to 3: ");
                    }
                    if (isInputValid) 
                        break;
                }
                
                // Game Button Activation
                buttons[buttonIndex-1].Press();
                Console.WriteLine("\n------------------------------------------------");
            }
            
            bool hasWon = Array.TrueForAll(bulbs, bulb => bulb.State == BulbState.On);
            PrintBulbs(bulbs);
            Console.WriteLine("\n" + (hasWon ? "YOU WIN" : "YOU LOSE") + "!!!!!!!");
        }

        /// <summary>
        /// Prints the bulbs and its states (On/Off).
        /// </summary>
        /// <param name="bulbs">An array containing the bulbs to be pruinted</param>
        private static void PrintBulbs(Bulb[] bulbs)
        {
            foreach (Bulb bulb in bulbs)
                Console.Write(bulb + "   ");
        }
        
        /// <summary>
        /// Prints the buttons actions on its managed bulbs.
        /// </summary>
        private static void PrintButtonLabels()
        {
            Console.WriteLine("\n\nButton 1 (changes bulb 1 state)");    
            Console.WriteLine("Button 2 (switches bulb 1 state with bulb 2 state)");    
            Console.WriteLine("Button 3 (switches bulb 2 state with bulb 3 state)");    
        }
    }
}