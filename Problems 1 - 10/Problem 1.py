# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def determine_if_multiple_of_3_or_5(number):
	"""Return whether the number is a multiple of 3 or 5.
	"""
	if number % 3 == 0 or number % 5 == 0:
		return True
	else:
		return False


if __name__ == '__main__':
	total = 0

	for i in range(1, 1000):
		if determine_if_multiple_of_3_or_5(i):
			total = total + i

	print(total)
