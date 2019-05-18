import json
from urllib.request import urlopen

with urlopen(
    "https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json"
) as response:
    source = response.read()

print(source)


# people_string = """
# {
#     "people":[
#         {
#             "name":"John Smith",
#             "phone":"615-555-7164",
#             "emails":["johnsmith@gogusemail.com","john.smith@work-place.com"],
#             "has_license":false

#         },
#         {
#             "name":"Jane Doe",
#             "phone":"560-555-5153",
#             "emails":null,
#             "has_license":true
#         }
#     ]
# }
# """

# data = json.loads(people_string)

# # print(type(data["people"]))
# for person in data["people"]:
#     del person["phone"]

# new_string = json.dumps(data, indent=2, sort_keys=True)

# print(new_string)
