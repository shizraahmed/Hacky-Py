import requests

ip = requests.get("https://httpbin.org/ip").json()["origin"]

print(ip)
