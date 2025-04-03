using System.Globalization;
using System.Reflection.Metadata;

namespace DeleniDlouhehoCisla
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string A = Console.ReadLine();
            int B = int.Parse(Console.ReadLine());
            char[] vysledek = new char[(A.Length) + 6];
            // pro kazdej string v A vydelim ho B a vynasobim ho CISLEM RADU. 
            // PAK TO CISLO FLORNU NA 6 POSLEDNICH RADU
            //PAK  BUDU PRIDAVAT DO ARRAYE VYSLEDKU POSTUPNE
            //POKUD NECO PRETECE TAK PRIDAM TO CISLO DO DALSIHO POLICKA ARRAYE
            //ALE POJEDE SE POZPATKU v ARRAY VYSLEDEK
            
            while(A.Length != 0)
            {
                string s = "";
                s += A[^1];
                A = A[..^1];
                double delenec = int.Parse(s) / B;
                
                int pocet_cisel = Convert.ToString(Convert.ToInt64(delenec)).Length;
                delenec = Math.Round(delenec, 6);

                for (Int64 i = 0; i < pocet_cisel; i++)
                {
                    

                }

            }

        }
    }
}
