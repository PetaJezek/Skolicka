import random
li = []
def Start():
    file = open('/home/jeza/Documents/Skolicka/Python_Cvika/podstatnaJmena.txt')
    content = file.readlines()
    
    word = "A"
    while word[0].isupper():
        word = content[random.randrange(0,len(content))].strip()
    global li 
    li = list(word)
    print("Jdeme hrat hahaha tak pojd tohle neuhodnes.")
    Round()
def Round():
    playing = True
    win = False
    n = 0
    global li
    guessed = ["_" for i in li]
    while playing == True:
        print(' '.join(guessed))
        print(f"STAV: Mas " + str(10 - n) + " pokus(u)")
        print("Napis pismeno:")
        guess = input()
        if guess in li:
            for i in range(len(li)):
                if guess == li[i]:
                    guessed[i] = guess
            if "_" not in guessed:
                playing = False
                win = True
            print("="* len(guessed)* 2)
        else:
            print("Bohuzel bracho.")
            print("="* len(guessed)* 2)
            n += 1
            if n == 10:
                playing = False
    if win == True:
        print("HURAA")
    else:
        print("Snad priste")
        print("Správná odpoved byla: "+ "".join(li))
        ##for i in range(100):
        ##print("IDIOT LMAOOOOOO")
        
Start()
        
        



