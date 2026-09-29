import pandas as pd
import pyreadstat
import matplotlib.pyplot as plt
import numpy as np  
import math        

df, meta = pyreadstat.read_sav("data.SAV", apply_value_formats=True)

lgbt_colors = ['#E40303', '#FF8C00', '#FFED00', '#008026', '#732982']
neplatne = ['Neví', 'Odmítl odpovědět', 'NEVÍ', 'ODMÍTL ODPOVĚDĚT']
poradi = [
    'ROZHODNĚ SOUHLASÍ', 'SPÍŠE SOUHLASÍ', 
    'ANI SOUHLAS ANI NESOUHLAS', 
    'SPÍŠE NESOUHLASÍ', 'ROZHODNĚ NESOUHLASÍ'
]

def vytvor_kolace(df, sloupec_x, nazev_grafu, jmeno_souboru):
    #  dat
    df_clean = df.loc[:, [sloupec_x, 'Manzelstvi_pro_vsechny']].dropna()
    df_clean = df_clean[~df_clean['Manzelstvi_pro_vsechny'].isin(neplatne)]
    
    crosstab = pd.crosstab(df_clean[sloupec_x], df_clean['Manzelstvi_pro_vsechny'])
    
    aktualni_poradi = [col for col in poradi if col in crosstab.columns]
    crosstab = crosstab[aktualni_poradi]
    
    kategorie = crosstab.index.tolist()
    pocet_kolacu = len(kategorie)
    
    sloupce = min(pocet_kolacu, 3)                
    radky = math.ceil(pocet_kolacu / 3)           
    
    fig, axes = plt.subplots(radky, sloupce, figsize=(5 * sloupce, 5 * radky))
    
    if pocet_kolacu == 1:
        axes_flat = [axes]
    else:
        axes_flat = np.array(axes).flatten()
        
    for i, kat in enumerate(kategorie):
        data_kat = crosstab.loc[kat]
        axes_flat[i].pie(
            data_kat, 
            autopct='%1.1f%%',
            startangle=90,
            colors=lgbt_colors[:len(aktualni_poradi)],
            wedgeprops={'edgecolor': 'white'}
        )
        axes_flat[i].set_title(kat, fontsize=14, pad=15)
        

    for j in range(pocet_kolacu, len(axes_flat)):
        axes_flat[j].set_visible(False)
        
    fig.legend(
        aktualni_poradi, 
        title="Postoj k návrhu", 
        loc="center left",         
        bbox_to_anchor=(1.0, 0.5), 
        fontsize=11
    )
    
    plt.suptitle(nazev_grafu, fontsize=16, y=1.05 if radky == 1 else 1.02)
    plt.tight_layout()
    
    plt.savefig(jmeno_souboru, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Graf byl úspěšně uložen jako {jmeno_souboru}")

vytvor_kolace(df, 'Pohlavi', 'Podpora manželství pro všechny podle pohlaví', 'graf_pohlavi.png')
vytvor_kolace(df, 'Vzdelani', 'Podpora manželství pro všechny podle vzdělání', 'graf_vzdelani.png')
vytvor_kolace(df, 'Vek_kategorie', 'Podpora manželství pro všechny podle věku', 'graf_vek.png')