# Python3 program to find a triplet 
# that sum to a given value

# returns true if there is triplet with
# sum equal to 'sum' present in A[]. 
# Also, prints the triplet
def find3Numbers(A, arr_size, sum):
	ele =0
	res = 0

	# Fix the first element as A[i]
	for i in range( 0, arr_size-2):

		# Fix the second element as A[j]
		for j in range(i + 1, arr_size-1): 
			
			# Now look for the third number
			for k in range(j + 1, arr_size):
				ele = A[i] + A[j] + A[k]
				# print("Triplet is", ele)
				if ele % sum == 0:
					res+=1

	# If we reach here, then no 
	# triplet was found
	return res

# Driver program to test above function 
A = [3,3,4,7,8]
sum = 5
arr_size = len(A)
print(find3Numbers(A, arr_size, sum))