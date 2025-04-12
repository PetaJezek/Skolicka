using System;
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
            int decimalCap = 6;
            int cur_length;
            string C = "";
            while (A.Length > 0)
            {
                
                
                cur_length = C.Length;
                while (A.Length > 0)
                {
                    
                    if (long.TryParse(C, out long res) && (res >= B || res == 0))
                    {
                        break;
                    }
                    C += A[0];
                    A = A.Remove(0, 1);

                }

                long cur = long.Parse(C) / B;
                result.Append(cur.ToString());
                long rem = long.Parse(C) - (cur * B);
                if(rem == 0)
                {
                    C = "";
                }
                else
                {
                    C = rem.ToString();
                }
            }
            result = new StringBuilder(result.ToString().TrimStart('0'));

            

            if (result.Length == 0) result.Append("0");

            int decimalDotId = result.Length;



            while (C != "" && long.Parse(C)!= 0 && decimalDigits < decimalCap + 1)
            {
                C += '0';
                long cur = long.Parse(C) / B;
                result.Append(cur.ToString());
                decimalDigits++;
                long rem = long.Parse(C) - (cur * B);
                C = rem.ToString();

            }
            while(decimalDigits < decimalCap + 1)
            {
                result.Append('0');
                decimalDigits++;
            }

            
            int roundDigitIndex = result.Length - 1;
            int roundDigit = result[roundDigitIndex] - '0';

            result.Remove(roundDigitIndex, 1); 

            if (roundDigit >= 5)
            {
                int i = roundDigitIndex - 1;
                while (i >= 0)
                {
                    if (result[i] == '.')
                    {
                        i--;
                        continue;
                    }

                    int digit = result[i] - '0';
                    if (digit < 9)
                    {
                        result[i] = (char)(digit + 1 + '0');
                        break;
                    }
                    else
                    {
                        result[i] = '0';
                        i--;
                    }
                }

                if (i < 0)
                {
                    result.Insert(0, '1');
                    decimalDotId++;
                }
            }

           
            while (result.Length - decimalDotId < 6)
                result.Append('0');

            result.Insert(decimalDotId, '.');
            return result.ToString();
        }
    }

}
