using System;

namespace FillSpheres
{
    class Program
    {
        static void Main(string[] args)
        {

            Sphere[] spheres = new Sphere[3]
            {
                new Sphere(new Color(255, 0, 0, 255), 1.0f),
                new Sphere(new Color(0, 255, 0, 255), 5.0f),
                new Sphere(new Color(0, 0, 255, 255), 2.5f)
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
            
        }
    }
}