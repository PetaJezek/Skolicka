import random

def stredni_hodnota(result, length):    
    # Caluclates expected value of P
    lastWasP = False
    countPO = 0
    countnotPO = 0

    for i in range(length):
        if i == 0:
            if result[i] == 'P':
                lastWasP = True
        elif result[i] == 'P':
            lastWasP = True
            countnotPO += 1
        elif lastWasP:
            countPO += 1
            lastWasP = False
        else:
            lastWasP = False
            countnotPO += 1
    return countPO , countnotPO/length

def main():
    """
    Parses command-line arguments and prints a random sequence of 'P' and 'O'.
    """
    random.seed(35681771)
    
    weights = [2/3, 1/3]
    for k in range(1, 7):
        result = random.choices(('P', 'O'), weights=weights, k=10**k)
        #print(result)
        print(f"--------------Vysledky pro k={k}-----------------")  # Print only the first 50 characters for brevity
        stredniHodnota, countPO = stredni_hodnota(result, 10**k)
        print(f"Procento not PO: {countPO*100:.2f}%")
        print(f"Střední hodnota PO: {stredniHodnota}")
    


if __name__ == "__main__":
    main()