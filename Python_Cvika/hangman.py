li = []
def Start():
    word = "haaaaaaaaaarambeeeeeeee"
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
        print(f"STAV: Mas " + str(10 - n) + " pokus(u)")
        print("Napis pismeno:")
        guess = input()
        if guess in li:
            for i in range(len(li)):
                if guess == li[i]:
                    guessed[i] = guess
            print(''.join(guessed))
            if "_" not in guessed:
                playing = False
                win = True
        else:
            print("Bohuzel bracho.")
            n += 1
            if n == 10:
                playing = False
    if win == True:
        print("HURAA")
    else:
        print("Snad priste")
        for i in range(100):
            print("*")
        print("IDIOT LMAOOOOOO")
        
Start()
        
        



