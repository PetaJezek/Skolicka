using System.Collections.Generic;
using System;
using System.Runtime.ConstrainedExecution;

namespace NextPermutation
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int pocet = int.Parse(Console.ReadLine());
            List<int> ints = new();
            int id = 0;
            while (ints.Count != pocet)
            {
                string s = "";
                int cur = Console.Read();

                while (cur != 32 && cur != 13 && cur != 10)
                {
                    s += Convert.ToChar(cur);
                    cur = Console.Read();

                }

                ints.Add(int.Parse(s));

            }


            for (int i = pocet; i > 0; i--)
            {
                if (ints[i-1] != pocet - i + 1)
                {
                    id = i;
                    break;
                }
            }
            if(id != 0) { 
            int prohazovanec = ints[id-1];
            for (int i = id; i > 0; i--)
            {
                if (ints[i - 1] < prohazovanec)
                {
                    int temp = ints[i - 1];
                    ints[i - 1] = prohazovanec;
                    ints.RemoveAt(id - 1);
                    ints.Add(temp);
                    ints.Sort(i, pocet - i , null);
                    break;
                }
            }
            for (int i = 0; i < pocet - 1; i++)
            {
                Console.Write(ints[i] + " ");
            }
            Console.Write(ints[pocet - 1]);
            }
            else
            {
                Console.WriteLine("NEEXISTUJE");
            }



        }
    }
}
