using System.Collections.Generic;

namespace PlayerManager4
{
    public class CompareByName: IComparer<Player>
    {

        private bool _ascendantMode;
        
        public CompareByName(bool ascendantMode)
        {
            _ascendantMode = ascendantMode;
        }
        
        public int Compare(Player? x, Player? y)
        {
            List<Player> players = new List<Player>() { x, y };
            int comparison = x.Name.CompareTo(y.Name);
            
            if (comparison == 0)
                return 0;
            
            if (comparison == 1 )
            {
                if (_ascendantMode)
                    return 1;
                else
                    return -1;
            }
            
            if (_ascendantMode)
                return -1;
            else
                return 1;
            
        }
    }
}