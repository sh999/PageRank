import json
import pickle
from pprint import pprint
pages = {}
counter = 0
with open("sitegraph2.json") as inputfile:
	for line in inputfile:
		line = json.loads(line)		
		site = line['url']
		if site[4:5] == "s":
			site = site[5:]
		else:
			site = site[4:]
		links = line['linkedurls']
		links_dict = {}
		for l in links:
			if (l[4:] not in links_dict and (l[4:]+"/") not in links_dict) and (l[5:] not in links_dict and (l[5:]+"/") not in links_dict):
				to_insert = {}
				if l[4:5] == "s":
					to_insert[l[5:]] = 0
					links_dict.update(to_insert)
				else:
					to_insert[l[4:]] = 0
					links_dict.update(to_insert)
		
		pages[site] = links_dict
		if counter % 1000 == 0:
			print counter
		counter += 1
# for k in pages:
# 	print k
outfile = open("out2", "w")
pickle.dump(pages, outfile)
print "Done"
# pprint(pages)
