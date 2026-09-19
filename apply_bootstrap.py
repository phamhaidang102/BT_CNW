import os
import re

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            content = f.read()

    # Apply general bootstrap classes
    
    # 1. Tables
    content = re.sub(r'<table\b([^>]*)>', r'<table class="table table-bordered table-striped"\1>', content)
    
    # 2. Forms and inputs
    content = re.sub(r'<input\b([^>]*)type="(text|password|email|number|tel|date)"', r'<input class="form-control"\1type="\2"', content)
    content = re.sub(r'<select\b', r'<select class="form-select"', content)
    content = re.sub(r'<textarea\b', r'<textarea class="form-control"', content)
    content = re.sub(r'<button\b([^>]*)>', r'<button class="btn btn-primary"\1>', content)
    content = re.sub(r'<input\b([^>]*)type="(submit|button|reset)"', r'<input class="btn btn-primary"\1type="\2"', content)
    
    # 3. Layout (specifically for Tuan2/Bai4 files like home.html, maze.html etc.)
    # Wrap body contents in container
    if 'class="container"' not in content:
        content = re.sub(r'(<body[^>]*>)', r'\1\n<div class="container">\n', content)
        content = re.sub(r'(</body>)', r'</div>\n\1', content)
        
    # Wrap links and noidung in a row
    if 'id="links"' in content and 'id="noidung"' in content and 'class="row"' not in content:
        content = content.replace('<div id="links">', '<div class="row">\n<div id="links" class="col-md-3">')
        content = content.replace('<div id="links" class="col-md-3"', '<div class="row">\n<div id="links" class="col-md-3"')
        content = content.replace('<div id="noidung">', '<div id="noidung" class="col-md-9">')
        content = content.replace('<div id="noidung" class="col-md-9"', '<div id="noidung" class="col-md-9"')
        content = content.replace('<address>', '</div><!-- end row -->\n<address>')

    # 4. Images
    content = re.sub(r'<img\b(?![^>]*class=")', r'<img class="img-fluid" ', content)

    # write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = r"d:\Code\2023_BTHTCNWeb_\Tuan4"
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html') or file.endswith('.htmll'):
            filepath = os.path.join(root, file)
            print(f"Processing {filepath}")
            process_file(filepath)