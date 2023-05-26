using System;

namespace GuessTheNumber
{
    public class View
    {
        
        public void PrintIntroduction()
        {
            Console.WriteLine("Welcome to Guess the Number!");
            Console.WriteLine("I have chosen a number between 1 and 100.");
        }

        public int ManageGuessMsg()
        {
            Console.Write("Take a guess: ");
            return Convert.ToInt32(Console.ReadLine());
        }

        public void PrintAttemptStateMsg(Model model)
        {
            switch (model.AttemptState)
            {
                case State.Right:
                    Console.WriteLine("Congratulations! You guessed the number correctly!");
                    Console.WriteLine("Number of attempts: " + model.Attempts);
                    return;
                case State.TooLow:
                    Console.WriteLine("Too low! Try again.");
                    return;
                case State.TooHigh:
                    Console.WriteLine("Too high! Try again.");
                    break;
            }
        }

        public void PrintLastMsg()
        {
            Console.WriteLine("Thank you for playing Guess the Number!");
        }
        
    }
}