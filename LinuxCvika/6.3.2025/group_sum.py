#!/usr/bin/env python3
import sys

def main():
    body = {}
    goly = {}
    i = 0
    for line in sys.stdin:
        line.rstrip()
        line = line.split(",")
        line.pop(0)
        line[1] = int(line[1].rstrip())
        
        if i // 2 == 0:
            if line[0] not in body.keys():
                body.update({line[0] : int(line[1])})
            else:
                body.update({line[0] : body.get(line[0]) + int(line[1])})
        else:
            if line[0] not in body.keys():
                goly.update({line[0] : int(line[1])})
            else:
                goly.update({line[0] : goly.get(line[0])+ int(line[1])})
        i += 1

    for key, value in body.items():
        sys.stdout.write(f"{key} {value}" + "\n")
    for key, value in goly.items():
        sys.stdout.write(f"{key} {value}" + "\n")
    
        



if __name__ == "__main__":
    main()