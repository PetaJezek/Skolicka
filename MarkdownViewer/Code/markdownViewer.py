import ctypes
import re
import tkinter as tk
from tkinter import filedialog
from tkinterweb import HtmlFrame
import markdown
from markdown.extensions import toc  # například pro generování TOC (Table of Contents)
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from markdown.extensions.toc import TocExtension
import webbrowser
import unicodedata



ctypes.windll.shcore.SetProcessDpiAwareness(True) #reseni pro lepsi rozliseni (nalezeno na stackoverflow)

class CustomHeaderIdProcessor(Treeprocessor):
    def generate_id(self, text):
        """Upravit text pro vytvoření bezpečného ID."""

        #  Převést text na malá písmena
        text = text.lower()
        
        # Nahradit mezery pomlčkami
        text = text.replace(" ", "-")


        return text
        
class CustomHeaderIdExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(CustomHeaderIdProcessor(md), "custom_header_id", 25)

def remove_accents(text):
    """
    Convert accented characters to their closest ASCII equivalent.
    """
    return ''.join(
        c for c in unicodedata.normalize('NFKD', text) if unicodedata.category(c) != 'Mn'
    )


def modify_ids(html_content):
    """
    Ensure all 'href' attributes use lowercase and keep special characters.
    """
    def transform_href(match):
        new_href = match.group(1).lower()
        new_href = remove_accents(new_href)
        return f'href="#{new_href}"'
    
    # Modify href attributes that reference the ids
    html_content = re.sub(r'href="#([^"]+)"', transform_href, html_content)

    return html_content


def load_markdown(): 
    #Funkce ktera nacita md soubour a nasledne ho prevadi na html
    file_path = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md"), ("All files", "*.*")])
    
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            # Read the markdown file content
            md_content = file.read()
            
            # Convert the markdown content to HTML
            html_content = markdown.markdown(md_content, extensions=['sane_lists',  toc.TocExtension(), 'extra', 'codehilite', 'mdx_truly_sane_lists', CustomHeaderIdExtension()], output_format="html5")
            #Modify the ids so it can 
            html_content = modify_ids(html_content)
            
            print(html_content)
            # Handle strikethrough by replacing 
            html_content = re.sub(r'~~(.*?)~~', r'<del>\1</del>', html_content)
            
            # Handle checkboxes
            html_content = re.sub(r'(\[x\])(.*?)', r'<span class="checkbox x"></span>\2', html_content)
            html_content = re.sub(r'(\[ \])(.*?)', r'<span class="checkbox"></span>\2', html_content)
            
            # Wrap the HTML content with the smooth scroll JavaScript
            full_html_content = f"""
            <html>
                <head>
                    <script>
                        // Custom script to handle anchor links and scroll
                        document.addEventListener("DOMContentLoaded", function() {{
                            var links = document.querySelectorAll('a[href^="#"]');
                            links.forEach(function(link) {{
                                link.addEventListener('click', function(e) {{
                                    var target = document.querySelector(this.getAttribute("href"));
                                    if (target) {{
                                        window.scrollTo({{
                                            top: target.offsetTop,
                                            behavior: "smooth"
                                        }});
                                        e.preventDefault();  // Prevent default anchor jump behavior
                                    }}
                                }});
                            }});
                        }});
                    </script>
                </head>
                <body>
                    {html_content}  <!-- Insert the converted HTML content here -->
                </body>
            </html>
            """
            # Load the HTML content into the HTML frame (e.g., a Tkinter HTML display widget)
            html_frame.load_html(full_html_content)
            
            # add custom CSS
            html_frame.add_css(css) 



def open_link(url):
    #funkce na otvirani linků (href)
    if "#" in url:
        html_frame.load_url(url)
    else:
        webbrowser.open(url)
# Vytvoření hlavního okna aplikace
root = tk.Tk()
root.title("Markdown Viewer")
root.state('zoomed')

# Tlačítko pro načtení Markdown souboru
btn_load = tk.Button(root, text="Open Markdown File", command=load_markdown)
btn_load.pack(pady=10)

#zakladni nastaveni zobrazovaneho html
html_frame = HtmlFrame(root, horizontal_scrollbar="auto", messages_enabled = False )
html_frame.pack(fill="both", expand=True)
html_frame.on_link_click(open_link)

#pridani css
with open('../Code/abyToByloHezke.css', 'r', encoding='utf-8') as file:
    css = file.read()
html_frame.add_css(css)

root.mainloop()
