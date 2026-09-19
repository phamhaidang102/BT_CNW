import os
import re

base_dir = r"d:\Code\2023_BTHTCNWeb_\Tuan4"

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            content = f.read()
            
    # 1. Remove all custom style tags
    content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
        
    # 2. Remove all custom CSS links (keep bootstrap)
    # We match <link ...> and only remove if it doesn't contain bootstrap
    def link_replacer(match):
        if 'bootstrap' in match.group(0):
            return match.group(0)
        return ''
    content = re.sub(r'<link[^>]*rel=["\']stylesheet["\'][^>]*>', link_replacer, content)
    
    # 3. Add Bootstrap classes via regex
    # H1
    content = re.sub(r'<h1\b([^>]*)>', r'<h1 class="text-primary text-center my-3"\1>', content)
        
    # H2
    content = re.sub(r'<h2\b([^>]*)>', r'<h2 class="text-white bg-success p-2 mt-4"\1>', content)
        
    # H3
    content = re.sub(r'<h3\b([^>]*)>', r'<h3 class="text-white bg-success p-2 w-50 mt-3"\1>', content)

    # Page container (for bai2a, bai2b, etc)
    content = re.sub(r'<div\s+id=["\']page["\']>', r'<div id="page" class="card p-4 shadow my-4 border-0">', content)
        
    # Sidebar links (for Bai4 farm)
    content = re.sub(r'<div\s+id=["\']links["\']([^>]*)>', r'<div id="links" class="col-md-3 list-group mb-4">', content)
    
    # Links inside #links
    # Since regex can't easily parse nested scope, we'll do a simple replace if we know the structure
    
    # Main content (for Bai4 farm)
    content = re.sub(r'<div\s+id=["\']noidung["\']([^>]*)>', r'<div id="noidung" class="col-md-9 bg-dark text-white p-4 rounded">', content)

    # Address
    content = re.sub(r'<address>', r'<address class="text-center border-top pt-3 mt-4 text-muted small">', content)

    # Body background for farm
    content = re.sub(r'<body\b([^>]*)>', r'<body class="bg-light"\1>', content)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html') or file.endswith('.htmll'):
            filepath = os.path.join(root, file)
            process_file(filepath)