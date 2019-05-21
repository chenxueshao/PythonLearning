import requests

# r = requests.get("https://imgs.xkcd.com/comics/python.png")

# with open("comic.png", "wb") as f:
#     f.write(r.content)

# r.headers r.ok


###### httpbin.org
# payload = {"page": 2, "count": 25}
# r = requests.get("https://httpbin.org/get", params=payload)

# payload = {"username": "chen", "password": "fine"}
# r = requests.post("https://httpbin.org/post", data=payload)

# r_dict = r.json()
# print(r_dict["form"])

# r = requests.get("https://httpbin.org/basic-auth/chen/fine", auth=("chen", "fine"))

r = requests.get("https://httpbin.org/delay/1", timeout=3)

print(r.text)
