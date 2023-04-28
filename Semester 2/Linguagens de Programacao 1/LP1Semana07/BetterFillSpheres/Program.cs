using System;

namespace BetterFillSpheres
{
    class Program
    {
        
        static void Main(string[] args)
        {

            Sphere[] spheres = new Sphere[3]
            {
                new Sphere( new Color { Red = 255, Green = 0, Blue = 0, Alpha = 255 }, 1f),
                new Sphere( new Color { Red = 0, Green = 255, Blue = 0, Alpha = 255 }, 1.25f),
                new Sphere( new Color { Red = 0, Green = 0, Blue = 255, Alpha = 255 }, 3.2f)
            };

            Console.WriteLine("\nSPHERES:");
            foreach (Sphere sphere in spheres)
                Console.WriteLine(sphere);

            // play around with spheres
            spheres[0].Throw();
            spheres[1].Throw();
            spheres[1].Pop();
            spheres[2].Throw();
            spheres[2].Throw();

            Console.WriteLine("\nplay around with spheres\n");

            Console.WriteLine("SPHERES:");
            foreach (Sphere sphere in spheres)
                Console.WriteLine(sphere);

            int chosen = 1;
            Console.WriteLine($"\nChecking color of sphere {chosen}: ");
            Console.WriteLine($"{spheres[chosen].Color.Name}");

        }
    }
}