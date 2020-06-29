# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import math


def check_for_primality(num):
	root_num = math.ceil(math.sqrt(num))

	possible_factor = 2

	while possible_factor <= root_num:
		if num % possible_factor == 0:
			return False
		possible_factor += 1
	print(num)
	return True


if __name__ == "__main__":
	# start at 2, to 2 million
	sum = 2

	for i in range(3, 2000001):
		if check_for_primality(i):
			sum += i

	print("Sum = ", sum)
