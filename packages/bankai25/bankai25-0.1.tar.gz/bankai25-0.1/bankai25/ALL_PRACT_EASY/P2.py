                        PRACTICAL NO.02

2. Working with Object Oriented C# and ASP .NET 
a. Create simple application to perform following operations 
i. Finding factorial Value
ii. Money Conversion 
iii. Quadratic Equation 
iv. Temperature Conversion 
CODE:

using System;
namespace ConsoleApp1
{
    class Program
    {
        static void fact()
        {
            Console.Write("Enter a number to find factorial: ");
            int n = Convert.ToInt32(Console.ReadLine());
            if (n == 0 || n == 1)
                n = 1;
            long fact = 1;
            for (int i = 2; i <= n; i++)
            {
                fact *= i;
            }
            Console.WriteLine($"Factorial of {n} is: {fact}");

            Console.ReadLine();
        }
        static void mconvert()
        {
            Console.Write("Enter amount in USD: ");
            decimal usd = Convert.ToDecimal(Console.ReadLine());

            decimal convertedAmount = ConvertToINR(usd);

            Console.WriteLine($"Amount in INR: {convertedAmount}");

            Console.ReadLine();
        }
        static decimal ConvertToINR(decimal usd)
        {
            decimal conversionRate = 79;
            return usd * conversionRate;
        }
        static void qequation()
        {
            Console.WriteLine("Enter coefficients (a, b, c) of the quadratic equation ax^2 + 	bx + c = 0:");
            Console.Write("Enter a: ");
            double a = Convert.ToDouble(Console.ReadLine());
            Console.Write("Enter b: ");
            double b = Convert.ToDouble(Console.ReadLine());
            Console.Write("Enter c: ");
            double c = Convert.ToDouble(Console.ReadLine());
            double discriminant = b * b - 4 * a * c;
            if (discriminant > 0)
            {
                double root1 = (-b + Math.Sqrt(discriminant)) / (2 * a);
                double root2 = (-b - Math.Sqrt(discriminant)) / (2 * a);

                Console.WriteLine($"Roots are real and different.\nRoot1 = {root1},Root2 = 	{ root2} ");
            }
            else if (discriminant == 0)
            {
                double root = -b / (2 * a);
                Console.WriteLine($"Roots are real and same.\nRoot = {root}");
            }
            else
            {
                double realPart = -b / (2 * a);
                double imaginaryPart = Math.Sqrt(-discriminant) / (2 * a);
                Console.WriteLine($"Roots are complex.\nRoot1 = {realPart} + 			   {imaginaryPart}i, 	Root2 = {realPart} - {imaginaryPart}i");
            }

            Console.ReadLine();
        }
        static void temp()
        {
            Console.Write("Enter temperature in Celsius: ");
            double celsius = Convert.ToDouble(Console.ReadLine());
            double fahrenheit = celsius * 9 / 5 + 32;
            double kelvin = celsius + 273.15;
            Console.WriteLine($"Temperature in Fahrenheit: {fahrenheit}");
            Console.WriteLine($"Temperature in Kelvin: {kelvin}");
            Console.ReadLine();
        }

        static void Main(string[] args)
        {
            Console.WriteLine("1-Find Factorial");
            Console.WriteLine("2-Money Conversion");
            Console.WriteLine("3-Solve Quadratic Equation");
            Console.WriteLine("4-Temperature Conversion");
            Console.WriteLine("Select Operation to perform :");
            int c = Convert.ToInt32(Console.ReadLine());
            switch (c)
            {
                case 1:
                    fact();
                    break;
                case 2:
                    mconvert();
                    break;
                case 3:
                    qequation();
                    break;
                case 4:
                    temp();
                    break;
                default:
                    Console.WriteLine("Invalid Option Selected");
                    break;
            }

        }
    }
}


OUTPUT:




b. Create simple application to demonstrate use of following concepts 
i. Function Overloading 
ii. Inheritance (all types) 
iii. Constructor overloading 
iv. Interfaces
CODE:
using System;
namespace ConsoleApp1
{
    public class Animal
    {
        public string Name;

        public Animal(string name)
        {
            Name = name;
        }
        public void Eat()
        {
            Console.WriteLine($"{Name} is eating.");
        }
    }
    public class Dog : Animal
    {
        public Dog(string name) : base(name)
        {
        }
        public void Shout()
        {
            Console.WriteLine($"{Name} Shout");
        }
    }
    public interface FLY
    {
        void Fly();
    }
    public interface SWIM
    {
        void Swim();
    }
    public class Duck : Animal, FLY, SWIM
    {
        public Duck(string name) : base(name)
        {
        }

        public void Fly()
        {
            Console.WriteLine($"{Name} is flying.");
        }

        public void Swim()
        {
            Console.WriteLine($"{Name} is swimming.");
        }
    }
    public class Hen : Animal
    {
        public Hen(string name) : base(name)
        {
        }
    }
    public class LION : Dog
    {
        public LION(string name) : base(name)
        {
        }
    }
    class Program3
    {

        static void Calculate(int num)
        {
            Console.WriteLine($"Square of {num} is: {num * num}");
        }
        static void Calculate(int num1, int num2)
        {
            Console.WriteLine($"Sum of {num1} and {num2} is: {num1 + num2}");
        }
        static void Main()
        {

            //function overloading
            Console.WriteLine(" Function Overloading");
            Calculate(5);
            Calculate(5, 3);

            Console.WriteLine();
            Console.WriteLine("Inheritance");
            Console.WriteLine("Single Level Inheritance");
            Console.WriteLine();
            //single inheritance
            Dog dog = new Dog("Rocky");
            dog.Eat();
            dog.Shout();
            Console.WriteLine();
            Console.WriteLine("Multiple  Inheritance");
            Console.WriteLine();
            // Multiple inheritance 
            Duck duck = new Duck("Ric");
            duck.Eat();
            duck.Fly();
            duck.Swim();
            Console.WriteLine("Multi Level Inheritance");
            Console.WriteLine();
            //Multilevel inheritance
            LION l = new LION("Sage");
            l.Shout();
            l.Eat();
            Console.WriteLine("Heirarchical Inheritance");
            Console.WriteLine();
            //Heirarchical inheritance
            Hen h = new Hen("Ben");
            h.Eat();

            Console.WriteLine("Interface Implimentation");
            Console.WriteLine();
            //interfaces
            Audi audiCar = new Audi();
            audiCar.Start();
            audiCar.Stop();
            Console.WriteLine("Constructor Overloading");
            Console.WriteLine();
            //constructor overloading
            Employee emp1 = new Employee("Vasant", 30000);
            emp1.Display();

            Employee emp2 = new Employee("Om");
            emp2.Display();
            Console.ReadLine();
        }
    }
    class Employee
    {
        public string Name;
        public decimal Salary;
        public Employee(string name, decimal salary)
        {
            Name = name;
            Salary = salary;
        }
        public Employee(string name)
        {
            Name = name;
            Salary = 0;
        }
        public void Display()
        {
            Console.WriteLine($"Name: {Name}, Salary: {Salary:C}");
        }
    }
    // Interface
    interface ICar
    {
        void Start();
        void Stop();
    }

    class Audi : ICar
    {
        public void Start()
        {
            Console.WriteLine("Audi car started.");
        }

        public void Stop()
        {
            Console.WriteLine("Audi car stopped.");
        }
    }
}
OUTPUT:
































c. Create simple application to demonstrate use of following concepts 
i. Using Delegates and events ii. Exception handling 
CODE:
using System;
class Program
{
    public delegate void EH(string msg);
    public static event EH OnNotify;
    static void Main()
    {
          OnNotify += DM;
        try
        {
            Console.Write("Enter a number: ");
            int num = Convert.ToInt32(Console.ReadLine());

            if (num < 0)
            {
                OnNotify?.Invoke("Number is Negative");
            }
            else
            {

                OnNotify?.Invoke("Number is Positive");
            }

            Console.Write("Enter a number 1: ");
            int num1 = Convert.ToInt32(Console.ReadLine());
            Console.Write("Enter a number 2: ");
            int num2 = Convert.ToInt32(Console.ReadLine());
            int res = num1 / num2;
            Console.WriteLine($"Result of Division of n1 : {num1} and n2 :{num2} is: 	{res}");
        }
        catch (FormatException)
        {
            OnNotify?.Invoke("Invalid input format");
        }
        catch (DivideByZeroException)
        {
            OnNotify?.Invoke("Cannot be diveded by zero");
        }
        catch (Exception ex)
        {
            OnNotify?.Invoke($"Error Occured: {ex.Message}");
        }

        Console.ReadLine(); 
    }

    static void DM(string msg)
    {
        Console.WriteLine($"Notification: {msg}");
    }
}


OUTPUT:
