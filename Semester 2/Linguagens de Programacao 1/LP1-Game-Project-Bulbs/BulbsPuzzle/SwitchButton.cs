using BulbsPuzzle.Interfaces;

namespace BulbsPuzzle
{
    /// <summary>
    /// Can hold two bulbs, and can switch their state between each other
    /// </summary>
    class SwitchButton: IBulbButton
    {
        // Holds the managed bulbs.
        private Bulb _bulb1;
        private Bulb _bulb2;
        
        /// <summary>
        /// It's the class constructor.
        /// </summary>
        /// <param name="bulb1">first bulb to be managed by this button</param>
        /// <param name="bulb2">second bulb to be managed by this button</param>
        public SwitchButton(Bulb bulb1, Bulb bulb2)
        {
            _bulb1 = bulb1;
            _bulb2 = bulb2;
        }
        
        // Interface Method
        public void Press()
        {
            if (_bulb1.State == _bulb2.State)
                return;
            _bulb1.SwitchState();
            _bulb2.SwitchState();
        }
    }
}