using System;
namespace Telefonni_seznam
{
    public class Node
    {
        public int Data;
        public Node Next;
        public Node(int data)
        {
            Data = data;
            Next = null;
        }
    }
    public class LinkedList
    {
        private Node head;
        public void Add(int data)
        {
            Node node = new(data);
            node.Next = head;
            head = node;
        }
        public void Remove(int data)
        {
            if (head == null) return;
            bool found = false;
            Node current = head;
            if(head.Data == data)
            {
                head = head.Next;
                return;
            }
            while (current.Next != null && found == false)
            {
                if(current.Next.Data == data)
                {
                    current.Next = current.Next.Next;
                    found = true;
                }
                else
                {
                    current = current.Next;
                }
                

            }
        }
        public void PrintList()
        {
            if(head != null)
            {
                Node current = head;
                while (current != null)
                {
                    Console.WriteLine(current.Data);
                    current = current.Next;
                }
                
            }
            
        }
        public void BubbleSort()
        {
            if(head == null) { return; }
            bool prohazovano;
            do
            {
                prohazovano = false;
                Node current = head;
                while(current.Next != null)
                {
                    if(current.Data < current.Next.Data)
                    {

                        (current.Data, current.Next.Data) = (current.Next.Data, current.Data);
                        prohazovano = true;
                    }
                    current = current.Next;
                }
            }
            while (prohazovano == true);
        }
    }
    class Phonebook
    {
        private LinkedList linkedList = new();
        bool jedem = true;
        public Phonebook()
        {
            while (jedem)
            {
                int[] input = [0,0];
                int i = 0;
                foreach(string str in Console.ReadLine().Split())
                {
                    input[i] = Convert.ToInt32(str);
                    i++;
                }
                switch (input[0])
                {
                
                    case 1:
                        linkedList.Add(input[1]);
                        break;
                    case 2:
                        linkedList.Remove(input[1]);
                        break;
                    case 4:
                        linkedList.BubbleSort();
                        break;
                    case 5:
                        linkedList.PrintList();
                        break;
                    case 6:
                        jedem = false;
                        break;
                    default:
                        break;
                }
            }
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            Phonebook phonebook = new();
        }
    }
}
