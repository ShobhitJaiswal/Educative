# Python program for the above approach

# Function to find the number of moves
# required to make the string empty.
def numberOfMoves(str, n):

	# If the first and the last
	# character are different
	if (str[0] != str[n - 1]):
		print("1")
		return

	# Check if there is a index i such that
	# s[i] != s[0] and s[i+1] != s[n-1]
	for i in range(0, len(str)):
		if (str[i] != str[0] and
			str[i + 1] != str[n - 1]):
				
			print("2")
			return

	# If no such index exists then
	# the answer is -1
	print(-1)
	return

# Driver Code
if __name__ == '__main__':
	
	str = "baabacaa"
	n = len(str)
	numberOfMoves(str, n)

	# This code is contributed by Samim Hossain Mondal.
