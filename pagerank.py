# pagerank.py
# Given input of a file with JSON objects showing adj. list for sites in a domain
#  Calculate the pageranks for sites in the domain
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