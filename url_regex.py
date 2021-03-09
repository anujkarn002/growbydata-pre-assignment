import re

urls = [
    'http://www.stackoverflow.com',
    'https://www.github.com',
    'www.example.net',
    'nepal.gov.np',
]

domains = []

for url in urls:
    result = re.search('([^.]+)(?:\.(?:gov\.np|[^.]+(?:$)))', url)
    domains.append(result.group(1))

print(domains)
