import re, urllib.request
html = urllib.request.urlopen('https://manirajdeva.github.io/weddingcard/index.html').read().decode('utf-8', errors='replace')
print('has images refs:', 'images/bride-story.jpg' in html, 'images/bride-hero.jpg' in html)
print('has Images refs:', 'Images/bride-story.jpg' in html, 'Images/bride-hero.jpg' in html)
for name in ['bride-story.jpg','bride-hero.jpg','groom-moment.webp']:
    m = re.search(r'(["\'])([^"\']*' + re.escape(name) + r')["\']', html)
    print(name, '=>', m.group(2) if m else 'NOTFOUND')
print('\nMATCH LINES:')
for line in html.splitlines():
    if 'images/' in line or 'Images/' in line:
        if 'src=' in line or 'url(' in line:
            print(line.strip())
