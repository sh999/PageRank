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
def make_site_list(adj_list):
	'''
	Return a collection of unique sites from an adj_list of the web
	'''
	site_list = {}
	num_id = 0				# Numerical id for each unique site
	for i in adj_list:
		site_list[i] = num_id
		num_id += 1
	return site_list
def make_init(site_list):
	pr_vec = [1,2,3,4]
	return pr_vec
def calculate(matrix, vector):
	'''
		One iteration of the pagerank calculation
	'''
	return vector
def rotate(matrix):
	'''
		Given matrix with rows X and cols Y, return a matrix
		 with rows Y and cols X. Necessary for pagerank to convert
		 original adj. list
	'''
	# print "in rotate()"
	rotated = {}
	# pprint(matrix)
	for k, v in matrix.iteritems():
		# print "ITEM",k
		for i in v:
			# print "i:",i," k:",k
			# print "orig:", matrix[k][i]
			to_insert = {}
			to_insert[k] = matrix[k][i]
			# print "to insert:"
			# pprint(to_insert)
			if i not in rotated:
				rotated[i] = {}
			rotated[i].update(to_insert) 
	return rotated
def main():
	damping = 0.85
	adj_list = {"A":{"B":0,"C":0}, "B":{"C":0},"C":{"A":0},"D":{"C":0}}
	unweighted = calc_unweighted(adj_list)	 # Adj list where 1 = link present
	weighted = calc_weighted(adj_list)  	 # Get adj list of raw numbers (1 = outlinks to)
	rotated_weighted = rotate(weighted)		 # Rotate weighted adj list to proper form
	sites_list = make_site_list(adj_list)				 # Each unique site has an integer ID
	pr_vec = make_init(sites_list)					 # Make initial PR vector, which is a vector with unique sites w/ score 1
	result = calculate(weighted, pr_vec)
	print "Initial adj_list"
	pprint(adj_list)
	print "unweighted list"
	pprint(unweighted)
	print "weighted list"
	pprint(weighted)
	print "rotated_weighted"
	pprint(rotated_weighted)
	print "sites_list"
	pprint(sites_list)
	print "pr_vec"
	pprint(pr_vec)
	print "result"
	pprint(result)

def test_rot():
	a = {'A': {'B': 1, 'C': 2}, 'B': {'C': 3}, 'C': {'A': 4}, 'D': {'C': 5}}
	b = {}
	pprint(a)
	for k, v in a.iteritems():
		# print "ITEM",k
		for i in v:
			# print "i:",i," k:",k
			# print "orig:", a[k][i]
			to_insert = {}
			to_insert[k] = a[k][i]
			# print "to insert:"
			# pprint(to_insert)
			if i not in b:
				b[i] = {}
			b[i].update(to_insert)  
	print b
	

main()