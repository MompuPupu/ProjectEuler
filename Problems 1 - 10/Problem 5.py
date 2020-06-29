# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# the below is wildly inefficient.
# the true solution is to find the prime factors of all of the numbers in the range (in this case, 1 to 20) and multiply them together

# TODO: code proper solution

def check_divisibility(num):
	for i in range(1, 21):
		if num % i != 0:
			return False
	return True


if __name__ == "__main__":
	solution_found = False
	test_number = 2520

	while not solution_found:
		if check_divisibility(test_number):
			solution_found = True
		else:
			print(test_number)
			test_number += 1

	print(test_number)


