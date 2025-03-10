#!/usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        
        radek = line.split()
        points_a = 0
        points_b = 0
        goals_a = radek[1]
        goals_b = radek[3]
        if goals_a > goals_b:
            points_a = 3
            points_b = 0
        elif goals_b > goals_a:
            points_a = 0
            points_b = 3
        else:
            points_a = 1
            points_b = 1

         

        sys.stdout.write("points," + radek[0] + "," + str(points_a) + "\n")
        sys.stdout.write("goals," + radek[0] + ","+ str(goals_a) + "\n")
        sys.stdout.write("points," + radek[4] + "," + str(points_b) + "\n")
        sys.stdout.write("goals," + radek[4] + ","+ str(goals_b) + "\n")



if __name__ == "__main__":
    main()