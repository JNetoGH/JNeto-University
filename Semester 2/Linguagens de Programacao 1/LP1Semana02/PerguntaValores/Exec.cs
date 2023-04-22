using System;

namespace PerguntaValores {

    class Cylinder {
        
        // AND VARIABLES
        private double _height = 0;
        private double _radius = 0;
       
        // PROPERTIES
        /// <summary> Cylinder volume formula: π * pow(r) * h </summary>
        private double Volume => Math.PI * Math.Pow(_radius, 2) * _height; 
        /// <summary> Cylinder Surface Area formula: 2πr(r + h) </summary> 
        private double SurfaceArea => 2 * Math.PI * _radius * (_radius + _height); 
        
        public Cylinder(double height, double radius) {
            this._height = height;
            this._radius = radius;
        }
        
        public override string ToString() {
            return $"height: {_height} \n" +
                   $"radius: {_radius} \n" +
                   $"volume: {Volume} \n" +
                   $"surface area: {SurfaceArea}";
        }
    }
    
    class Exec {
        static void Main(string[] args) {
            
            Console.Write("\ninsert height: ");
            double height = double.Parse(Console.ReadLine());
            Console.Write("insert radius: ");
            double ray = double.Parse(Console.ReadLine());

            Cylinder cylinder = new Cylinder(height, ray);
            Console.WriteLine("\n" + cylinder.ToString());
            
        }
    }
    
}