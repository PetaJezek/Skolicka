import sys

#s = sys.stdin.read()  # Reads the input provided via standard input
s = "!) And they all drank free"
word = []
line = []

for i in s:
    if i.isalpha():
        word.append(i)
    
    elif len(line) + len(word) < 30 and word:
        
        for j in word:
            line.append(j)
        line.append(' ')
        word = []
    elif word:
        print(''.join(line))
        line = []
        for j in word:
            line.append(j)
        
        word = []

for j in word:
    line.append(j)

print(''.join(line))
