"""
Read data from a JSON file
"""

import json
import io
import requests

"""
The following reads from a file
file = input ("Please type in a file name")
with io.open(file, 'r', encoding='utf8') as f:
    text = f.read()

data = json.loads(text)
"""
link = "http://api.nobelprize.org/v1/prize.json"
data = json.loads(requests.get(link).text)

year = input("Please type in a year")
cat = input("Please type in the category")
cat = cat.lower()

for item in data["prizes"]:
    if item["year"] == year and item["category"] == cat:
        # print (item)
        for person in item["laureates"]:
            print(person["firstname"], person["surname"])
