import requests
import os

qq = os.environ['qq']

print(qq)

url = f'http://api.qdikun.com/api/qqmusic/?qq={qq}'

response = requests.get(url)

print(response.text)

url =f'https://dachebijia.001api.com/Api/qy?qq={qq}&t=1'

response = requests.get(url)

print(response.json()['msg']+'增加5小时')
