using BulbsPuzzle.Interfaces;

namespace BulbsPuzzle
{
    /// <summary>
    /// Can hold only one bulb, and can change this bulb's state.
    /// </summary>
    class SimpleButton: IBulbButton
    {
        // Holds the managed bulb.
        private Bulb _bulb;
        
        /// <summary>
        /// It's the class constructor.
        /// </summary>
        /// <param name="bulb">The bulb to be managed by this button.</param>
        public SimpleButton(Bulb bulb) => _bulb = bulb;
        
        // Interface Method
        public void Press() => _bulb.SwitchState();
    }
}