using System;
using System.Collections.Generic;

namespace GameSixFriday
{
    public class GameLevel
    {
        private struct Room
        {
            public int adress;
            public List<Foe> foes;
            public Room(int adress) : this()
            {
                this.adress = adress;
                foes = new List<Foe>();
            }
            public override string ToString() => $"Room {adress}: {string.Join(',', foes)}";
        }

        private int totalRooms;
        private Difficulty difficulty;
        private static int totFoes;
        private Room[] rooms;
        
        public GameLevel(int totalRooms, Difficulty difficulty)
        {
            this.totalRooms = totalRooms;
            this.difficulty = difficulty;
            this.rooms = new Room[totalRooms];
            for (int i = 0; i < totalRooms; i++)
                this.rooms[i] = new Room(i);
        }

        public void SetFoeInRoom(int roomAddress, Foe foe)
        {
            rooms[roomAddress].foes.Add(foe);
            totFoes += 1;
        }

        public Difficulty GetDifficulty() => this.difficulty;
        public int GetNumRooms() => this.totalRooms;
        public int GetNumFoes() => totFoes;

        public void PrintFoes()
        {
            for (int i = 0; i < totalRooms; i++)
            {
                if (rooms[i].foes.Count == 0)
                    continue;
                Console.WriteLine($"{rooms[i]}");
            }
        }
    }
}