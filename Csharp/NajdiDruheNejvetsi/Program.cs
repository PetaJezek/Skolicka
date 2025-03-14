    namespace NajdiDruheNejvetsi 
    { 
        using System;
        using System.Linq;

        class Program
        {
            static void Main()
            {
                int[] numbers = (Console.ReadLine()??"")
                                    .Split()
                                    .Select(int.Parse)
                                    .ToArray();

                int largest = int.MinValue;
                int secondLargest = int.MinValue;

                foreach (int num in numbers)
                {
                    if (num == -1)
                        break;

                    if (num > largest)
                    {
                        secondLargest = largest;
                        largest = num;
                    }
                    else if (num > secondLargest && num != largest)
                    {
                        secondLargest = num;
                    }
                }

                Console.WriteLine(secondLargest);
            }
        }
    }