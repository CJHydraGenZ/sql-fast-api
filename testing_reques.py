from email import header
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Referer': 'https://google.com',
    'DNT': '1',
    'Cahya': 'sahhda'
}

url = 'https://komiku.id/ch/bakemonogatari-chapter-100/'
r = requests.get(url)


print(r.text)
print(r.status_code)
