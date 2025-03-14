using System;





namespace ConsoleApp1

{

    public class Program
    {
        public static void Main(string[] args)
        {
            long cur = 0;
            long snd = int.MinValue;
            long max = int.MinValue;
            bool running = true;
            while (running)
            {
                string s = "";
                cur = Console.Read();
                while (cur != 32 && cur != 13 && cur !=  10)
                {
                    s += Convert.ToChar(cur);
                    cur = Console.Read();
                }

                long cislo = long.Parse(s);
                if (cislo == -1)

                {
                    running = false;
                }
                else if (cislo > max)
                {
                    long temp = max;
                    max = cislo;
                    snd = temp;
                }
                else if (cislo > snd)
                {
                    snd = cislo;
                }
            }
            Console.WriteLine(snd);

        }

    }

}
