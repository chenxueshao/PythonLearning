from collections import namedtuple

Color = namedtuple("olor", ["red", "green", "blue"])
color = Color(55, 155, 255)

print(type(Color))
print(color.red)
