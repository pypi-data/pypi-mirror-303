                PRACTICAL NO.01

1.Working with basic C# and ASP .NET 
a. Create an application that obtains four int values from the user and displays the product
CODE:
using System;
class Demo
{
    static void Main()
    {
        Console.WriteLine("Enter Four Integer Values ");
        Console.WriteLine("Enter First Number :");
        int n1 = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Enter Second Number :");
        int n2 = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Enter Third Number :");
        int n3 = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Enter Fourth Number :");
        int n4 = Convert.ToInt32(Console.ReadLine());
        int sp = n1 * n2 * n3 * n4;
        Console.WriteLine("The Product of Given Number is  :" + sp);
}
}








b. Create an application to demonstrate string operations

using System;
class Demo
{
    static void Main()
    {
        string s1 = "New";
        string s2 = "World";
        string cs = s1 + " " + s2;
        Console.WriteLine("Concatinated String : " + cs);
        Console.WriteLine("Length of the String : " + s1.Length);
        string ss = cs.Substring(0, 3);
        Console.WriteLine("Substring : " + ss);
        int indx = cs.IndexOf("World");
        Console.WriteLine("Index of  : " + indx);
        string rs = cs.Replace("New", "Hello");
        Console.WriteLine("Replace string : " + rs);
    }
}







c. Create an application that receives the (Student Id, Student Name, Course Name, Date of Birth) information from a set of students. The application should also display the information of all the students once the data entered
CODE:
using System;
class Program
{
    static void Main()
    {
        List<Student> students = new List<Student>();

        while (true)
        {
            Console.WriteLine("Enter student information or type 'quit' to exit:");

            Console.Write("Student Id: ");
            string id = Console.ReadLine();

            if (id.ToLower() == "quit")
                break;

            Console.Write("Student Name: ");
            string name = Console.ReadLine();

            Console.Write("Course Name: ");
            string course = Console.ReadLine();

            Console.Write("Date of Birth (dd/mm/yyyy): ");
            string dob = Console.ReadLine();
            Student student = new Student(id, name, course, dob);
            students.Add(student);

            Console.WriteLine("Student added successfully.\n");
        }

        Console.WriteLine("\nList of Students:");
        foreach (var student in students)
        {
            Console.WriteLine($"Student Id: {student.Id}");
            Console.WriteLine($"Student Name: {student.Name}");
            Console.WriteLine($"Course Name: {student.Course}");
            Console.WriteLine($"Date of Birth: {student.DOB}\n");
        }

        Console.ReadLine();
    }
    class Student
    {
        public string Id;
        public string Name;
        public string Course;
        public string DOB;
        public Student(string id, string name, string course, string dob)
        {
            Id = id;
            Name = name;
            Course = course;
            DOB = dob;
        }
    }
}





















d. Create an application to demonstrate following operations 
i. Generate Fibonacci series
ii. Test for prime numbers
iii. Test for vowels
iv. Use of foreach loop with arrays 
v. Reverse a number and find sum of digits of a number
CODE:

using System;
class Programx
{
    static void Main()
    {
        //  Generate Fibonacci series
        Console.WriteLine("Fibonacci Series:");
        GenerateFibonacci(10);

        // Test for prime numbers
        Console.WriteLine("\nPrime Numbers:");
        TestPrimeNumbers(10);

        // Test for vowels
        Console.WriteLine("\nVowels:");
        TestVowels("Hello World");

        //  Use of foreach loop with arrays
        Console.WriteLine("\nForeach Loop with Arrays:");
        string[] value = { "YASH", "ROHIT", "VIRAJ" };
        foreach (var v in value)
        {
            Console.WriteLine(v);
        }

        //  Reverse a number and find sum of digits of a number
        Console.WriteLine("\nReverse and Sum of Digits:");        
 int number = 12345;
        int reversedNumber = ReverseNumber(number);
        Console.WriteLine($"Reversed number of {number} is: {reversedNumber}");
        int sumOfDigits = SumOfDigits(number);
        Console.WriteLine($"Sum of digits of {number} is: {sumOfDigits}");
        Console.ReadLine();
  
 }
    static void GenerateFibonacci(int count)
    {
        int a = 0, b = 1;
        for (int i = 0; i < count; i++)
        {
            Console.Write(a + " ");
            int temp = a;
            a = b;
            b = temp + b;
        }
    }
    static void TestPrimeNumbers(int n)
    {
        for (int i = 2; i <= n; i++)
        {
            bool isPrime = true;
            for (int j = 2; j < i; j++)
            {
                if (i % j == 0)
                {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime)
                Console.Write(i + " ");
        }
    }
    static void TestVowels(string str)
    {
        List<char> vowels = new List<char> { 'a', 'e', 'i', 'o', 'u' };
        foreach (char c in str.ToLower())
        {
            if (vowels.Contains(c))
                Console.Write(c + " ");
        }
    }
    static int ReverseNumber(int number)
    {
        int reversed = 0;
        while (number > 0)
        {
            int remainder = number % 10;
            reversed = reversed * 10 + remainder;
            number = number / 10;
        }
        return reversed;
    }
    static int SumOfDigits(int number)
    {
        int sum = 0;
        while (number > 0)
        {
         

   	int digit = number % 10;
            sum += digit;
            number = number / 10;
        }
        return sum;
    }
}










