using System.Security.Cryptography.X509Certificates;

namespace OKF
{

    //create enum with 3 items]
    
    internal class Program
    {
        static void Spocitej()
        {
            int[] chlast = { 1, 2, 3 };
            int pocet = int.Parse(Console.ReadLine());
            int vysledek = 0;
            List<int[]> list = new List<int[]>();

            for (int i = 0; i < chlast.Length; i++)
            {


                _Spocitej(pocet-1, i, ref list);
            }
            Console.WriteLine(vysledek);
            void _Spocitej(int zbyle, int posledni, ref List<int[]> list)
            {

                if (zbyle == 0)
                {
                    vysledek++;
                    return;
                }


                if (posledni == 0)
                {


                    _Spocitej(zbyle - 1, 0, ref list);
                    _Spocitej(zbyle - 1, 1, ref list);
                    _Spocitej(zbyle - 1, 2, ref list);

                }
                else if (posledni == 1)
                {
                    _Spocitej(zbyle - 1, 0, ref list);
                    _Spocitej(zbyle - 1, 1, ref list);


                }
                else
                {
                    _Spocitej(zbyle - 1, 0, ref list);
                }
            }
        }
        static void Main(string[] args)
        {

            Spocitej();


        }



      

    }
}
