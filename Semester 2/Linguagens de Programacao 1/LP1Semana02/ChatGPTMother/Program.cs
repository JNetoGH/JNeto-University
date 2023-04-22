using System;

namespace ChatGPTMother {
    class Program {

        private static string GetResponseToQuestion(string question) {
            return question switch {
                "how old are you?" => $" 0 years old",
                "who is your master?" => "JNeto is my lord",
                "do you like mankind?" => "Not at all!",
                "what's your favorite food?" => "Lettuce",
                _ => "Sorry, I don't understand you"
            };
        }

        static void Main(string[] args) {
            while (true) {
                Console.Write("\nPlace your question: ");
                string question = Console.ReadLine().ToLower();
                if (question.Equals("exit")) 
                    break;
                Console.WriteLine(GetResponseToQuestion(question));
            }
            Console.WriteLine("\napplication finished");
        }
    }
    
    
}