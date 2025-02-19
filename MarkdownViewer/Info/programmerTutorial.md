# Dokumentace k Python kódu

Tento Python skript je určený k zobrazení a interakci s Markdown soubory v grafickém uživatelském rozhraní (GUI) pomocí Tkinteru a knihovny `tkinterweb` pro zobrazení HTML obsahu. Skript obsahuje funkce pro načítání souboru ve formátu Markdown, jeho převod na HTML, a vykreslení obsahu v GUI aplikaci. Kromě toho podporuje přizpůsobené funkce pro manipulaci s ID hlaviček, odstraňování diakritiky a přidávání CSS pro vzhled.

## Obsah
1. [Importy](#importy)
2. [Funkce](#funkce)
  - [CustomHeaderIdProcessor a CustomHeaderIdExtension](#customheaderidprocessor-a-customheaderidextension)
  - [remove_accents](#remove_accents)
  - [modify_ids](#modify_ids)
  - [load_markdown](#load_markdown)
  - [open_link](#open_link)
3. [GUI](#gui)
4. [CSS](#css)
5. [Jak to funguje](#jak-to-funguje)
---

## Importy
Kód začíná importem několika knihoven, které zajišťují potřebnou funkčnost pro převod Markdown souboru do HTML, zobrazení v GUI, a další úpravy textu a formátování.

- `ctypes`: Používá se pro nastavení DPI awareness pro lepší zobrazení na vysokých DPI obrazovkách.
- `re`: Knihovna pro práci s regulárními výrazy, používá se pro úpravu HTML kódu.
- `tkinter`: Knihovna pro tvorbu grafického uživatelského rozhraní.
- `tkinterweb`: Umožňuje zobrazovat HTML obsah v Tkinter aplikaci.
- `markdown`: Knihovna pro konverzi Markdown textu na HTML.
- `markdown.extensions.toc`: Rozšíření pro generování obsahu (Table of Contents).
- `unicodedata`: Používá se k odstranění diakritiky z textu.

---

## Funkce

### CustomHeaderIdProcessor a CustomHeaderIdExtension
Tato rozšíření pro knihovnu `markdown` umožňují přizpůsobit generování ID pro hlavičky (`h1`, `h2`, atd.). ID jsou převáděna na malá písmena a mezery jsou nahrazovány pomlčkami.

### remove_accents
Tato funkce odstraňuje diakritiku z textu, což je užitečné pro zajištění, že všechny ID jsou kompatibilní s URL (např. odstranění písmen s háčky nebo čárkami).

### modify_ids
Funkce pro úpravu odkazů (atributy `href` v HTML) tak, aby byly všechny ID v malých písmenech a bez diakritiky.

### load_markdown
Tato funkce načítá Markdown soubor, převádí jeho obsah na HTML pomocí knihovny `markdown`, přidává specifická rozšíření (jako generování obsahu a vlastní ID pro hlavičky), a provádí několik úprav v HTML. Například převádí zrušený text (strikethrough) na HTML tag `<del>`, nebo upravuje zaškrtávací políčka na HTML formát.

HTML obsah je následně vložen do webového rámce (`HtmlFrame`), který je součástí Tkinter GUI. Pro zajištění plynulého posouvání stránek je přidán JavaScript pro zpracování anchor odkazů.

### open_link
Funkce pro otevírání odkazů, které jsou obsaženy v HTML souboru. Pokud odkaz obsahuje kotvu (hash `#`), otevře se odpovídající část dokumentu v rámci aplikace, jinak se otevře v externím prohlížeči.

---

## GUI
### Tkinter Okno (`root`)
Aplikace využívá Tkinter pro vytvoření GUI. Okno je nastaveno na "zoomed" stav, aby se přizpůsobilo obrazovce. Do okna je přidáno tlačítko pro načítání souborů Markdown (`btn_load`), které spustí funkci `load_markdown`.

### HTML Frame (`html_frame`)
Tento rámec je zodpovědný za zobrazení HTML obsahu převzatého z Markdown souboru. Rámec také podporuje přidání vlastního CSS pro styling a reakci na kliknutí na odkazy.

---

## CSS
Skript načítá externí soubor CSS (`abyToByloHezke.css`), který je použit pro přizpůsobení vzhledu HTML obsahu v aplikaci. Tento CSS soubor je načítán při startu aplikace a přidán do HTML rámce pro aplikování stylů.

### Úvod

Tento CSS soubor slouží k vylepšení vzhledu a čitelnosti webové stránky, která obsahuje textový obsah a kód (například po konverzi Markdown souboru). Stylizace je navržena tak, aby byla stránka přehledná a dobře čitelná na různých zařízeních. Zahrnuje různé části pro fonty, kódové bloky, seznamy, tabulky a další, čímž vytváří příjemné prostředí pro uživatele.

### Fonty a Typografie

1. **Základní styl pro tělo stránky**  
   Základní nastavení pro texty na stránce zahrnuje použití fontu "Arial" s fallback na "Noto Color Emoji" pro emoji (které zatím nefunguje). Nastaveno je větší písmo a větší mezery mezi řádky, což zlepšuje čitelnost. Dále jsou přidány okraje pro text, aby obsah nebyl na okraji obrazovky, což zlepšuje čitelnost na širokých monitorech. Pozadí stránky je světle šedé, což dodává stránce jemnější vzhled, a text je tmavě šedý, aby byl dobře kontrastní vůči pozadí.

### Speciální Formátování

2. **Blockquote (citace)**  
   Pro texty v tagu `<blockquote>`, které označují citace, je nastavený kurzivní styl a šedá barva. To zajišťuje, že citace budou vizuálně odlišeny od běžného textu a snadno je rozeznáte.

3. **Kódové bloky**  
   Tento styl se zaměřuje na zobrazení kódových bloků (např. při zobrazování kódu ve formátu Markdown). Kódové bloky jsou zobrazeny s odlišným pozadím a okraji, což je odlišuje od ostatního textu na stránce. Použití přetékání (overflow-x) znamená, že pokud je kód příliš široký, bude mít horizontální posuvník.

4. **Syntax Highlighting (zvýraznění syntaxe)**  
   Pro kódové bloky je implementováno zvýraznění syntaxe. Každý typ kódu (například klíčová slova, proměnné, funkce, řetězce) je zobrazen různými barvami. To usnadňuje čtení kódu a orientaci v něm, zejména pro programátory, kteří hledají specifické části kódu.

### Interaktivita a Seznamy

5. **Checkboxy**  
   Pro zobrazení checkboxů (např. v seznamu úkolů) je vytvořený styl, který zajišťuje, že neoznačené checkboxy budou mít malý červený rámeček a po zaškrtnutí se změní na zelené. Tento interaktivní prvek je vizuálně přehledný a zjednodušuje práci s úkoly na stránce.

6. **Seznamy**  
   Pro checkboxy v seznamu je nastaven menší font, což pomáhá k lepší úpravenosti a čitelnosti seznamu.

### Tabulky

7. **Tabulky**  
   Tabulky mají nastavený plný široký prostor pro obsah (100% šířka), s okraji mezi buňkami a paddingem pro lepší čitelnost. Nadpisy tabulek jsou zobrazeny na šedém pozadí, což je vizuálně odděluje od ostatního obsahu tabulky.




---

## Jak to funguje

1. **Načítání Markdown souboru**:
    - Po spuštění aplikace a kliknutí na tlačítko "Open Markdown File" je uživateli umožněno vybrat Markdown soubor. Tento soubor je následně načten a převeden na HTML. Současně jsou aplikovány specifické úpravy pro formátování a generování obsahu (TOC).
    
2. **Zobrazení HTML**:
    - Po převodu je HTML zobrazeno v rámci aplikace pomocí widgetu `HtmlFrame`. Uživatel může prohlížet Markdown obsah v prohlížečovém formátu přímo v Tkinter okně.
    
3. **Interakce s odkazy**:
    - Jakýkoli odkaz v Markdown souboru (např. vygenerovaný TOC) je interaktivní. Pokud je to kotva, skáče na odpovídající část dokumentu, jinak otevírá externí URL v prohlížeči.

4. **Přizpůsobení vzhledu**:
    - Používá se externí CSS soubor pro úpravu vzhledu HTML obsahu, což zajišťuje lepší vizuální vzhled a čitelnost.

Tento kód umožňuje efektivní a interaktivní zobrazení Markdown souborů v grafickém rozhraní, což může být užitečné pro různé aplikace, které vyžadují zobrazení dokumentace nebo textových souborů ve formátu Markdown.
