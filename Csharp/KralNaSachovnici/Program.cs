using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

namespace KralNaSachovnici
{
    class linkList
    {

    }
    class KralSachovnici
    {
        public int[,] pole = new int[8, 8];
        public (int, int) start { get; set; }
        public KralSachovnici()
        {
            int pocetPrekazek = int.Parse(Console.ReadLine());
            for (int i = 0; i < pocetPrekazek; i++)
            {
                string[] line = Console.ReadLine().Split();
                pole[int.Parse(line[0]), int.Parse(line[1])] = -2;
            }
            string[] line1 = Console.ReadLine().Split();
            
            pole[int.Parse(line1[0]), int.Parse(line1[1])] = 0;
            start = (int.Parse(line1[0]), int.Parse(line1[1]);


            string[] line1 = Console.ReadLine().Split();
            pole[int.Parse(line1[0]), int.Parse(line1[1])] = -1;
            
        }

        public int Prohledej()
        {
            
        }
        
        
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            KralSachovnici kral = new();
            Console.WriteLine(kral.pole);
        }
    }
}
