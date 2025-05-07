namespace NPP
{
    internal class Program
    {
        static void Main(string[] args)
        {

            int pocet = int.Parse(Console.ReadLine());
            string s = Console.ReadLine();

            int id = 0;
            int temp = 0;
            int x = 0;
            while (id <= pocet)
            {
                if (s[x] == 32) 
                {
                    id++;

                }

                x++;
            }



            
        }
        static void SpocitejPKonciciZde()
    }
}
