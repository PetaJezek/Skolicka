using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Xml.Linq;
using System;

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
        public int[,] pole = new int[8, 8];
        

        public (int, int) start { get; set; }
        public (int, int) end { get; set; }

        private void readInput()
        {
            int pocetPrekazek = int.Parse(Console.ReadLine());
            for (int i = 0; i < pocetPrekazek; i++)
            {
                string[] line = Console.ReadLine().Split();
                pole[int.Parse(line[0])-1, int.Parse(line[1]) - 1] = -2;
            }

            string[] line1 = Console.ReadLine().Split();
            pole[int.Parse(line1[0]) - 1, int.Parse(line1[1]) - 1] = 0;
            start = (int.Parse(line1[0]) - 1, int.Parse(line1[1])-1);


            line1 = Console.ReadLine().Split();
            pole[int.Parse(line1[0]) - 1, int.Parse(line1[1]) - 1] = -1;
            end = (int.Parse(line1[0]) - 1, int.Parse(line1[1]) - 1);

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
                        if (newX >= 0 && newX <= 7 && newY >= 0 && newY <= 7)
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
