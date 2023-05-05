namespace GameUnits
{
    public class DiplomatUnit: XPUnit
    {
        
        public override float Cost => 7.1f;
       
        public DiplomatUnit() : base(6, 1) { }

        public void MakeAgreement(Unit unit)
        {
            if (unit is DiplomatUnit) this.XP += 3;
            else if (unit is SettlerUnit) this.XP += 2;
            else this.XP ++;
        }
     
    }
}