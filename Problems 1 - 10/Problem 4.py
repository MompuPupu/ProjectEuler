# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

import math


def check_for_palindrome(num):
	# loads the number into an array of characters
	digit_list = [int(x) for x in str(num)]

	# iterates through the array, checking if the first is the same as the last, etc.
	for i in range(1, math.floor(len(digit_list) / 2) + 1):
		if digit_list[i - 1] != digit_list[-i]:
			return False
	print(digit_list)
	return True


def check_if_multiple_of_three_digits(num):
	for i in range(999, 99, -1):
		if num % i == 0:
			other_factor = num / i
			if other_factor > 99 and other_factor < 1000:
				return True
	return False


if __name__ == "__main__":
	test_number = 998001
	solution_found = False
	# 100 * 100 to 999 * 999 = 10,000 to 998,001

	while not solution_found:
		if check_for_palindrome(test_number):
			if check_if_multiple_of_three_digits(test_number):
				solution = test_number
				solution_found = True
			else:
				test_number -= 1
		else:
			test_number -= 1

	print(solution)
