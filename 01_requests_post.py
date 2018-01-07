import requests
import json
url = "https://cn.tecdoc.net/?auth=login"
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64)'
                         'AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/63.0.3239.108 Safari/537.36'}
s = requests.session()

data = {'username': 'XXXXXX', 'password': 'XXXXXX'}
s.post(url,data=data, headers=headers)

r = s.get('https://cn.tecdoc.net/_chooser/mfrs?year=&mfr=&model=&vehicle_type=&ctx=%2F&ltt=ktype&lang=zh')
r.encoding = r.apparent_encoding
str_json = json.loads(r.text)
for name in str_json:
    print(name)
