import json
from pprint import pprint

a = open("graph1.json", "r")
# print a.readlines()
for i in a.readlines():
	e = eval(i)
	pprint(e)
# with open('try.json') as data_file:    
#     data = json.load(data_file)

# pprint(data)