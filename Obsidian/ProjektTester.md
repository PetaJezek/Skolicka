
## Table of Contents 📝
- [Introduction](#introduction)
- [Emojis Galore](#emojis-galore)
- [Menší nadpis (H3)](#Menší-nadpis-H3)

## Introduction 
Markdown is an easy way to format text and add some cool elements to your documents! 📝💻 Let's see how emojis can enhance your writing! 😊

## Emojis Galore
Here are some fun emojis you can use:




# Hlavní nadpis (H1)

## Podnadpis (H2)

### Menší nadpis (H3)

#### Nejmenší nadpis (H4)

---
**Toto je tučný text**

*Toto je kurzíva*

***Toto je tučné a kurzívní***

~~Toto je přeškrtnutý text~~

---

> Toto je bloková citace.  
> Může mít více řádků.
> Může mít spusty i více řádků.

---

### Seznamy
- Nečíslovaný seznam, položka 1
- Nečíslovaný seznam, položka 2
  - Vnořená položka 1
   - Vnořená položka 2

1. Číslovaný seznam, položka 1
2. Číslovaný seznam, položka 2
  1. Vnořená položka 1
  2. Vnořená položka 2

---

### Kódové bloky

Jednoduchý inline kód: `print("Hello, world!")`

Víceřádkový kód:

```python
def load_markdown():
    file_path = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            md_content = file.read()
            display_markdown(md_content)

def display_markdown(md_content):
    text_widget.config(state=tk.NORMAL) #CO SE DEJE
    text_widget.delete("1.0", tk.END)
    
    in_code_block = False
    for line in md_content.split("\n"):
        if  "```" in line:
            in_code_block = not in_code_block
            continue
```

---

### Odkazy a obrázky

[Odkaz na Youtube](https://www.youtube.com)



![Markdown Logo](https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg)

---

### Tabulky

| Jméno    | Věk | Město    |
|----------|----|---------|
| Alice    | 25 | Praha   |
| Bob      | 30 | Brno    |
| Charlie  | 35 | Ostrava |

---

### Check-list

- [x] Hotová položka
- [x] Nehotová položka
- [ ] Další nehotová položka

---

Tohle pokrývá téměř všechny možnosti Markdownu! 🚀


