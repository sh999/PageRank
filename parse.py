'''
parse.py
Parses json links file to appropriate data structure for pagerank
'''
with open("test.json") as inputfile:
	for line in inputfile:
		print line