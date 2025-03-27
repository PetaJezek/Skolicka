using System;
using System.Collections.Generic;
namespace Maximu_value_in_a_sequence
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int elements = int.Parse(Console.ReadLine());
            int x = 0;
            int nejvetsi = int.MinValue;
            List<int> ints = new();
            while (true)
            {
                string s = "";
                int cur = Console.Read();
                while(cur != 32 && cur != 13 && cur != 10)
                {
                    s += Convert.ToChar(cur);
                    cur = Console.Read();
                }

                x++;

                if (int.Parse(s) > nejvetsi)
                {
                    nejvetsi = int.Parse(s);
                    ints.Clear();
                    ints.Add(x);
                }
                else if (int.Parse(s) == nejvetsi)
                {
                    ints.Add(x);
                }


                if (x == elements)
                {
                    break;
                }
            }
            Console.WriteLine(nejvetsi);

            for (int i = 0; i < ints.Count - 1; i++)
            {
                Console.Write(ints[i] + " ");
            }
            Console.Write(ints[ints.Count-1]);
        }
    }
}
