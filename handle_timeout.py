import requests

url = "https://www.google.com/search?q=nike+shoes"

try:
    res = requests.get(url, timeout=0.075)
    with open('content.html', 'w+') as file:
        file.write(res.text)
except requests.exceptions.ReadTimeout:
    print("Error: Request Timed Out")
