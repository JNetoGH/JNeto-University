using System;

namespace PlayerAchievements {
    
    [Flags]
    public enum Achievement {
        DefeatOptionalBoss = 1 << 0,
        FindHiddenLevel = 1 << 1,
        FinishGame = 1 << 2
    }
    
    class Program {
        
        static void Main(string[] args) {
            
            int totalOfPlayers = int.Parse(WriteAndRead("\nInsert the total of players: "));
            Achievement[] achievementsArray = new Achievement[totalOfPlayers];
    
            for (int i = 0; i < totalOfPlayers; i++) {
                Console.WriteLine($"\nPlayer {i} Achievements Setup");
                foreach (Achievement availableAchievement in Enum.GetValues(typeof(Achievement))) 
                    if (WriteAndRead($"Add {availableAchievement} (Y/N): ").ToUpper().Equals("Y")) 
                        achievementsArray[i] |= availableAchievement;
            }
            
            Console.WriteLine();
            for (int i = 0; i < totalOfPlayers; i++) {
                Console.WriteLine($"\nPlayer {i} Achievements Display \n{achievementsArray[i]}");
                if (HasAchievements(achievementsArray[i], Enum.GetValues(typeof(Achievement)) as Achievement[])) 
                    Console.WriteLine("Completionist!");
            } 

        }

        private static bool HasAchievements(Achievement collection, Achievement[] checks) {
            foreach (Achievement check in checks) 
                if ((collection & check) != check) 
                    return false;
            return true;
        }
        
        private static string WriteAndRead(string str) {
            Console.Write(str);
            return Console.ReadLine();
        }
        
    }
}