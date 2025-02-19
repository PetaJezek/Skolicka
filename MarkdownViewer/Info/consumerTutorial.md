# Markdown Viewer – Uživatelská příručka

## 📖 O aplikaci

**Markdown Viewer** je jednoduchá aplikace, která umožňuje otevírat a zobrazovat Markdown soubory (`.md`) v přehledné HTML podobě.

✅ Načítá a zobrazuje Markdown soubory  
✅ Podporuje klikatelné odkazy (v rámci dokumentu i na web)  
✅ Správně zobrazuje zaškrtávací políčka (checkboxy)  
✅ Obsahuje posuvník (scrollbar) pro pohodlné prohlížení  

---

## Jak aplikaci používat

### Instalace závislostí  

Pokud spouštíte aplikaci v Pythonu, je nutné nainstalovat potřebné knihovny.  

1. Ujistěte se, že máte nainstalovaný **Python 3.x**  
2. Otevřete terminál nebo příkazový řádek a přejděte do složky s aplikací  
3. Spusťte následující příkaz:  

   ```sh
   pip install -r requirements.txt
   ```

Soubor requirements.txt obsahuje následující knihovny, které jsou nutné pro správnou funkci aplikace:

1. Markdown==3.7
2. tkinterweb==3.25.12

Pokud nemáte pip, můžete ho nainstalovat podle [oficiální dokumentace](https://pip.pypa.io/en/stable/installation/)

### Spuštění aplikace

- Otevřete soubor **MarkdownViewer.exe** (nebo spusťte `markdownViewer.py`, pokud používáte verzi pro Python).

### Načtení Markdown souboru

1. Klikněte na tlačítko **"Open Markdown File"**.  
2. Vyberte soubor s příponou `.md`.  
3. Obsah souboru se zobrazí v okně aplikace.  

### Interaktivní funkce

- 📌 **Anchor links (kotvy)**: Kliknutím na odkaz v dokumentu ([Zpět na začátek](#markdown-viewer-uživatelská-příručka)) se plynule posunete na odpovídající sekci.
- 🌍 **Webové odkazy**: Kliknutím na odkaz na internetové stránce se otevře váš výchozí prohlížeč.  
- ✅ **Zaškrtávací políčka (checkboxy)**:  
  - `[x]` **Zelený čtvereček** = označené (checked)  
  - `[ ]` **Červený čtvereček** = neoznačené (unchecked)  
- 📜 **Posuvník (scrollbar)**: Pokud je soubor delší, lze stránkou pohodlně rolovat.  
- Podpora formátování: Aplikace správně zobrazuje různé formátovací prvky v Markdownu:

1. Kódové bloky:
    ```python
def hello():
    print("Hello, Markdown!")
    ```


2. Bloková kurzíva:

    > Toto je bloková kurzíva (blockquote).


3. Tabulky:

| Název  | Hodnota |
|--------|---------|
| První  | 10      |
| Druhý  | 20      |





Citace:

    "Markdown je skvělý pro psaní dokumentace!"

### Načtení dalšího souboru

- Stačí znovu stisknout tlačítko **"Open Markdown File"** a vybrat jiný soubor.  

---

## ❓ Nejčastější dotazy

### 🔹 Jaký typ souborů mohu otevřít?
Aplikace podporuje pouze soubory s příponou **.md** (Markdown).  

### 🔹 Nevidím žádný obsah, co mám dělat?
Zkontrolujte, zda váš Markdown soubor obsahuje text a není prázdný.  

### 🔹 Jak zavřít aplikaci?
Klikněte na křížek (**X**) v pravém horním rohu okna.  


