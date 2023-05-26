using System.Collections.Generic;

namespace PlayerManagerMVC
{
    public class CompareByName : IComparer<Player>
    {
        private bool ord;

        public int Compare(Player p1, Player p2)
        {
            if (p1 == p2) return 0;
            if (p1 is null) return -1;
            if (p2 is null) return 1;

            if (ord)
                return p1.Name.CompareTo(p2.Name);
            else
                return p2.Name.CompareTo(p1.Name);
        }

        public CompareByName(bool ord)
        {
            this.ord = ord;
        }
    }
}