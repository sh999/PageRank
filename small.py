'''
small.py
Do pagerank on small networks
'''
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
	'''
	weighted = copy.deepcopy(adj_list)
	for k, v in weighted.iteritems():
		# print "site:", k
		# print "# links:", len(v)
		# print "links:", v
		for name in v:
			v[name] = 1.0/len(v)
		# print ""
	# pprint(weighted)
	return weighted
def make_site_list(adj_list):
	'''
	Return a collection of unique sites from an adj_list of the web
	'''
	site_list = {}
	num_id = 1				# Numerical id for each unique site
	# pprint(adj_list)
	for i in adj_list:
		for j in adj_list[i]:
			# print "inserting j:",j
			if j not in site_list:
				# print "j not in site_list"
				site_list[j] = num_id
				num_id += 1
			else:
				# print "j in site_list"
				pass
	return site_list
def make_init(site_list):
	i = 1
	pr_vec = {}
	for pg in site_list:
		pr_vec[pg] = i 
		# i += 1
	# pr_vec = [1,2,3,4]
	print "pr_vec:"
	pprint(pr_vec)
	return pr_vec
def matrix_times_vector(matrix, vector):
	'''
		One iteration of the pagerank calculation
	'''
	# pprint(matrix)
	# pprint(vector)
	pr_vector = {}	
	for row in vector:						# Loop through result vector
		# print "\npr row:", row
		curr_sum = 0
		if row in matrix:
			# print "matrix[row]:", matrix[row]
			for elem in matrix[row]:		# Loop through matrix row	
				# print "multiplying", elem, ":", matrix[row][elem], "by", vector[row]
				mult = matrix[row][elem] * vector[row]		# Multiply matrix row by vector column
				curr_sum += mult 			# Sum terms successively
			# print "curr_sum:", curr_sum
		pr_vector[row] = curr_sum
	# pprint(pr_vector)
	return pr_vector
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
def scalar_times_matrix(scalar, matrix):
	'''
		Multiply scalar times matrix.
		Important for, say, alpha times S 
	'''
	result = {}
	pprint(matrix)
	for k, v in matrix.iteritems(): 	# Loop through matrix row elements
		# print "k:", k
		to_insert = {} 					# Temporary row element to insert
		for i in v: 					# Loop through columns
			to_insert[i] = scalar * matrix[k][i] 	# Multiply same scalar by each element for all elements in row
			# print "\tto_insert\t",
			# pprint(to_insert)
			to_insert.update(to_insert) 	# Putative row to insert
			# print ""
		result[k] = to_insert 			# Insert multiple elements (row)
	return result
def main():
	damping = 0.85  			# Damping factor
	inv_damping = 1 - damping
	# adj_list = {"A":{"B":0,"C":0}, "B":{"C":0},"C":{"A":0},"D":{"C":0}}
	adj_list = {"H":{"Ab":0,"P":0,"L":0}, "Ab":{"H":0},"P":{"H":0},"L":{"H":0,"A":0,"B":0,"C":0,"D":0,}}
	unweighted = calc_unweighted(adj_list)	 # Adj list where 1 = link present
	weighted = calc_weighted(adj_list)  	 # Get adj list of raw numbers (1 = outlinks to)
	rotated_weighted = rotate(weighted)		 # Rotate weighted adj list to proper form
	rotated_weighted_damping = scalar_times_matrix(damping,rotated_weighted)		 # Multiply weighted matrix by damping factor (alpha * S)
	sites_list = make_site_list(adj_list)				 # Each unique site has an integer ID
	pr_vec = make_init(sites_list)					 # Make initial PR vector, which is a vector with unique sites w/ score 1
	result = matrix_times_vector(rotated_weighted, pr_vec)
	print "\nInitial adj_list"
	pprint(adj_list)
	print "\nunweighted list"
	pprint(unweighted)
	print "\nweighted list"
	pprint(weighted)
	print "\nrotated_weighted"
	pprint(rotated_weighted)
	print "\nsites_list"
	pprint(sites_list)
	print "\npr_vec init"
	pprint(pr_vec)
	print "\nrotated_weighted times pr_vec"
	pprint(result)
	print "\nrotated weighted times damping"
	pprint(rotated_weighted_damping)


main()