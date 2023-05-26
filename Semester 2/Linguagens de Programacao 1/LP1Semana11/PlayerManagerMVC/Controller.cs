using System.Collections.Generic;

namespace PlayerManagerMVC
{
    public class Controller
    {
        private List<Player> list;
        private IView view;
        private IComparer<Player> compareByName;
        private IComparer<Player> compareByNameReverse;
        private PlayerOrder playerOrder;

        public Controller(List<Player> list)
        {
            this.list = list;

            compareByName = new CompareByName(true);
            compareByNameReverse = new CompareByName(false);
            playerOrder = PlayerOrder.ByScore;
        }

        public void Run(IView view)
        {
            int input;
            this.view = view;
            do
            {
                // 1 -> Insert player
                // 2 -> List all players
                // 3 -> List players w/ score > x
                // 4 -> Change player sorting criteria
                // 0 -> Exit
                input = view.MainMenu(playerOrder);

                switch (input)
                {
                    case 0:
                        break;
                    case 1:
                        InsertPlayer();
                        break;
                    case 2:
                        SortPlayers();
                        view.ShowPlayers(list);
                        break;
                    case 3:
                        SortPlayers();
                        ShowPlayersWithScore();
                        break;
                    case 4:
                        ChangePlayerOrder();
                        break;
                    default:
                        view.InvalidOption();
                        break;
                }
            }
            while (input != 0);
        }

        private void ChangePlayerOrder()
        {
            do
            {
                playerOrder = view.AskPlayerOrder();

                if (playerOrder < PlayerOrder.ByScore
                    || playerOrder > PlayerOrder.ByNameReverse)
                {
                    view.InvalidOption();
                }
                else
                {
                    break;
                }
            }
            while (true);
        }

        private void SortPlayers()
        {
            switch (playerOrder)
            {
                case PlayerOrder.ByScore:
                    list.Sort();
                    break;
                case PlayerOrder.ByName:
                    list.Sort(compareByName);
                    break;
                case PlayerOrder.ByNameReverse:
                    list.Sort(compareByNameReverse);
                    break;
            }
        }

        private void InsertPlayer()
        {
            // Ask view to give us information for creating a new player
            (string name, int score) = view.AskForPlayer();

            // Create new player
            Player p = new Player(name, score);

            // Insert new player in player list
            list.Add(p);
        }

        private void ShowPlayersWithScore()
        {
            // Ask view for minimum score
            int minScore = view.AskForMinimumScore();

            // Create collection with players above minimum score
            IEnumerable<Player> players =
                GetPlayersWithScoreGreaterThan(minScore);

            // Ask view to show players
            view.ShowPlayers(players);
        }

        private IEnumerable<Player> GetPlayersWithScoreGreaterThan(int minScore)
        {
            foreach (Player p in list)
            {
                if (p.Score > minScore)
                    yield return p;
            }
        }
    }
}