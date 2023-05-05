namespace GameUnits
{
    
    public class MilitaryUnit : XPUnit
    {
        
        private int movement;
        public int AttackPower { get; private set; }
        public override float Cost => AttackPower + XP;
        public override int Health 
        {
            get => base.Health + XP;
            set => base.Health = value;
        }

        public MilitaryUnit(int movement, int health, int attackPower) : base(movement, health)
        {
            this.AttackPower = attackPower;
        }

        public void Attack(Unit u)
        {
            this.XP++;
            u.Health--;
        }
        
        public override string ToString()
        {
            return $"{base.ToString()} AP={AttackPower}";
        }
        
    }
    
}