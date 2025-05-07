using System;
using System.Collections.Generic;


class Program
{
    static void Main(string[] args)
    {
        var game = new Game();
    }
}

class Game
{
    private int rounds;
    private char[][] grid;
    private Beast beast;

    public Game()
    {
        
        rounds = 20; 

       
        List<string> lines = new List<string>();
        int width = int.Parse(Console.ReadLine());
        int height = int.Parse(Console.ReadLine());

        grid = new char[height][];
        for (int i = 0; i < height; i++)
        {
            string line = Console.ReadLine();
            grid[i] = line.ToCharArray();
        }


      
        beast = new Beast(grid);
        Run();
    }

    private void Run()
    {
        for (int i = 0; i < rounds; i++)
        {
            Move();
        }
    }

    private void View()
    {
        for (int i = 0; i < grid.Length; i++)
        {
            Console.WriteLine(new string(grid[i]));
        }
        Console.WriteLine();
    }

    private void Move()
    {
        int rightRow = beast.Position[0] + beast.Right[0];
        int rightCol = beast.Position[1] + beast.Right[1];
        int forwardRow = beast.Position[0] + beast.Forward[0];
        int forwardCol = beast.Position[1] + beast.Forward[1];

        if (rightRow >= 0 && rightRow < grid.Length && rightCol >= 0 && rightCol < grid[0].Length &&
            grid[rightRow][rightCol] == '.')
        {
            
            beast.RotateRight();
            grid[beast.Position[0]][beast.Position[1]] = beast.Char;
            View();
            rounds--;

            if (rounds > 0)
            {
                grid[beast.Position[0]][beast.Position[1]] = '.';
                beast.Position[0] += beast.Forward[0];
                beast.Position[1] += beast.Forward[1];
                grid[beast.Position[0]][beast.Position[1]] = beast.Char;
                View();
                rounds--;
            }
        }
        else if (rightRow >= 0 && rightRow < grid.Length && rightCol >= 0 && rightCol < grid[0].Length &&
                 grid[rightRow][rightCol] == 'X' &&
                 forwardRow >= 0 && forwardRow < grid.Length && forwardCol >= 0 && forwardCol < grid[0].Length &&
                 grid[forwardRow][forwardCol] == '.')
        {
         
            grid[beast.Position[0]][beast.Position[1]] = '.';
            beast.Position[0] += beast.Forward[0];
            beast.Position[1] += beast.Forward[1];
            grid[beast.Position[0]][beast.Position[1]] = beast.Char;
            View();
        }
        else
        {
           
            beast.RotateLeft();
            grid[beast.Position[0]][beast.Position[1]] = beast.Char;
            View();
        }
    }
}

class Beast
{
    public char Char { get; set; }
    public int[] Right { get; set; }
    public int[] Forward { get; set; }
    public int[] Left { get; set; }
    public int[] Down { get; set; }
    public int[] Position { get; set; }

    public Beast(char[][] grid)
    {
        Right = new int[2];
        Forward = new int[2];
        Left = new int[2];
        Down = new int[2];
        Position = new int[2];

        for (int i = 0; i < grid.Length; i++)
        {
            for (int j = 0; j < grid[i].Length; j++)
            {
                if (grid[i][j] == '^')
                {
                    Char = '^';
                    Right = new int[] { 0, 1 };
                    Forward = new int[] { -1, 0 };
                    Left = new int[] { 0, -1 };
                    Down = new int[] { 1, 0 };
                    Position = new int[] { i, j };
                    return;
                }
                else if (grid[i][j] == 'v')
                {
                    Char = 'v';
                    Right = new int[] { 0, -1 };
                    Forward = new int[] { 1, 0 };
                    Left = new int[] { 0, 1 };
                    Down = new int[] { -1, 0 };
                    Position = new int[] { i, j };
                    return;
                }
                else if (grid[i][j] == '>')
                {
                    Char = '>';
                    Right = new int[] { 1, 0 };
                    Forward = new int[] { 0, 1 };
                    Left = new int[] { -1, 0 };
                    Down = new int[] { 0, -1 };
                    Position = new int[] { i, j };
                    return;
                }
                else if (grid[i][j] == '<')
                {
                    Char = '<';
                    Right = new int[] { -1, 0 };
                    Forward = new int[] { 0, -1 };
                    Left = new int[] { 1, 0 };
                    Down = new int[] { 0, 1 };
                    Position = new int[] { i, j };
                    return;
                }
            }
        }
    }

    public void RotateLeft()
    {
        int[] tempVector = Forward;
        Forward = Left;
        Left = Down;
        Down = Right;
        Right = tempVector;

        if (Char == '^')
            Char = '<';
        else if (Char == '>')
            Char = '^';
        else if (Char == 'v')
            Char = '>';
        else
            Char = 'v';
    }

    public void RotateRight()
    {
        int[] tempVector = Forward;
        Forward = Right;
        Right = Down;
        Down = Left;
        Left = tempVector;

        if (Char == '^')
            Char = '>';
        else if (Char == '>')
            Char = 'v';
        else if (Char == 'v')
            Char = '<';
        else
            Char = '^';
    }
}