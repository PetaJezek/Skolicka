import ctypes
import re
import tkinter as tk
from tkinter import filedialog
import markdown
from tkinterweb import HtmlFrame
import markdown
from markdown.extensions import toc  # například pro generování TOC (Table of Contents)
import tkinter.font as tkFont


ctypes.windll.shcore.SetProcessDpiAwareness(True) #reseni pro lepsi rozliseni (nalezeno na stackoverflow)




    
#Funkce ktera nacita md soubour a nasledne ho prevadi na html 
def load_markdown():
    

    file_path = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            
            md_content = file.read()
            md_content = markdown.markdown(md_content, extensions=['sane_lists', 'extra', 'codehilite', 'mdx_truly_sane_lists', toc.TocExtension(), ]) #exstension -> maji nastarosti spravny prechod z md do html
            html_content = markdown.markdown(md_content)
            print(md_content)
            html_content = re.sub(r'~~(.*?)~~', r'<del>\1</del>', html_content) #aby fungovalo proskrtavani
            
            html_content = re.sub(r'(\[x\])(.*?)', r'<span class="checkbox x"></span>\2', html_content)
            html_content = re.sub(r'(\[ \])(.*?)', r'<span class="checkbox"></span>\2', html_content)
            

            print(html_content)
            html_frame.load_html(html_content)
            html_frame.add_css(css)
# Vytvoření hlavního okna aplikace
root = tk.Tk()
  # Zvýší rozlišení pro vysoké DPI
root.title("Markdown Viewer")
root.state('zoomed')

# Tlačítko pro načtení Markdown souboru
btn_load = tk.Button(root, text="Open Markdown File", command=load_markdown)
btn_load.pack(pady=10)

html_frame = HtmlFrame(root, horizontal_scrollbar="auto", messages_enabled = False )
html_frame.pack(fill="both", expand=True)


with open('MarkdownViewer\\abyToByloHezke.css', 'r', encoding='utf-8') as file:
    css = file.read()
html_frame.add_css(css)


root.mainloop()
