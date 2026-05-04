import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all remaining temporary amazon links with the real storefront URL
old_url = 'https://www.amazon.com.br'
new_url = 'https://www.amazon.com.br/s?me=A2FL1W3S46MFWA&marketplaceID=A2Q3Y263D00KWC'

content = content.replace(old_url, new_url)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated all external links to Amazon Storefront.")
