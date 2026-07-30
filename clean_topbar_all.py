#!/usr/bin/env python3
import glob, re

html_files = glob.glob("/home/ssvcharan/Antigravity/LaredoFire/*.html")

for filepath in html_files:
    with open(filepath) as f:
        content = f.read()
    
    # Remove everything between <body> and <!-- Header Navigation --> or <header
    new_content = re.sub(
        r'<body>\s*.*?(?=<header|\x3c!-- Header)',
        '<body>\n\n    ',
        content,
        flags=re.DOTALL
    )
    
    with open(filepath, "w") as f:
        f.write(new_content)

print("Cleanly removed top bar content between <body> and <header> in all HTML files!")
