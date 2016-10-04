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
def make_init_pr_vec(site_list):
	i = 1.0/len(site_list)
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
	pprint(matrix)
	pprint(vector)
	pr_vector = {}	
	for row in vector:						# Loop through result vector
		print "\npr row:", row
		curr_sum = 0
		if row in matrix:
			print "matrix[row]:", matrix[row]
			for elem in matrix[row]:		# Loop through matrix row	
				print "multiplying", elem, ":", matrix[row][elem], "by", vector[row]
				mult = matrix[row][elem] * vector[elem]		# Multiply matrix row by vector column
				curr_sum += mult 			# Sum terms successively
			print "curr_sum:", curr_sum
		pr_vector[row] = curr_sum
	print "Matrix times vector:"
	pprint(pr_vector)
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
	# pprint(matrix)
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
def surfer_times_pr(inv_damping,vector):
	'''
		Multiplies "Matrix" of random surfer (term 2 of equation)
		 by pagerank vector
		But not really storing surfer matrix because it's full
		Instead, multiply element by element
	'''
	# pr_vector = {}	
	# for row in vector:						# Loop through result vector
	# 	# print "\npr row:", row
	# 	curr_sum = 0
	# 	print "len:" len
	# 	for i in range(0, len(vector)):
	# 		print "hey"
	# 	# if row in matrix:
	# 	# 	# print "matrix[row]:", matrix[row]
	# 	# 	for elem in matrix[row]:		# Loop through matrix row	
	# 	# 		# print "multiplying", elem, ":", matrix[row][elem], "by", vector[row]
	# 	# 		mult = matrix[row][elem] * vector[row]		# Multiply matrix row by vector column
	# 	# 		curr_sum += mult 			# Sum terms successively
	# 		# print "curr_sum:", curr_sum
	# 	pr_vector[row] = curr_sum
	# # pprint(pr_vector)
	# return pr_vector
	sum_of_vec_elements = 0
	for k in vector:
		sum_of_vec_elements = sum_of_vec_elements + vector[k]
	factor = sum_of_vec_elements * inv_damping / len(vector)	
	# print "sum:", sum_of_vec_elements
	return factor
def add_faux_matrices(matrix, faux_matrix):
	'''
		Does the final addition of pagerank iteration of form:
		matrix + faux_matrix
		where faux_matrix is the pagerank vector after multiplied by surfer matrix
	'''
	result = {}
	for k, v in matrix.iteritems():
		to_insert = {}
		for i in v:
			to_insert[i] = faux_matrix + matrix[k][i] 	# Multiply same scalar by each element for all elements in row
			# print "\tto_insert\t",
			# pprint(to_insert)
			to_insert.update(to_insert) 	# Putative row to insert
			# print ""
		result[k] = to_insert 			# Insert multiple elements (row)
	return result
def add_vectors(vector1, vector2):
	'''
		After distributing the pr vectors, add them together
		vector2 is not really a vector; it's a number but represents vector
		 filled with the same number
	'''
	result = {}
	for k in vector1:
		# print "k:", k
		# print "vector1[k]:", vector1[k]
		result[k] = vector1[k] + vector2
	return result

def test_onestep():
	damping = 0.85  			# Damping factor
	inv_damping = 1 - damping
	# adj_list = {"A":{"B":0,"C":0}, "B":{"C":0},"C":{"A":0},"D":{"C":0}}
	adj_list = {"H":{"Ab":0,"P":0,"L":0}, "Ab":{"H":0},"P":{"H":0},"L":{"H":0,"A":0,"B":0,"C":0,"D":0,}}
	adj_list = {"1":{"2":0,"3":0,"4":0},"2":{"3":0,"4":0},"3":{"1":0},"4":{"1":0,"3":0}}
	unweighted = calc_unweighted(adj_list)	 # Adj list where 1 = link present
	weighted = calc_weighted(adj_list)  	 # Get adj list of raw numbers (1 = outlinks to)
	rotated_weighted = rotate(weighted)		 # Rotate weighted adj list to proper form
	rotated_weighted_damping = scalar_times_matrix(damping,rotated_weighted)		 # Multiply weighted matrix by damping factor (alpha * S)
	sites_list = make_site_list(adj_list)				 # Each unique site has an integer ID
	pr_vec = make_init_pr_vec(sites_list)					 # Make initial PR vector, which is a vector with unique sites w/ score 1
	rw_v = matrix_times_vector(rotated_weighted, pr_vec)
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
	pprint(rw_v)
	print "\nrotated weighted times damping"
	pprint(rotated_weighted_damping)
	print "\nterm1:"
	term1 = matrix_times_vector(rotated_weighted_damping, pr_vec)
	pprint(term1)
	print "\nterm2:"
	term2 = surfer_times_pr(inv_damping,pr_vec)
	pprint(term2)
	print "\nadded together:"
	added = add_vectors(term1,term2)
	pprint(added)
	print "\n------------"
	print "Multiplying vector:"
	pprint(rotated_weighted)
	print "By vector"
	pprint(rw_v)
	print "\nResult:rotated_weighted times prev pr_vec"
	round2 = matrix_times_vector(rotated_weighted, rw_v)
	pprint(round2)
	round3 = matrix_times_vector(rotated_weighted, round2)

def one_iteration(damping, matrix, pr_vector):
	new_pr_vector = {}
	inv_damping = 1 - damping
	# adj_list = {"A":{"B":0,"C":0}, "B":{"C":0},"C":{"A":0},"D":{"C":0}}
	# sites_list = make_site_list(adj_list)				 # Each unique site has an integer ID
	# pr_vec = make_init_pr_vec(sites_list)					 # Make initial PR vector, which is a vector with unique sites w/ score 1
	# rw_v = matrix_times_vector(rotated_weighted, pr_vector)
	#term1 = matrix_times_vector(rotated_weighted_damping, pr_vector)
	#term2 = surfer_times_pr(inv_damping,pr_vector)
	term1 = matrix_times_vector(matrix, pr_vector)
	term2 = surfer_times_pr(inv_damping,pr_vector)
	added = add_vectors(term1,term2)

	print"\nterm1:"
	pprint(term1)
	print "\nterm2:"
	pprint(term2)
	print "\nadded:"
	pprint(added)
	print ""
	return added
def sum_vector(vector):
	'''
		For normalizing the values of the pagerank vector so they add to 1
	'''
	summed = 0
	for i in vector:
		summed += vector[i]
	return summed
def normalize(vector):
	'''
		For normalizing the values of the pagerank vector so they add to 1
	'''
	summed = 0
	for i in vector:
		summed += vector[i]
	for i in vector:
		vector[i] = vector[i]/summed
	return vector
def looping():
	damping = 0.85 
	adj_list = {"H":{"Ab":0,"P":0,"L":0}, "Ab":{"H":0},"P":{"H":0},"L":{"H":0,"A":0,"B":0,"C":0,"D":0,}}
#	adj_list = {"A":{"B":0,"C":0}, "B":{"C":0},"C":{"A":0},"D":{"C":0}}
	#adj_list = {"1":{"2":0,"3":0,"4":0},"2":{"3":0,"4":0},"3":{"1":0},"4":{"1":0,"3":0}}
	pr_vector = make_init_pr_vec(make_site_list(adj_list))
	unweighted = calc_unweighted(adj_list)	 # Adj list where 1 = link present
	weighted = calc_weighted(adj_list)  	 # Get adj list of raw numbers (1 = outlinks to)
	rotated_weighted = rotate(weighted)		 # Rotate weighted adj list to proper form
	rotated_weighted_damping = scalar_times_matrix(damping,rotated_weighted)		 # Multiply weighted matrix by damping factor (alpha * S)
	print "\norig pr:"
	pprint(pr_vector)
	pr = one_iteration(damping, rotated_weighted_damping, pr_vector)
	limit = 30
	iterations = 0
	while(iterations < limit):
		print "\n-------------"
		print "\nRun iteration ", iterations
		pr = one_iteration(damping, rotated_weighted_damping, pr)
		print "\nsummed:", sum_vector(pr)
		iterations += 1
# pr = one_iteration(damping, adj_list, pr)
# pprint(pr)
# pr = one_iteration(damping, adj_list, pr)
# pprint(pr)
#test_onestep()
looping()
