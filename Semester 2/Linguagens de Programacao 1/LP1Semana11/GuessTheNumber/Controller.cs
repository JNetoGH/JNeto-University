namespace GuessTheNumber
{
    public class Controller
    {
        private View _view;
        private Model _model;

        public Controller(View view, Model model)
        {
            _view = view;
            _model = model;
        }

        public void RunGame()
        {
            _view.PrintIntroduction();
            _model.GenerateNewTargetNumber();
            RunGameLoop();
            _view.PrintLastMsg();
        }
        
        private void RunGameLoop()
        {
            while (_model.AttemptState != State.Right)
            {
                _model.Guess = _view.ManageGuessMsg();
                _model.Attempts++;
                _view.PrintAttemptStateMsg(_model);
            }
        }
        
    }
}