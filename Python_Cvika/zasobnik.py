import sys
text = []


## string = "$ python3 my_prog.py < sample_input To come home.  Peel off sandals. And step.  Onto the cool tile floor.  Needing only the rush of water.  Overstrawberries I picked myself."
for line in sys.stdin:
    line = line.strip()
    for i in line:
        if i != ".":
            text.append(i)
        else:
            text.append(i)
            text.append("\n")
            i += 1
print(''.join(text))
