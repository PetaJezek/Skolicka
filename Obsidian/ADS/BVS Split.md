
``` python
rozděl(t, k):
    // Pokud je strom prázdný
    pokud t == null:
        vrať (null, null)
    
    // Pokud je hodnota v kořeni menší nebo rovna k
    pokud t.hodnota <= k:
        
        (mensi, vetsi) = rozděl(t.pravý, k)
	//Ziskavame pod stromy s hodnotama mensima a vetsima nez k 
        t.pravý = mensi
        
        // Vrátíme  upravený strom t a větší strom z rekurze
        vrať (t = t1, vetsi = t2)
    
    // Pokud je hodnota v kořeni větší než k delame to stejne akorat invertovaně
    jinak:
        (mensi, vetsi) = rozděl(t.levý, k)
        
        t.levý = vetsi
        
        vrať (mensi = t1, t = t2)

```

Každou rekurzí se posouváme vždycky na dalšího potomka, a operace které provadíme zabírají $O(1)$, tedy celková složitost je $O(h)$, kde h je hloubka stromu $t$.