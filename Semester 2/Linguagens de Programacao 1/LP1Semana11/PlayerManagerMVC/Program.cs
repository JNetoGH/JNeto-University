using System.Collections.Generic;

namespace PlayerManagerMVC
{
    public class Program
    {
        private static void Main()
        {
            // List of player is our model
            List<Player> list = new List<Player>()
            {
                new Player("Pedro", 50),
                new Player("Verde", 42),
            };

            // Create controller
            Controller controller = new Controller(list);

            // Create view
            IView view = new UglyView(controller);

            // Start program
            controller.Run(view);
        }
    }
}
