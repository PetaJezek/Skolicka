using System.Globalization;
using System.Reflection.Metadata;
using System.Runtime.InteropServices;
using System.Text;

namespace DeleniDlouhehoCisla
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string A = Console.ReadLine();
            int B = int.Parse(Console.ReadLine());
            Console.WriteLine(LongDivision(A, B));
        }

        static string LongDivision(string A, int B)
        {
            StringBuilder result = new StringBuilder();
            
            int decimalDigits = 0;
            int decimalCap = 7;
            int cur_length;
            string C = "";
            while (A.Length > 0)
            {
                // extract the first digits that create a number greater than B
                
                cur_length = C.Length;
                
                while (A.Length > 0)
                {
                    //try parse C 
                    if(int.TryParse(C, out int res) && res >= B)
                    {
                        break;
                    }
             
                    C += A[0];
                    A = A.Remove(0, 1);
                    cur_length = C.Length;
                }

                int cur = int.Parse(C) / B;
                result.Append(cur.ToString());
                int rem = int.Parse(C) - (cur * B);
                C = rem.ToString();


            }
            
             result.Append('.');
            
            
            while(int.Parse(C) != 0 && decimalDigits < decimalCap)
            {
                C += '0';
                int cur = int.Parse(C) / B;
                result.Append(cur.ToString());
                decimalDigits++;
                int rem = int.Parse(C) - (cur * B);
                C = rem.ToString();

            }
            while(decimalDigits < decimalCap)
            {
                result.Append('0');
                decimalDigits++;
            }
            
            bool carry = false;
            int id = result.Length - 1;
            do
            {
                if(carry == true)
                {
                    result[id] = (char)(result[id] + 1);
                }

                if(result[id] == '9')
                {
                    result[id] = '0';
                    carry = true;
                    id--;
                }
                else
                {
                   
                    carry = false;
                }
            }
            while (carry);



            return result.ToString();
        }
    }

}
