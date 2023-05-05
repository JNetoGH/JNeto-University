namespace GameUnits
{
    public abstract class XPUnit: Unit
    {
        
        public int XP { get; protected set; }
        public override int Health { get; set; }
        
        protected XPUnit(int movement, int health) : base(movement, health)
        {
            XP = 0;
        }
        
        public override string ToString()
        {
            return $"{base.ToString()} XP={XP}";
        }
        
    }
}