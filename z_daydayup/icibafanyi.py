import requests
import json

url = 'http://fy.iciba.com/ajax.php?a=fy'

params = {
    # "f": "hhh",
    # "t": "kkk",
    "w": "test"
}

r = requests.request("post", url, params=params)

# print(r.text)

d = json.loads(r.text)
print(d["content"]["word_mean"])
