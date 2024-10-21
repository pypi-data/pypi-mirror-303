                    PRACTICAL NO.05
Write the program for the following: 
a.Create an application to print on screen the output of adding, subtracting, multiplying and 
dividing two numbers entered by the user in C#
CODE:
using System;
namespace BasicOperation
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the first number:");
            double num1 = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter the second number:");
            double num2 = Convert.ToDouble(Console.ReadLine());
            double sum = num1 + num2;
            double difference = num1 - num2;
            double product = num1 * num2;
            double quotient = num1 / num2;
            Console.WriteLine($"Addition : {sum}");
            Console.WriteLine($"Subtraction : {difference}");
            Console.WriteLine($"Multiplication : {product}");
            Console.WriteLine($"Division : {quotient}");
            Console.ReadLine();
        }
    }
}
   
OUTPUT:
 

b.Create an application to print Floyd’s triangle till n rows in C#
CODE:
using System;
namespace BasicOperation
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the number of rows :");
            int n = Convert.ToInt32(Console.ReadLine());

            int number = 1; 
            for (int i = 1; i <= n; i++)
            {
                for (int j = 1; j <= i; j++)
                {
                    Console.Write(number + " ");
                    number++;
                }
                Console.WriteLine(); 
            }
            Console.ReadLine();
        }

    }
}
   
OUTPUT:


c.Create an application to demonstrate following operations i. Generate Fibonacci series. ii. Test 
for prime numbers.

CODE:
using System;
namespace NumberOperations
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Choose an operation:");
            Console.WriteLine("1. Generate Fibonacci series");
            Console.WriteLine("2. Test for prime numbers");
            int choice = Convert.ToInt32(Console.ReadLine());

            switch (choice)
            {
                case 1:
                    GenerateFibonacciSeries();
                    break;
                case 2:
                    TestPrimeNumbers();
                    break;
                default:
                    Console.WriteLine("Invalid choice");
                    break;
            }

            Console.ReadLine();
        }

        static void GenerateFibonacciSeries()
        {
            Console.WriteLine("Enter the number for the Fibonacci series :");
            int n = Convert.ToInt32(Console.ReadLine());

            int n1 = 0, n2 = 1, nx;

            Console.WriteLine("Fibonacci series:");
            Console.Write(n1 + " " + n2 + " ");

            for (int i = 2; i < n; i++)
            {
                nx = n1 + n2;
                Console.Write(nx + " ");
                n1 = n2;
                n2 = nx;
            }
            Console.WriteLine();
        }

        static void TestPrimeNumbers()
        {
            Console.WriteLine("Enter a number to check prime:");
            int number = Convert.ToInt32(Console.ReadLine());

            if (IsPrime(number))
            {
                Console.WriteLine($"{number} is a prime number.");
            }
            else
            {
                Console.WriteLine($"{number} is not a prime number.");
            }
        }
        static bool IsPrime(int number)
        {
            if (number <= 1)
            {
                return false;
            }

            for (int i = 2; i < number; i++)
            {
                if (number % i == 0)
                {
                    return false;
                }
            }
            return true;
        }
    }
}



OUTPUT:




