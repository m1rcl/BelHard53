import requests

url = 'http://127.0.0.1:7777'

res = requests.get(url)

text2 = res.text
print(text2)