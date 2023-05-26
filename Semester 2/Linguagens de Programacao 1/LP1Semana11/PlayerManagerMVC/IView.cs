using System.Collections.Generic;

namespace PlayerManagerMVC
{
    public interface IView
    {
        int MainMenu(PlayerOrder playerOrder);

        void InvalidOption();

        void ShowPlayers(IEnumerable<Player> players);

        (string, int) AskForPlayer();

        int AskForMinimumScore();

        PlayerOrder AskPlayerOrder();
    }
}