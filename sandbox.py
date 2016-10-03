from pprint import pprint
import copy
def calc_unweighted(adj_list):
	'''
		Return adj list based on link presence; if link to a site, element is 1
	'''
	unweighted = copy.deepcopy(adj_list)
	for k, v in unweighted.iteritems():
		# print "site:", k
		# print "links:", v
		for name in v:
			v[name] = 1
		# print ""
	# pprint(unweighted)
	return unweighted

def calc_weighted(adj_list):
	'''
		Return adj list based on # of sites (vote dilution); if link to 3 sites, each element is 1/3
		However, this is in inverse, so 1/3 becomes 3
	'''
	weighted = copy.deepcopy(adj_list)
	for k, v in weighted.iteritems():
		# print "site:", k
		# print "# links:", len(v)
		# print "links:", v
		for name in v:
			v[name] = len(v)
		# print ""
	# pprint(weighted)
	return weighted
def site_list(adj_list):
	'''
	Return a collection of unique sites
	'''
	pass

adj_list = {"A":{"B":0,"C":0}, "B":{"C":0},"C":{"A":0},"D":{"C":0}}
unweighted = calc_unweighted(adj_list)	 # Adj list where 1 = link present
weighted = calc_weighted(adj_list)  	 # Get adj list of raw numbers (1 = outlinks to)
pprint(adj_list)
pprint(unweighted)
pprint(weighted)
