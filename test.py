import http
import math
import sys

import requests

print(sys.version)
print(sys.executable)


def greet(person):
    greeting = "hello, {}".format(person)
    return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)
