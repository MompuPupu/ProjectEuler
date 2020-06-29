# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

number = 600851475143
# number = 13195


def determine_if_prime(num):
	"""

	:param num: number to test
	:return: true if prime
	"""
	i = 2

	root_num = math.sqrt(num)

	while i <= root_num:
		if num % i == 0:
			return False
		i += 1

	return True


def determine_if_factor(num):
	""" Determines if a given number is a factor of the global number

	:param num:
	:return: returns array with the two factors if they are factors, else returns false
	"""
	global number

	if number % num == 0:
		factor_pair = [num, math.floor(number / num)]
		print("Factor pair = ", factor_pair)
		return factor_pair
	else:
		return False

if __name__ == '__main__':
	known_factors = []

	root_num = math.sqrt(number)

	# run through all numbers from 1 to the sqrt of the number to find all factors. Load all factors into a list
	for i in range(1, math.ceil(root_num)):
		possible_factors = determine_if_factor(i)
		if possible_factors:
			known_factors.append(possible_factors[0])
			known_factors.append(possible_factors[1])

	known_factors.sort()

	# initialise looping variable to false. We need to loop over the array backwards and check each factor for primality
	prime_factor_found = False
	index_to_check = len(known_factors) - 1

	while not prime_factor_found:
		possible_prime = known_factors[index_to_check]
		if determine_if_prime(possible_prime):
			largest_prime_factor = possible_prime
			prime_factor_found = True
		else:
			index_to_check -= 1

	print("Largest prime factor is: ", largest_prime_factor)
