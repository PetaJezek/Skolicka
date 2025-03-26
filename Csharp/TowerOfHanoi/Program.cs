using System.Runtime.CompilerServices;
using System;

namespace TowerOfHanoi
{
    internal class Program
    {
        static public void Tower()
        {
            int pocet_kruhu = int.Parse(Console.ReadLine());

            string[] nazvy = { "1", "2", "3" };
            int i = 1;
            _TowerofHanoi(pocet_kruhu, nazvy[0], nazvy[1], nazvy[2]);
            
            void _TowerofHanoi(int pocet,string odkud,string kam,string volno)
            {
                if(pocet == 1)
                {
                    Console.WriteLine("Kotouc 1"  +  " z " + odkud + " na " + kam);
                    
                    return;
                    
                }
                _TowerofHanoi(pocet - 1, odkud, volno, kam);
                
                Console.WriteLine("Kotouc " + pocet + " z " + odkud + " na " + kam);

                pocet_kruhu -= 1;

                _TowerofHanoi(pocet - 1, volno, kam, odkud);
            }
        }

        static void Main(string[] args)
        {
            Tower();
        }
    }
}
