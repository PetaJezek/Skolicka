"""

Dobrý den,
na tento úkol, bych potřeboval prodloužit deadline z důvodu mé neschopnosti najít řešení (a taky časového vytížení).
Tím myslím, že v tento moment mě nic nenapadá. Nad úkolem jsem přemýšlel celý týden a nikam jsem se neposunul. (Až na nějaký brute-force projít všechno)
Myslím, že do neděle mě snad už něco napadne. Děkuji
"""
"""

"""
import math
def solve(k):
    opponents = 100
    dp_table = [[0] * (k + 1)  for _ in range(opponents + 1)]
    back_track = [[0] * (k + 1)  for _ in range(opponents + 1)]
    for i in range(1,opponents+1):
        for rounds in range(1, k + 1):
            max_reward = 0
            for vyrazeny in  range(1, i + 1):
                odmena = math.floor((100000 * vyrazeny) / i)
                if max_reward <  odmena + dp_table[i - vyrazeny][rounds-1]:
                    location = (vyrazeny,(i - vyrazeny,rounds-1))
                    max_reward = odmena + dp_table[i - vyrazeny][rounds-1]
            max_reward = max(max_reward, odmena + dp_table[i - vyrazeny][rounds-1])
            dp_table[i][rounds] = max_reward
            back_track[i][rounds] = (location)
    print(dp_table[opponents][k])
    
    temp = back_track[opponents][k]
    cuts = []
    while temp[1] != (0,0):
        cuts.append(temp[0])
        k-= 1
        temp = back_track[temp[1][0]][temp[1][1]]
    cuts.append(temp[0])
    print(*(cuts))



    

solve(int(input()))
