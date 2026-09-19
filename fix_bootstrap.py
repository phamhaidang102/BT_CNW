import os
import re

def fix_html(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            content = f.read()

    # Fix the double <div class="row"> issue
    content = content.replace('<div class="row">\n<div class="row">\n<div id="links" class="col-md-3">', '<div class="row">\n<div id="links" class="col-md-3">')
    
    # write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = r"d:\Code\2023_BTHTCNWeb_\Tuan4"
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html') or file.endswith('.htmll'):
            filepath = os.path.join(root, file)
            fix_html(filepath)