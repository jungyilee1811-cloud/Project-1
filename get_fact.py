import requests
url="https://uselessfacts.jsph.pl/api/v2/facts/random"
response=requests.get(url)
data=response.json()
if response.status_code==200:
        print(data["text"])
