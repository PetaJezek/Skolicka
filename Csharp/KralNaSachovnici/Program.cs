using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Xml.Linq;
using System;
using System.IO;


/*
OBJEKTOVÝ NÁVRH PROGRAMU "KRÁL NA ŠACHOVNICI"

Třída Node:
- Uzel obsahuje data typu (int, int), což jsou souřadnice na šachovnici
- Má odkaz na další uzel v seznamu (Next)
- Konstruktor vytvoří nový uzel a nastaví mu souřadnice, odkaz na další je null

Třída LinkedList:
- Jednoduchý spojový seznam, který má jenom odkaz na hlavu (head)
- Metoda Add přidává nový prvek na začátek seznamu - nejdřív se vytvoří nový uzel, potom se nastaví jeho Next na starou hlavu a nakonec se nový uzel stane hlavou
- Metoda RemoveLast odebere poslední prvek ze seznamu a vrátí jeho data
  * Pokud je v seznamu jen jeden prvek, vrátí se jeho hodnota a seznam se vyprázdní
  * Jinak se projde seznam až k předposlednímu prvku, zapamatuje se hodnota posledního, poslední se odřízne a vrátí se hodnota

Třída KralSachovnici:
- Hlavní třída programu, obsahuje spojový seznam (linkedList) pro ukládání pozic k prozkoumání
  * height - výška šachovnice (výchozí hodnota 8)
  * width - šířka šachovnice (výchozí hodnota 8)
  * start - souřadnice krále na začátku (dvojice int)
  * end - souřadnice cíle (dvojice int)
  * pole - 2D pole, které představuje šachovnici, kde:
    - 0 znamená volné pole nebo výchozí pozici krále
    - -2 je zakázané pole (označené jako 'X' ve vstupu)
    - -1 je cílové pole (označené jako 'C' ve vstupu)
    - kladné číslo představuje vzdálenost od startu (kolik tahů krále je potřeba)

- Metoda readInput:
  * Načte vstupní soubor "sachovnice.txt"
  * První řádek je výška, druhý řádek je šířka
  * Další řádky popisují šachovnici znaky ., X, S, C
  * Nastaví pole, start a end podle vstupu

- Metoda ProhledejPole:
  * Implementuje něco jako BFS (ale ne úplně )
  * Vloží startovní pozici do seznamu
  * Dokud není seznam prázdný a cíl není dosažen:
    - Vezme poslední pozici ze seznamu (to není typické pro BFS, tam se obvykle bere první)
    - Pro všech 8 směrů, kam může král táhnout:
      * Spočítá nové souřadnice
      * Zkontroluje, jestli jsou v šachovnici (ale je tam chyba v porovnání s <= místo <)
      
*/

namespace KralNaSachovnici
{
    public class Node
    {
        public (int,int) Data { get; set; }
        public Node Next { get; set; }
        public Node((int,int) data)
        {
            Data = data;
            Next = null;
        }
    }
    public class LinkedList
    {

        public Node head;

        public void Add((int, int) data)
        {
            Node node = new(data)
            {
                Next = head
            };

            head = node;

        }
        
        public (int,int) RemoveLast()
        {
            Node current = head;
            
            if(current.Next == null)
            {
                (int, int) temp1 = head.Data;
                head = null;
                return temp1;   
            }
            while(current.Next.Next != null)
            {
                current = current.Next;
            }
            (int, int) temp = current.Next.Data;
            current.Next = null;
            return temp;
        }
    }

    class KralSachovnici
    {
        LinkedList linkedList = new();
        
        
        public int height { get; set; } = 8;
        public int width { get; set; } = 8;
        public (int, int) start { get; set; }
        public (int, int) end { get; set; }

        public int[,] pole { get; set; }
        private void readInput()
        {
            string[] lines = File.ReadAllLines("sachovnice.txt");

            height = int.Parse(lines[0]);
            width = int.Parse(lines[1]);
            pole = new int[height, width];
            for (int i = 0; i < height; i++)
            {
                string line = lines[i + 2];

                for (int j = 0; j < width; j++)
                {
                    char c = line[j];

                    if (c == '.')
                        pole[i, j] = 0;

                    else if (c == 'X')
                        pole[i, j] = -2;
                    else if (c == 'S')
                    {
                        pole[i, j] = 0;
                        start = (i, j);
                    }
                    else if (c == 'C')
                    {
                        pole[i, j] = -1;
                        end = (i, j);
                    }
                }
            }

        }
        public void ProhledejPole()
        {
            linkedList.Add(start);
            while (linkedList.head != null && pole[end.Item1, end.Item2] == -1)
            {
                (int  x, int y) = linkedList.RemoveLast();

                int hloubka = pole[x, y];
                for (int i = -1; i < 2; i++)
                {
                    for (int j = -1; j < 2; j++)
                    {
                        int newX = i + x;
                        int newY = j + y;

                        if(i == 0 && j == 0)
                        {
                            continue;
                        }
                        if (newX >= 0 && newX < height  && newY >= 0 && newY < width)
                        {
                            if (pole[newX, newY] == 0)
                            {
                                linkedList.Add((newX, newY));
                                pole[newX, newY] = hloubka + 1;
                            }
                            
                            if (pole[newX, newY] == -1)
                            {
                                pole[newX, newY] = hloubka + 1;
                            }
                        }
                    }
                }
            }
            return;
        }
        public KralSachovnici()
        {
            readInput();
            
            ProhledejPole();
            if(start == end)
            {
                Console.WriteLine(0);
            }
            else
            {
                Console.WriteLine(pole[end.Item1, end.Item2]);
            }
               
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            KralSachovnici kral = new();
           
        }
    }
}
