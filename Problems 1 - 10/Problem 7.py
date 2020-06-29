# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math

def check_for_primality(num):
	root_num = math.ceil(math.sqrt(num))

	possible_factor = 2

	while possible_factor <= root_num:
		if num % possible_factor == 0:
			return False
		possible_factor += 1

	return True

if __name__ == "__main__":
	# start with one prime found (2) to simplify incrementing through odd numbers
	primes_found = 1
	test_num = 3

	while primes_found < 10001:
		if check_for_primality(test_num):
			primes_found += 1
			print(primes_found)
		else:
			test_num += 2

	print(test_num)