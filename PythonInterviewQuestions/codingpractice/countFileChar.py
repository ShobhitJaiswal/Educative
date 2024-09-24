# Program to get letter count in a text file

# explicit function to return the letter count
def letterFrequency(fileName, letter):
	# open file in read mode
	file = open(fileName, "r")

	# store content of the file in a variable
	text = file.read()

	# declare count variable
	count = 0

	# iterate through each character
	for char in text:

		# compare each character with
		# the given letter
		if char == letter:
			count += 1

	# return letter count
	return count


# call function and display the letter count
print(letterFrequency('factorial.py', 'g'))
