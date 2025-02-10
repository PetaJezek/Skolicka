import tkinter as tk
from tkinter import filedialog
import re

def load_markdown():
    file_path = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            md_content = file.read()
            display_markdown(md_content)

def display_markdown(md_content):
    text_widget.config(state=tk.NORMAL)
    text_widget.delete("1.0", tk.END)
    
    in_code_block = False
    for line in md_content.split("\n"):
        if  "```" in line:
            in_code_block = not in_code_block
            continue

        if in_code_block:  # Zobrazí víceřádkový kód
            text_widget.insert(tk.END, line + "\n", "code")
            continue

        if re.match(r"^# ", line):
            line = line[2:]
            text_widget.insert(tk.END, line + "\n", "h1")
        elif re.match(r"^## ", line):
            line = line[3:]
            text_widget.insert(tk.END, line + "\n", "h2")
        elif re.match(r"^### ", line):
            line = line[4:]
            text_widget.insert(tk.END, line + "\n", "h3")
        elif re.match(r"^#### ", line):
            line = line[5:]
            text_widget.insert(tk.END, line + "\n", "h4")
        elif re.match(r"^> ", line):  # Bloková citace
            text_widget.insert(tk.END, line + "\n", "quote")
        elif re.match(r"^- \[ \]", line):  # Nezaškrtnutý checkbox
            text_widget.insert(tk.END, "☐ " + line[4:] + "\n", "checklist")
        elif re.match(r"^- \[x\]", line, re.IGNORECASE):  # Zaškrtnutý checkbox
            text_widget.insert(tk.END, "✔ " + line[4:] + "\n", "checked")
        elif re.match(r"^- ", line) or re.match(r"^\d+\.", line):  # Seznamy
            text_widget.insert(tk.END, line + "\n", "list")
        elif "|" in line:  # Detekce tabulky
            text_widget.insert(tk.END, line + "\n", "table")
        elif re.search(r"\*\*(.*?)\*\*", line):  # Tučné písmo
            bold_text = re.sub(r"\*\*(.*?)\*\*", r"\1", line)
            text_widget.insert(tk.END, bold_text + "\n", "bold")
        elif re.search(r"\*(.*?)\*", line):  # Kurzíva
            italic_text = re.sub(r"\*(.*?)\*", r"\1", line)
            text_widget.insert(tk.END, italic_text + "\n", "italic")
        elif re.search(r"~~(.*?)~~", line):  # Přeškrtnutý text
            strike_text = re.sub(r"~~(.*?)~~", r"\1", line)
            text_widget.insert(tk.END, strike_text + "\n", "strikethrough")
        elif re.search(r"\[(.*?)\]\((.*?)\)", line):  # Odkazy
            match = re.search(r"\[(.*?)\]\((.*?)\)", line)
            if match:
                text_widget.insert(tk.END, match.group(1), "link")
            text_widget.insert(tk.END, "\n")
        else:
            text_widget.insert(tk.END, line + "\n")

    text_widget.config(state=tk.DISABLED)

# Vytvoření hlavního okna aplikace
root = tk.Tk()
root.title("Markdown Viewer")
root.geometry("800x600")

# Tlačítko pro načtení Markdown souboru
btn_load = tk.Button(root, text="Open Markdown File", command=load_markdown)
btn_load.pack(pady=10)

# Vytvoření textového widgetu pro zobrazení Markdown
text_widget = tk.Text(root, wrap="word", font=("Arial", 12))
text_widget.pack(fill="both", expand=True, padx=10, pady=10)

# Konfigurace stylů pro různé typy Markdown prvků
text_widget.tag_configure("h1", font=("Arial", 18, "bold"))
text_widget.tag_configure("h2", font=("Arial", 16, "bold"))
text_widget.tag_configure("h3", font=("Arial", 14, "bold"))
text_widget.tag_configure("h4", font=("Arial", 13, "bold"))
text_widget.tag_configure("bold", font=("Arial", 12, "bold"))
text_widget.tag_configure("italic", font=("Arial", 12, "italic"))
text_widget.tag_configure("strikethrough", font=("Arial", 12, "overstrike"))
text_widget.tag_configure("quote", font=("Arial", 12, "italic"), foreground="gray")
text_widget.tag_configure("list", font=("Arial", 12))
text_widget.tag_configure("checklist", font=("Arial", 12), foreground="blue")
text_widget.tag_configure("checked", font=("Arial", 12), foreground="green")
text_widget.tag_configure("table", font=("Courier", 12))
text_widget.tag_configure("code", font=("Courier", 12, "bold"), background="#f4f4f4")
text_widget.tag_configure("link", font=("Arial", 12, "underline"), foreground="blue")

root.mainloop()
