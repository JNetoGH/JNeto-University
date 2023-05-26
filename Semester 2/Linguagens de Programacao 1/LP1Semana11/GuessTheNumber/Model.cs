using System;

namespace GuessTheNumber
{
    public enum State
    {
        TooLow,
        TooHigh,
        Right,
        None
    }
    
    public class Model
    {
        private Random _random = new Random(); 
        private int _targetNumber = 0;  // between 1 and 100
        public int Attempts { get; set; } = 0;
        public int Guess { get; set; } = 0;
        public State AttemptState
        {
            get
            {
                if (Guess < _targetNumber) return State.TooLow;
                if (Guess > _targetNumber) return State.TooHigh;
                if (Attempts > 0) return State.Right;
                return State.None;
            }
        }
        
        public void GenerateNewTargetNumber()
        {
            _targetNumber = _random.Next(1, 101); 
        }
        
    }
}