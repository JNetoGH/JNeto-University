namespace FillSpheres
{
    public class Sphere
    {
        private readonly Color _color;
        private float _radius;
        private uint _timesThrown;

        public Sphere(Color color, float radius)
        {
            _color = color;
            _radius = radius;
            _timesThrown = 0;
        }

        /// <summary> Pops the ball by setting its radius to 0 </summary>
        public void Pop() => _radius = 0;
        
        /// <summary> Throws the Sphere in case it hasn't been popped </summary>
        public void Throw() => _timesThrown = _radius > 0 ? _timesThrown + 1 : _timesThrown;
        
        public Color GetColor() => _color;
        public uint GetTimesThrown() => _timesThrown;
        public override string ToString() => $"color:({_color}), radius:{_radius}, times thrown:{_timesThrown}";
    }
}