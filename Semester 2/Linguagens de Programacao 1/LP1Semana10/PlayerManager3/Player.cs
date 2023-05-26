using System;

namespace PlayerManager3
{
    public class Player: IComparable<Player>
    {
        public string Name { get; }
        public int Score { get; }
        
        public Player(string name, int score)
        {
            Name = name;
            Score = score;
        }
        
        public int CompareTo(Player? other)
        {
            if (other.Score == Score)
                return 0;
            if (other.Score < Score)
                return -1;
            return 1;
        }
    }
}
