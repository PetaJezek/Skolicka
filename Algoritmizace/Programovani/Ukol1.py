nejvetsi = int(input())
druhy = -1
Input = 0
if nejvetsi != -1:  
    Input = int(input())
    while Input != -1:
        
        if (druhy == -1) and (nejvetsi > Input):
            druhy = Input
        elif nejvetsi > Input > druhy:
            druhy = Input
        elif Input > nejvetsi:
            temp = nejvetsi
            nejvetsi = Input
            druhy = temp
        Input = int(input())
        

    if Input == -1 and druhy != -1:
        print(druhy)
    else: print(nejvetsi)
else: print(nejvetsi)