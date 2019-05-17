first = "XueShao"
last = "Chen"

info = f"My name is {first.upper()} {last.lower()}"
print(info)


person = {"name": "Chen", "age": 30}
print(f"My name is {person['name']} and I am {person['age']}")


for n in range(15):
    print(f"Value is {n:03}")


from datetime import datetime

bday = datetime(2018, 3, 15)
print(f"Birthday is {bday:%b %d, %Y}")

