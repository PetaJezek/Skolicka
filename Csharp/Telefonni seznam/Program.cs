namespace Telefonni_seznam
{
    class Phonebook
    {
        public List<int> ints;
        bool jedem = true;
        public Phonebook()
        {


            List<int> ints = new();
            this.ints = ints;

           
            while (jedem)
            {
                List<int> input = new();
                foreach(string str in Console.ReadLine().Split())
                {
                    int a = int.Parse(str);
                    input.Add(a);

                }
                switch (input[0])
                {
                
                    case 1:
                        ints.Add(input[1]);
                        break;
                    case 2:
                        ints.Remove(input[1]);
                        break;
                    case 4:
                        ints.Sort();
                        ints.Reverse();
                        break;
                    case 5:
                        foreach (int i in ints)
                        {
                            Console.WriteLine(i);
                        }
                        break;
                    case 6:
                        jedem = false;
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
