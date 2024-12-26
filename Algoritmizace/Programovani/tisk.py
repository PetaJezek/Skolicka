from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# File path for PDF
file_path = r"C:\Users\petrj\OneDrive - Univerzita Karlova\Skolicka\Algoritmizace\Programovani\lejstro.pdf"

# Create PDF with ReportLab
c = canvas.Canvas(file_path, pagesize=A4)
width, height = A4

# Title
c.setFont("Helvetica-Bold", 14)
c.drawString(50, height - 50, "Veta 6.19 (Maticova reprezentace linearniho zobrazeni)")

# Content
c.setFont("Helvetica", 12)
text = """
Bud f : U → V linearni zobrazeni, BU = {x1, ..., xn} baze prostoru U,
 a BV = {y1, ..., ym} baze prostoru V. 
Pak pro kazde x ∈ U plati:
[f(x)]BV = BV [f]BU · [x]BU. (6.1)

Dukaz
Oznacme A := BV [f]BU. Bud x ∈ U, tedy x = ∑n i=1 αi xi,
 neboli [x]BU = (α1, ..., αn)T. Pak:

1. f(x) = f ( ∑n j=1 αj xj ) = ∑n j=1 αj f(xj)
#2. = ∑n j=1 αj ( ∑m i=1 aij yi )
#3. = ∑n j=1 ∑m i=1 αj aij yi 
#4. = ∑m i=1 ( ∑n j=1 αj aij ) yi.

Tedy vyraz ∑n j=1 αj aij reprezentuje i-tou souradnici
 vektoru [f(x)]BV. Jeho hodnota je ∑n j=1 αj aij = (A · [x]BU )i,
   coz je i-ta slozka vektoru BV [f]BU · [x]BU.

Matice linearniho zobrazeni tedy prevadi souradnice
vektoru vzhledem k dane bazi na souradnice jeho obrazu.
Plne tak popisuje linearni zobrazeni, a navic obraz
libovolneho vektoru muzeme vyjadrit jednoduchym zpusobem
jako nasobeni matici.

Poznamka
Symbol kan oznacuje kanonickou bazi, tj. tu skladanou z 
jednotkovych vektoru.

***
Mam problem pochopit nasledujici cast dukazu: 
Tedy vyraz #∑n j=1 αj aij reprezentuje i-tou souradnici 
vektoru [f(x)]BV, ale jeho hodnota je 
#∑n j=1 αj aij = (A · [x]BU )i.

Prosim o vysvetleni teto casti a vyznamu vztahu
 (A · [x]BU )i pro konkretni priklad nebo vyklad.
"""

# Draw multiline text
text_object = c.beginText(50, height - 80)
text_object.setFont("Helvetica", 12)
text_object.setTextOrigin(50, height - 80)
text_object.textLines(text)
c.drawText(text_object)

# Save PDF
c.save()

print(f"PDF successfully created at {file_path}")