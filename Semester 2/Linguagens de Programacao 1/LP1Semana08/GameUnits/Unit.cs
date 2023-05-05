using System;

namespace GameUnits
{
    public abstract class Unit
    {
        private int movement;
        public virtual int Health { get; set; }
        public abstract float Cost { get; }

        public Unit(int movement, int health)
        {
            this.movement = movement;
            Health = health;
        }

        public virtual void Move()
        {
            Console.WriteLine($"{this.movement}");
        }
        
        public override string ToString()
        {
            return $"{this.GetType().Name}: HP={Health} COST={Cost:F2}";
        }
    }
}