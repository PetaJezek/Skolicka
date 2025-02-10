import re

s = "<li>[ ] Hotová položka</li>"

print(re.sub(r'(<li>\[ \])(.*?)(</li>)', r'<span class="checkbox x"></span>\2', s))