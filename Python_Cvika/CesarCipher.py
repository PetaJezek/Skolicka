k = int(input())

if k < 0:

    while k < 0:

        k += 26
        
k = (k)%26 

text = (input())

text = text.upper()

chars = []

s = ""

for ch in text:
    if ord("Z") >= ord(ch) + k>= ord("A") and ord("Z") >= ord(ch)>= ord("A"):
        chars.append(chr(ord(ch)+ k))
    elif ord("Z") >= ord(ch)>= ord("A"):
        chars.append(chr(ord(ch)+ k - 26))
    else: 
        chars.append(ch)     

for i in chars:

    s = s + i

print(s)
