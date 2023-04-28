namespace BetterFillSpheres
{
    public class Color
    {
        public byte Red { get; set; } = 0;
        public byte Green { get; set; } = 0;
        public byte Blue { get; set; } = 0;
        public byte Alpha { get; set; } = 0;
        public byte Grey => (byte)((Red + Blue + Red) / 3);
        public string Name => this switch
        {
            { Red: 255, Green: 0, Blue: 0 } => "Red 100%",
            { Red: 0, Green: 255, Blue: 0 } => "Green 100%",
            { Red: 0, Green: 0, Blue: 255 } => "Blue 100%",
            _ => "Mixed"
        };

        public Color() { }
        public Color(byte red,  byte green, byte blue, byte alpha)
        {
            Red = red;
            Green = green;
            Blue = blue;
            Alpha = alpha;
        }
        
        public override string ToString() => $"r:{Red}, g:{Green}, b:{Blue}, a:{Alpha}, grey:{Grey}";
    }
}