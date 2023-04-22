using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PlayerPerks {

    [Serializable]
    public class PerkKeyNotFoundException : Exception {
        public PerkKeyNotFoundException() : base("Unknown perk!") { }
    }
    
    [Serializable]
    public class PlayerInitializedWithNoPerks : Exception {
        public PlayerInitializedWithNoPerks() : base("No perks at all!") { }
    }
    
    [Flags]
    public enum Perks {
        WaterBreathing = 1 << 0, 
        Stealth = 1 << 1,
        AutoHeal = 1 << 2, 
        DoubleJump = 1 << 3
    }
    
    public class Player {
        
        private Perks _ownedPerks;
        
        public readonly Dictionary<char, Perks> _possiblePerks = new Dictionary<char, Perks>() {
            { 'a', Perks.AutoHeal}, { 'w', Perks.WaterBreathing },
            { 's', Perks.Stealth }, { 'd', Perks.DoubleJump }
        };
        
        public Player(string initialPerks) {
            if (initialPerks.Equals(string.Empty)) throw new PlayerInitializedWithNoPerks();
            AddPerkFromString(initialPerks);
        }

        public void AddPerkFromString(string str) {
            foreach (char key in str) {
                int totAppearances = str.Count(letter => letter == key);
                if (totAppearances % 2 == 0) continue; // when even appearances, do not add the perk
                AddPerkFromKey(key);
            }
        }
        
        public void AddPerkFromKey(char key) {
            if (!_possiblePerks.ContainsKey(key)) throw new PerkKeyNotFoundException();
            _ownedPerks |= _possiblePerks[key];
        }
        
        public override string ToString() {
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.AppendLine($"perks: {_ownedPerks}");
            if ((_ownedPerks & Perks.Stealth) == Perks.Stealth && (_ownedPerks & Perks.DoubleJump) == Perks.DoubleJump)
                stringBuilder.AppendLine("Silent jumper!");
            if (!((_ownedPerks & Perks.AutoHeal) == Perks.AutoHeal))
                stringBuilder.AppendLine("Not gonna make it!");
            return stringBuilder.ToString();
        }
    }
    
    public class Program {
        static void Main(string[] args) {
            
            Player? p = null;

            try {
                if (args.Length == 0) {
                    p = new Player("");
                    return;
                }
                p = new Player(args[0]);
            }
            catch (PerkKeyNotFoundException e) {
                Console.WriteLine(e.Message);
                return;
            }
            catch (PlayerInitializedWithNoPerks e) {
                Console.WriteLine(e.Message);
                return;
            }
        
            Console.WriteLine(p);
        }
    }
}