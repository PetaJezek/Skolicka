s = input()
print(s)
with open(s, "rb") as f:
    f = f.read()

magic = []
while f:
    current_magic = f[:4]
    current_magic = current_magic.decode('utf-8')
    
    magic.append(current_magic)
    f = f[4:]
    int_lenght = 0
    lenght = f[:4]
    for byte in lenght:
        int_lenght = (int_lenght << 8) | byte

    f = f[4+int_lenght:]
    
    
print(*magic)
##Principy pocitacu/StarTrek_TheNextGeneration.mid
##Principy pocitacu/Bass_sample-trackname-MTrk-signal.app-saved.mid
    
    

