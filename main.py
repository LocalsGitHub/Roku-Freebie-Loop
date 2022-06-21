# Credit to Local#5353 | arshan.xyz
import requests
import threading
from time import sleep
import json

with open("myconfig.json", "r") as f:
    parse = json.loads(f.read())
    name1 = parse['first_name']
    name2 = parse['last_name']
    street1 = parse['street1']
    street2 = parse['street2']
    city = parse['city']
    country = parse['country']
    state = parse['state']
    telephone = parse['telephone']
    zipcode = parse['zipcode']
    email = parse['email']
    f.close()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "csrf-token": "CiR7Vryc-C4DsHZb9zuvF4LeXdbGmHfbLF6U",
    "Content-Type": "application/json",
    "Content-Length": "249",
    "Origin": "https://my.roku.com",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://my.roku.com/HDMI",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
}

cookies = {
    "_uc": "736e9a4a-fb68-41f2-9e84-ac50a564644d:74277b16da879e6b05805027841843fa",
    "AWSALB": "1+3/O+8CB1c7FR6ZLg8NRf96WXgafv4AcBuHeZFW6DYk4D7n5D5cjszC0XM2DDXwCeUDX6aAj3r8L58p1rhegkaohkATOCnKcqA/HNP2muvIvrEgEUPeX52LNp0Q",
    "AWSALBCORS": "1+3/O+8CB1c7FR6ZLg8NRf96WXgafv4AcBuHeZFW6DYk4D7n5D5cjszC0XM2DDXwCeUDX6aAj3r8L58p1rhegkaohkATOCnKcqA/HNP2muvIvrEgEUPeX52LNp0Q",
    "_csrf": "ErnRN_7D1XCNtq51Jp3d6JHa",
    "ks.locale": '''j:{"language":"en","country":"US"}''',
    "amoeba": "NkVTTkZuQk1JI0NvbnRyb2wsTE1mMDFuSzJQI0NvbnRyb2wscjc5UVFPU0VnI0NvbnRyb2wsVkw3NzAtOHpmI0NvbnRyb2wseloxblR4ZVBwI0NvbnRyb2wscEJRYXNzT1pzI1Rlc3QsWUNNTkxoSDZpI2ltYWdlc3dhcHBlcnRvcCxDV3JkelgxZ3kjc2VvaGVybywwLXZSSFBLbzIjQ29udHJvbCxnZklNQi1ia0UjQ29udHJvbA==",
    "_usn": "8e666a45-8093-4a40-a8ad-d6bf76a862da",
    "my.state": '''j:{"source":"web","signin_post_redirect":"https://my.roku.com/account/purchases/products","signup_post_redirect":"https://my.roku.com/account/purchases/products"}'''
}

data = f'''{{"esn": "CT386F875324","firstname": "{name1}","lastname": "{name2}","street1": "{street1}","street2": "{street2}","city": "{city}","country": "{country}","state": "{state}","tel": "{telephone}","zip": "{zipcode}","userEmail": "{email}","isLatam": "false"}}'''

def send(iteration):
    req = requests.post("https://my.roku.com/api/v1/hdmi/process?locale=en-US", headers=headers, cookies=cookies, data=data)
    if req.status_code == 201:
        print(f"Success! Will be shipped on {req.json()['date']} | Iteration: {str(iteration)} | Made by: arshan.xyz")
    else:
        print(f"Error: {req.text}\nStatus Code: {req.status_code}")

i = 1
for _ in range(1000):
    threading.Thread(target=send, daemon=True, args=(i,)).start()
    i += 1
    sleep(0.3)