using System;
using System.Globalization;
using System.Net;

namespace VariasStrings {
    
    class Exec {
        
        private static void Main() {


            #region EXS 4 e 5

            Console.WriteLine();
            string verbatimPathLike = @"path\to\I\know\where";
            Console.WriteLine(verbatimPathLike + "\n");
            
            string strConcatenation1 = "your country is: " + RegionInfo.CurrentRegion.EnglishName;
            string strConcatenation2 = "your machine name is: " + Environment.MachineName;
            string strInterpolation1 = $"your IP is: {Dns.GetHostEntry(Dns.GetHostName()).AddressList[0]}";
            string strInterpolation2 = $"your name is: {Environment.UserName}";
            string strFormat1 = String.Format("your OS is: {0}", Environment.OSVersion);
            string strFormat2 = String.Format("this program location: {0}", AppDomain.CurrentDomain.BaseDirectory);
            
            Console.WriteLine(strConcatenation1);
            Console.WriteLine(strConcatenation2);
            Console.WriteLine(strInterpolation1);
            Console.WriteLine(strInterpolation2);
            Console.WriteLine(strFormat1);
            Console.WriteLine(strFormat2);
            
            // straight in console example
            Console.WriteLine("your machine is set to: " + CultureInfo.CurrentCulture.DisplayName);
            Console.WriteLine($"your calendar is set to: {CultureInfo.CurrentCulture.Calendar}\n");

            #endregion

            
            #region EX 6
            
            double xx = 0.12345;
            
            Console.WriteLine($"xx (F2) {xx:F2}");
            Console.WriteLine($"xx (P1) {xx:P1}");
            
            int ii = 18;
            Console.WriteLine($"\nii: {ii}(10) == {ii.ToString("X")}(16)");
            Console.WriteLine($"ii as money: {ii.ToString("C")}");
            
            #endregion
            
        }
        
 
       
    }
    
}