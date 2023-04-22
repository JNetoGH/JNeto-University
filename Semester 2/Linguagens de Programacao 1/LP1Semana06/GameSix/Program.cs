using System;

namespace GameSix
{
    public class Program
    {
        
        public static void Main(string[] args)
        {
            
            Foe test = new Foe("Test");
            test.PickPowerUp(PowerUp.Shield, 1333);
            Console.WriteLine(test + "\n");

            Console.WriteLine(Foe.GetTotalPowerUpsGathered());
            
            int size = GetValidatedNumberFromUSer("Total of enemies: ", 
                "Please insert a number bigger than 0", 
                (i => i > 0 ));
            Foe[] foes = new Foe[size];
            for (int i = 0; i < foes.Length; i++)
            {
                Console.Write($"Please insert a name to Foe number {i+1}: ");
                foes[i] = new Foe(Console.ReadLine());
                
            }
            foreach (Foe foe in foes)
                Console.WriteLine(foe.GetName());
            
            Console.WriteLine("Thank you for using the program!");

        }

        private static int GetValidatedNumberFromUSer(string inputMsg, string errorMsg, Predicate<int> validation)
        {
            while (true)
            {
                try
                {
                    Console.Write(inputMsg);
                    int num = int.Parse(Console.ReadLine());
                    if (!validation.Invoke(num))
                        throw new Exception();
                    return num;
                }
                catch (Exception e)
                {
                    Console.WriteLine(errorMsg+"\n");
                }
            }
        }
        
    }
}