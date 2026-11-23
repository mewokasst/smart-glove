import re

html = open(r'c:\Users\Diana  C. Francisco\Downloads\Glove_sign\smart_glove_3d_viewer.html', encoding='utf-8').read()
scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
code = '\n'.join(scripts)

# Simple brace/paren/bracket count (not perfect but good enough)
braces = code.count('{') - code.count('}')
parens = code.count('(') - code.count(')')
brackets = code.count('[') - code.count(']')

print(f'Braces balance: {braces}')
print(f'Parens balance: {parens}')
print(f'Brackets balance: {brackets}')
print(f'File size: {len(html)} bytes')
print(f'Has currentBends: {"currentBends" in code}')
print(f'Has targetBends: {"targetBends" in code}')
print(f'Has BEND_LERP_SPEED: {"BEND_LERP_SPEED" in code}')
print('Status:', 'OK' if braces == 0 and parens == 0 and brackets == 0 else 'MISMATCH (may be ok due to string literals)')
