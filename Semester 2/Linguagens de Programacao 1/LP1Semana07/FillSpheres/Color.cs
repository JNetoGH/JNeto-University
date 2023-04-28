namespace FillSpheres
{
    public class Color
    {
        private byte _red = 0;
        private byte _blue = 0;
        private byte _green = 0;
        private byte _alpha = 0;
                            
        public Color(byte red, byte blue, byte green, byte alpha)
        {
            _red = red;
            _blue = blue;
            _green = green;
            _alpha = alpha;
        }

    
        public byte GetRed() => _red;
        public void SetRed(byte newValue) => _red = newValue;

        public byte GetBlue() => _blue;
        public void SetBlue(byte newValue) => _blue = newValue;
        
        public byte GetGreen() => _green;           
        public void SetGreen(byte newValue) => _green = newValue;

        public byte GetAlpha() => _alpha;           
        public void SetAlpha(byte newValue) => _alpha = newValue;
        
        public byte GetGrey() => (byte) ((_red + _blue + _red) / 3);
        
        public override string ToString() => $"r:{_red}, b:{_blue}, g:{_green}, a:{_alpha}";
    }
}