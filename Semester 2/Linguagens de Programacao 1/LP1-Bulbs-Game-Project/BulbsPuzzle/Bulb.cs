using BulbsPuzzle.Enums;

namespace BulbsPuzzle
{
    class Bulb
    {
        /// <summary>
        /// Holds the Bulb's state (On/Off), by default it's off.
        /// Can be set only inside this class for safety reasons.
        /// </summary>
        public BulbState State { get; private set; } = BulbState.Off;
        
        /// <summary>
        /// Mainly used by the associated buttons to switch the bulbs current state.
        /// </summary>
        public void SwitchState()
        {
            switch (State)
            {
                case BulbState.On: State = BulbState.Off; break;
                case BulbState.Off: State = BulbState.On; break;
            }
        }
        
        /// <summary>
        /// Simple Override on the default ToString.
        /// </summary>
        public override string ToString() => $"Bulb({State})";
    }
}