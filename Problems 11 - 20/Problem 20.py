# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!


def calculate_factorial(num):
	answer = 1

	for i in range(1, num + 1):
		answer *= i

	return answer


def sum_digits(num):
	num_string = str(num)
	answer = 0

	for c in num_string:
		answer += int(c)

	return answer


if __name__ == '__main__':
	print(sum_digits(calculate_factorial(100)))

