using System;
using System.Collections.Generic;

namespace LootSort
{
    public class Program
    {
        private static void Main()
        {
            // Set where we'll place the loot
            ISet<Loot> lootSet = new HashSet<Loot>();

            // We'll use this list later to sort the loot
            List<Loot> sorted;

            // Add various loot to the set
            lootSet.Add(new Loot(LootType.Ammo, "Powerful 45mm rounds", 12.5f));
            lootSet.Add(new Loot(LootType.Collectible, "Unique ruby", 500f));
            lootSet.Add(new Loot(LootType.Health, "Powerup +50HP", 7.5f));
            lootSet.Add(new Loot(LootType.Shield, "Powerup +75AP", 42.5f));
            lootSet.Add(new Loot(LootType.Weapon, "Colt Revolver", 83.75f));
            lootSet.Add(new Loot(LootType.Ammo, "Powerful 45mm rounds", 12.5f));
            lootSet.Add(new Loot(LootType.Ammo, "Powerful 45mm rounds", 12.5f));
            lootSet.Add(new Loot(LootType.Shield, "Powerup +75AP", 42.5f));
            lootSet.Add(new Loot(LootType.Weapon, "Colt Revolver", 83.75f));
            lootSet.Add(new Loot(LootType.Shield, "Powerup +25AP", 21.25f));
            lootSet.Add(new Loot(LootType.Weapon, "Colt Revolver", 67.25f));
            lootSet.Add(null);

            // Add all contents of the set to a list
            sorted = new List<Loot>(lootSet);

            // Sort the list
            // This will fail if the Loot class doesn't implement IComparable<Loot>)
            sorted.Sort();

            // Print the contents of the sorted loot list
            foreach (Loot loot in sorted)
            {
                // This will implicitly call loot.ToString()
                Console.WriteLine(loot);
            }

            // Expected output:
            //
            // [           Ammo]	12.50	Powerful 45mm rounds
            // [    Collectible]	500.00	Unique ruby
            // [         Health]	7.50	Powerup +50HP
            // [         Shield]	42.50	Powerup +75AP
            // [         Shield]	21.25	Powerup +25AP
            // [         Weapon]	83.75	Colt Revolver
            // [         Weapon]	67.25	Colt Revolver
        }
    }
}
